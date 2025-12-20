import React, { useState, useRef } from 'react';
import { Outlet, Link } from "react-router-dom";

// Pass your images as imports or via props accordingly.
// For example you can import them like:
// import savitaImg from './path_to_images/savita.jpg';
// (Adapt this import to your setup)

const Carousel = ({ data }) => {
  const [items, setItems] = useState(data);
  const [animClass, setAnimClass] = useState('');
  const [buttonsDisabled, setButtonsDisabled] = useState(false);
  const [showDetail, setShowDetail] = useState(false);
  const [detailIndex, setDetailIndex] = useState(null); // Which item detail to show
  const timeoutRef = useRef(null);


  const showSlider = (type) => {
    setButtonsDisabled(true);
    setAnimClass('');
  
    Promise.resolve().then(() => {
      let newItems = [...items];
      if (type === 'next') {
        newItems.push(newItems.shift());
        setAnimClass('next');
      } else {
        newItems.unshift(newItems.pop());
        setAnimClass('prev');
      }
      setItems(newItems);
  
      if (timeoutRef.current) clearTimeout(timeoutRef.current);
      timeoutRef.current = setTimeout(() => setButtonsDisabled(false), 100);
    });
  };
  

  // Show the detail section for the clicked item
  const handleSeeMore = (index) => {
    setShowDetail(true);
    setDetailIndex(index);
    setAnimClass('showDetail');
  };

  // Back to main carousel
  const handleBack = () => {
    setAnimClass('');
    setShowDetail(false);
    setDetailIndex(null);
  };

  return (
    <div className={`carousel${animClass ? ' ' + animClass : ''}`}>
      <div className="list">
        {items.map((item, index) => (
          <div className={`item position-${index+1}`} key={index}>
            {console.log(index+1)}
            <img src={item.image} alt={item.name} />
            <div className="introduce">

              <div className="topic">{item.name}</div>
              <div className="des">
                {/* Truncate or limit the description if needed */}
                {item.description.length > 100
                  ? item.description.substring(0, 100) + '...'
                  : item.description}
              </div>
              <button
                className="seeMore"
                onClick={() => handleSeeMore(index)}
                disabled={showDetail}
              >
                SEE MORE &#8599;
              </button>
            </div>

            {/* Show detail only for selected item */}
            {showDetail && detailIndex === index && (
              <div className="detail">
                <div className="title">{item.name}</div>
                <div className="des">{item.description}</div>
                {/* You can add more details/specifications below if you want */}
                {/* For demo purposes, a simple Checkout buttons area */}
                <div className="checkout">
                  <Link to={`/Read/${item.id}`} className='btn'>
                  READ
                  </Link>
                </div>
              </div>
            )}
          </div>
        ))}
      </div>

      <div className="arrows">
        <button id="prev" onClick={() => showSlider('prev')} disabled={buttonsDisabled || showDetail}>
          &lt;
        </button>
        <button id="next" onClick={() => showSlider('next')} disabled={buttonsDisabled || showDetail}>
          &gt;
        </button>
        {/* Show "Back" (See All) only when detail is active */}
        {showDetail ? (
          <button id="back" onClick={handleBack}>
            GO BACK &#8599;
          </button>
        ) : null}
      </div>
    </div>
  );
};

export default Carousel;
