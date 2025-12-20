import { useState } from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import './App.css'
import NavBar from '../components/NavBar'
import Silder from '../components/Silder'
import Read from "../components/Read"
import Categories from '../components/Categories';

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <BrowserRouter>
      <Routes>
        <Route path="/" element={<Silder />}></Route>
        <Route path="/Read/:rid" element={<Read/>}/>
        <Route path="/Category" element={<Categories/>}/>
          </Routes></BrowserRouter>
      
    
   
    </>
  )
}

export default App
