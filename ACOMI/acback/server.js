const express = require("express");
const path = require("path");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

// ✅ MongoDB Connection
mongoose.connect("mongodb://localhost:27017/mybooks");

const db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error:"));
db.once("open", function() {
  console.log("✅ MongoDB connected");
});

// ✅ Mongoose Schema and Model
const bookSchema = new mongoose.Schema({
  title: String,
  author: String,
  cover: String,
  pdf: String,
});

const Book = mongoose.model("comic", bookSchema);

// ✅ API endpoint - Get all comics
app.get("/comic", async (req, res) => {
  try {
    const books = await Book.find();
    res.json(books);
  } catch (err) {
    console.error("Database error:", err);
    res.status(500).json({ error: "Failed to fetch comics" });
  }
});

// ✅ Serve static files BEFORE React catch-all
app.use("/thumb", express.static(path.join(__dirname, "comic/savita/thumb")));
app.use("/savita", express.static(path.join(__dirname, "comic/savita")));

// ✅ Serve React frontend dist folder
app.use(express.static(path.join(__dirname, "../acfront/dist")));

app.use("/thumb", express.static(path.join(__dirname, "comic/savita/thumb"), {
    dotfiles: 'deny',
    index: false
  }), (req, res, next) => {
    console.log("Thumb request:", req.path, "File requested:", req.url);
    next();
  });
  

// ✅ Catch-all route for React Router (LAST - after all other middleware)
app.use((req, res) => {
  res.sendFile(path.join(__dirname, "../acfront/dist/index.html"));
});

// ✅ Start server
app.listen(PORT, () => {
  console.log(`🚀 Server running at http://localhost:3000`);
});
