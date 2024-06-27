document
  .getElementById("find-cartridges")
  .addEventListener("click", function () {
    let brand = document.getElementById("printer-brand").value;
    let series = document.getElementById("printer-series").value;
    let model = document.getElementById("printer-model").value;
    alert(`Searching for cartridges for ${brand} ${series} ${model}`);
  });
