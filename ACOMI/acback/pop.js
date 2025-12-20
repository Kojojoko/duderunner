const mongoose = require("mongoose");
const fs = require("fs");
const path = require("path");

// ✅ MongoDB Connection
mongoose.connect("mongodb://localhost:27017/mybooks");

const db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error:"));
db.once("open", async function() {
  console.log("✅ MongoDB connected");
  await populateDatabase();
  process.exit(0);
});

// ✅ Mongoose Schema and Model
const bookSchema = new mongoose.Schema({
  title: String,
  author: String,
  cover: String,
  pdf: String,
});

const Book = mongoose.model("comic", bookSchema);

// ✅ Auto-populate database from files
async function populateDatabase() {
  try {
    const pdfFolder = path.join(__dirname, "comic/savita");
    const thumbFolder = path.join(__dirname, "comic/savita/thumb");

    // Get all PDF files
    const pdfFiles = fs.readdirSync(pdfFolder).filter(file => file.endsWith(".pdf"));

    console.log(`Found ${pdfFiles.length} PDF files`);

    for (const pdfFile of pdfFiles) {
      // Extract title without extension
      const title = pdfFile.replace(".pdf", "");

      // Find matching thumbnail (same name but with -01.jpg)
      const thumbName = `${title}-01.jpg`;
      const thumbPath = path.join(thumbFolder, thumbName);

      // Check if thumbnail exists
      const thumbExists = fs.existsSync(thumbPath);

      if (!thumbExists) {
        console.log(`⚠️  Skipping ${title} - no matching thumbnail`);
        continue;
      }

      // Check if already in database
      const exists = await Book.findOne({ title });
      if (exists) {
        console.log(`⏭️  Skipping ${title} - already in database`);
        continue;
      }

      // Add to database
      const book = new Book({
        title: title,
        author: "Kirutu",
        cover: `/thumb/${thumbName}`,
        pdf: `/savita/${pdfFile}`,
      });

      await book.save();
      console.log(`✅ Added: ${title}`);
    }

    console.log("🎉 Database population complete!");
  } catch (err) {
    console.error("Error:", err);
  }
}
