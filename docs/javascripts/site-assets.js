/* Resolve paths to files under the MkDocs site root (GitHub Pages: /nmcb-handover-docs/). */
(function () {
  function siteRoot() {
    var match = location.pathname.match(/^(.*\/nmcb-handover-docs\/)/);
    if (match) return match[1];
    if (location.pathname.indexOf("/nmcb-handover-docs") !== -1) {
      return location.pathname.split("/nmcb-handover-docs")[0] + "/nmcb-handover-docs/";
    }
    return "/";
  }

  window.nmcbAssetUrl = function (relativePath) {
    return siteRoot() + String(relativePath).replace(/^\//, "");
  };
})();
