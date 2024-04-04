import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
  const navigate = useNavigate();

  return (
    <nav>
      {/* Your logo here */}
      <div>Habibi Health</div>
      
      {/* Navigation links */}
      <div>
        <a href="/about">ABOUT</a>
        <Link to="/search-food">FOOD SEARCH</Link> 
        {/* Add more links as needed */}
      </div>

      {/* Authentication links */}
      <div>
        <button onClick={() => navigate('/login')}>Log In</button>
        <button onClick={() => navigate('/signup')}>Sign Up</button>
      </div>
    </nav>
  );
};

export default Navbar;