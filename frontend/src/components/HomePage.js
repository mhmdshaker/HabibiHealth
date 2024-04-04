import React from 'react';
import Navbar from './Navbar';
import HeroSection from './HeroSection';
import { Link } from 'react-router-dom';


const HomePage = () => {
  return (
    <div>
      <Navbar />
      <HeroSection />
      {/* Add more sections as needed */}
      <div className="home-section">
        <Link to="/search-food" className="home-search-food-link">
          Explore Foods
        </Link>
      </div>
    </div>
  );
};

export default HomePage;