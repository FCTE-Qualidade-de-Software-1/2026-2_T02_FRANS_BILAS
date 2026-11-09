#!/usr/bin/env python3
"""Cross-check all G2 totals and each method against the original RuboCop JSON."""
import csv
import json
import math
import re
import sys
from pathlib import Path


def verify(folder):
    def rows(name):
        with (folder / name).open(newline="", encoding="utf-8") as stream:
            return list(csv.DictReader(stream))

    summary = json.loads((folder / "summary.json").read_text())
    classes = rows("M2.1-classes.csv")
    methods = rows("M2.2-methods.csv")
    files = rows("M2.3-sloc.csv")
    specs = rows("M2.4-specs.csv")
    total = len({row["name"] for row in classes})
    overrides = {row["name"] for row in classes if row["override"] == "true"}
    covered = {row["name"] for row in specs if row["specs"]}
    expected_specs = {(row["path"], row["name"], row["specs"])
                      for row in classes if row["override"] == "true"}
    assert {(row["path"], row["name"], row["specs"]) for row in specs} == expected_specs
    assert len({(row["path"], row["line"]) for row in methods}) == len(methods)
    assert summary["M2.1"]["classes"] == total
    assert summary["M2.1"]["overrides"] == len(overrides)
    assert math.isclose(summary["M2.1"]["percent"], 100 * len(overrides) / total)
    assert summary["M2.4"]["overrides"] == len(overrides)
    assert summary["M2.4"]["with_spec"] == len(covered)
    assert math.isclose(summary["M2.4"]["percent"], 100 * len(covered) / len(overrides))
    for metric, records, key, count_key, sum_key in [
        ("M2.2", methods, "complexity", "methods", "sum"),
        ("M2.3", files, "sloc", "class_files", "sloc"),
    ]:
        values = [int(row[key]) for row in records]
        assert summary[metric][count_key] == len(values)
        assert summary[metric][sum_key] == sum(values)
        assert summary[metric]["maximum"] == max(values)
        assert math.isclose(summary[metric]["mean"], sum(values) / len(values))
    raw = json.loads((folder / "M2.2-rubocop.json").read_text())
    assert raw["summary"]["offense_count"] == sum(len(file["offenses"]) for file in raw["files"])
    reported = {}
    for file in raw["files"]:
        for offense in file["offenses"]:
            assert offense["cop_name"] == "Metrics/CyclomaticComplexity", offense
            path = "app/" + file["path"].split("app/", 1)[1]
            key = (path, offense["location"]["start_line"])
            assert key not in reported
            reported[key] = int(re.search(r"\[(\d+)/0\]", offense["message"])[1])
    empty = []
    for row in methods:
        key = (row["path"], int(row["line"]))
        if key in reported:
            assert reported.pop(key) == int(row["complexity"]), row
        else:
            assert row["empty"] == "true" and int(row["complexity"]) == 1, row
            empty.append(row)
    assert not reported, reported
    # Missing entries are listed for inspection: the CLI omits empty methods.
    print(json.dumps({"totals_verified": True, "rubocop_offenses": raw["summary"]["offense_count"],
                      "methods_not_reported_by_cli": empty}, indent=2))


if __name__ == "__main__":
    verify(Path(sys.argv[1]))
