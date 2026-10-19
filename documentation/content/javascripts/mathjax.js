
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

function typesetMath() {
  if (typeof MathJax !== "undefined" && MathJax.typesetPromise) {
    MathJax.startup.output.clearCache();
    MathJax.typesetClear();
    MathJax.texReset();
    MathJax.typesetPromise().catch(function(err) {
      console.warn("MathJax typeset error:", err);
    });
  }
}

if (typeof document$ !== "undefined") {
  document$.subscribe(typesetMath);
}

document.addEventListener("DOMContentLoaded", function() {
  typesetMath();

  const contentArea = document.querySelector(".md-content") || document.body;
  if (contentArea && window.MutationObserver) {
    const observer = new MutationObserver(function(mutations) {
      for (const mutation of mutations) {
        for (const node of mutation.addedNodes) {
          if (node.nodeType === 1) {
            if (
              (node.matches && node.matches(".arithmatex")) ||
              (node.querySelector && node.querySelector(".arithmatex"))
            ) {
              if (!node.querySelector("mjx-container") && !node.matches("mjx-container")) {
                typesetMath();
                return;
              }
            }
          }
        }
      }
    });

    observer.observe(contentArea, { childList: true, subtree: true });
  }
});

