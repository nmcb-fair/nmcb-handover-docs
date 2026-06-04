/* Footer: show total visits from pageviews-data.json */
(function () {
  var target = document.getElementById("nmcb-pageview-total");
  if (!target) return;

  fetch(new URL("pageviews-data.json", document.baseURI))
    .then(function (r) {
      return r.json();
    })
    .then(function (data) {
      if (!data.configured) {
        target.textContent = "";
        return;
      }
      target.textContent =
        " · " +
        data.totalVisitors.toLocaleString() +
        " visits (last " +
        data.periodDays +
        "d)";
    })
    .catch(function () {});
})();
