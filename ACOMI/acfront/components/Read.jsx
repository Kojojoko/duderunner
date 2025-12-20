import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { data } from './Info'
import NavBar from './NavBar';
import "../src/index.css"

const Read = () => {
  const { rid } = useParams();
  const read = data.find(c => c.id == rid)
  const [books, setBooks] = useState([]);
  const API_URL = "http://localhost:3000/comic"

  useEffect(() => {
    fetch(API_URL, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
      mode: "cors",
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error(`HTTP error! Status: ${res.status}`);
        }
        return res.json();
      })
      .then((data) => {
        console.log("Fetched data:", data);
        setBooks(data);
      })
      .catch((err) => {
        console.error("Fetch error:", err);
      });
  }, []);

  return (
    <>
      <NavBar />
      <div className="carousel">
        <div className="view">
          <div className='imgview'>
            <img src={read.image} alt={read.title} />
          </div>
          <div className='grid'>
            <div className="book-grid">
              {books.map((book) => (
                <div key={book._id} className="book-card">
                 <img 
      src={`http://localhost:3000${book.cover}`} 
      alt={book.title} 
      className="book-cover"
      onError={() => console.log("Failed to load:", `http://localhost:3000${book.cover}`)}
    />
                  <h5 className="book-title">{book.title}</h5>
                  <h6 className="book-author">{book.author}</h6>
                  <button
                    className="read-btn"
                    onClick={() => {
                      const pdfUrl = `http://localhost:3000${book.pdf}`;
                      console.log("Opening PDF:", pdfUrl);
                      window.open(pdfUrl, "_blank");
                    }}
                  >
                    Read PDF
                  </button>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default Read
