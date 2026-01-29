async function uploadAndGenerate() {
  const file = document.getElementById("pdf").files[0];

  if (!file) {
    alert("Please select a PDF file first");
    return;
  }

  const form = new FormData();
  form.append("file", file);

  // 1️⃣ Upload file
  await fetch("/upload", {
    method: "POST",
    body: form
  });

  // 2️⃣ Auto-generate PDFs
  const res = await fetch(`/generate-pdf?filename=${file.name}`, {
    method: "POST"
  });

  const data = await res.json();

  // 3️⃣ Show download links
  document.getElementById("summaryLink").href = data.summary;
  document.getElementById("summaryLink").innerText = "📄 Download Tender Summary";

  document.getElementById("impLink").href = data.points;
  document.getElementById("impLink").innerText = "📄 Download Important Points";
}
