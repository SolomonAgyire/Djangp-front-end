document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("invoiceForm");
  const resultDiv = document.querySelector(".result-content");

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    resultDiv.innerHTML = "<p>Loading...</p>";

    const fileInput = document.getElementById("imageUpload");
    const file = fileInput.files[0];

    if (!file || !file.type.startsWith("image/")) {
      resultDiv.innerHTML = "<p>Please upload a valid image file.</p>";
      return;
    }

    const formData = new FormData(form);

    fetch("http://your-backend-url/extract-invoice-data", {
      method: "POST",
      body: formData
    })
      .then((response) => response.json())
      .then((data) => {
        resultDiv.innerHTML = formatData(data);
      })
      .catch((error) => {
        console.error("Error:", error);
        resultDiv.innerHTML =
          "<p>Error extracting data from invoice. Please try again later.</p>";
      });
  });

  function formatData(data) {
    let formattedHTML = "";

    for (const [key, value] of Object.entries(data)) {
      formattedHTML += `<div class="result-item"><strong>${key}:</strong> ${value}</div>`;
    }

    return formattedHTML;
  }
});
