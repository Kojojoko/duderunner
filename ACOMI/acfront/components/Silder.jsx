import React, { useState } from 'react'
import "../src/index.css"

import Carousel from "./Carousel"
import NavBar from './NavBar';
import {data} from './Info';



const Silder = () => { 
 


 
  return (
   <>
   <NavBar/>
    <Carousel data={data}/>
   </>
  )
}

export default Silder