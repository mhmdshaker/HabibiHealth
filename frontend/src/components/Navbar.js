import React from 'react';
import './Navbar.css';
const Navbar = () => {
  return (
    <nav>
      {/* Your logo here */}
      <div>Habibi Health</div>
      
      {/* Navigation links */}
      <div>
        <a href="/about">ABOUT</a>
        <a href="/food">FOOD</a>
        {/* Add more links as needed */}
      </div>

      {/* Authentication links */}
      <div>
        <button>Log In</button>
        <button>Sign Up</button>
      </div>
    </nav>
  );
};

export default Navbar;