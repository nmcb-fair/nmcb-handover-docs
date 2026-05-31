/* Allow Mermaid click links to internal doc pages (Material for MkDocs). */
document$.subscribe(function () {
  if (typeof mermaid === "undefined") return;
  mermaid.initialize({
    startOnLoad: false,
    securityLevel: "loose",
  });
});
