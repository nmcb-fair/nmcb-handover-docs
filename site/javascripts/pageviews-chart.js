/* Site usage page: bar charts from pageviews-data.json */
(function () {
  if (!/\/site-usage\/?$/.test(location.pathname)) return;

  var chartJs =
    "https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js";

  function el(id) {
    return document.getElementById(id);
  }

  function loadScript(src) {
    return new Promise(function (resolve, reject) {
      var s = document.createElement("script");
      s.src = src;
      s.onload = resolve;
      s.onerror = reject;
      document.head.appendChild(s);
    });
  }

  function renderMeta(data) {
    var meta = el("pageviews-meta");
    if (!meta) return;
    if (!data.configured) {
      meta.innerHTML =
        "<p><strong>Statistics are not available yet.</strong> " +
        (data.message || "Configure GoatCounter and GitHub secrets, then redeploy.") +
        "</p>";
      return;
    }
    meta.innerHTML =
      "<p>Unique visitors in the last <strong>" +
      data.periodDays +
      "</strong> days (GoatCounter). Last updated: <strong>" +
      data.updated +
      "</strong>. Total across listed pages: <strong>" +
      data.totalVisitors.toLocaleString() +
      "</strong>.</p>";
  }

  function barChart(canvasId, labels, values, label) {
    var canvas = el(canvasId);
    if (!canvas || !labels.length) return;
    new Chart(canvas.getContext("2d"), {
      type: "bar",
      data: {
        labels: labels,
        datasets: [
          {
            label: label,
            data: values,
            backgroundColor: "rgba(63, 81, 181, 0.65)",
            borderColor: "rgba(63, 81, 181, 1)",
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        indexAxis: canvasId === "pageviews-by-page" ? "y" : "x",
        plugins: {
          legend: { display: false },
        },
        scales: {
          x: { beginAtZero: true, ticks: { precision: 0 } },
          y: { beginAtZero: true, ticks: { precision: 0 } },
        },
      },
    });
  }

  function renderTable(pages) {
    var tbody = el("pageviews-table-body");
    if (!tbody) return;
    tbody.innerHTML = "";
    pages.forEach(function (row) {
      var tr = document.createElement("tr");
      tr.innerHTML =
        "<td><code>" +
        row.path +
        "</code></td>" +
        "<td>" +
        (row.title || "—") +
        "</td>" +
        "<td>" +
        row.section +
        "</td>" +
        "<td style=\"text-align:right\">" +
        row.visitors.toLocaleString() +
        "</td>";
      tbody.appendChild(tr);
    });
  }

  fetch(new URL("pageviews-data.json", document.baseURI))
    .then(function (r) {
      return r.json();
    })
    .then(function (data) {
      renderMeta(data);
      if (!data.configured || !data.sections.length) return;

      return loadScript(chartJs).then(function () {
        barChart(
          "pageviews-by-section",
          data.sections.map(function (s) {
            return s.label;
          }),
          data.sections.map(function (s) {
            return s.visitors;
          }),
          "Visitors"
        );

        var top = (data.pages || []).slice(0, 20);
        barChart(
          "pageviews-by-page",
          top.map(function (p) {
            return p.path;
          }),
          top.map(function (p) {
            return p.visitors;
          }),
          "Visitors"
        );

        renderTable(data.pages || []);
      });
    })
    .catch(function (err) {
      var meta = el("pageviews-meta");
      if (meta) meta.textContent = "Could not load pageviews-data.json: " + err;
    });
})();
