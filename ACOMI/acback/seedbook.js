// seedBooks.js
const mongoose = require("mongoose");

const books = [];

  books.push({
    title: ` Savita Bhabhi - EP 14 - Sexpress!.pdf`,
    author: "Kirutu",
    cover: `/comic/savita/thumb/Savita Bhabhi - EP 14 - Sexpress!.jpg`,
    pdf: `/comic/savita/Savita Bhabhi - EP 14 - Sexpress!.pdf`
  });

const bookSchema = new mongoose.Schema({
  title: String,
  author: String,
  cover: String,
  pdf: String
});

const Book = mongoose.model("Comic", bookSchema);

mongoose.connect("mongodb://localhost:27017/mybooks", {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(async () => {
  await Book.deleteMany(); // clear old data
  await Book.insertMany(books);
  console.log("✅ All books inserted");
  process.exit();
}).catch(err => {
  console.error("❌ Error connecting to MongoDB:", err);
});
