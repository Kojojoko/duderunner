// generateCovers.js
const fs = require("fs");
const path = require("path");
const { convert } = require("pdf-poppler");

const pdfFolder = path.join("C:/Users/Kumaresa pandiyan/OneDrive/Documents/ACOMI/acback/comic/savita");
const outputFolder = path.join("C:/Users/Kumaresa pandiyan/OneDrive/Documents/ACOMI/acback/comic/savita/","thumb");

if (!fs.existsSync(outputFolder)) {
  fs.mkdirSync(outputFolder);
}

const pdfFiles = fs.readdirSync(pdfFolder).filter(f => f.endsWith(".pdf"));

(async () => {
  for (const file of pdfFiles) {
    const pdfPath = path.join(pdfFolder, file);
    const baseName = path.parse(file).name;

    const options = {
      format: "jpeg",
      out_dir: outputFolder,
      out_prefix: baseName,
      page: 1
    };

    try {
      await convert(pdfPath, options);
      console.log(`✅ Cover generated: ${baseName}.jpg`);
    } catch (err) {
      console.error(`❌ Failed for ${file}:`, err);
    }
  }
})();
