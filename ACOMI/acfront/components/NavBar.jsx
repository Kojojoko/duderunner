import React from 'react'
import "../src/index.css"
import { Outlet, Link } from "react-router-dom";

const NavBar = () => {
  return (
    <header>
        <div className='logo'>
            <h3>ACOMIC</h3>
        </div>
        <nav>
            <ul>
                <li>
                   <Link to="/">Home</Link>
                </li>
                <li>
                    <Link to="/Category">Categories</Link>
                </li>
                <li>
                    Info
                </li>
            </ul>
        </nav>
    </header>
  )
}

export default NavBar