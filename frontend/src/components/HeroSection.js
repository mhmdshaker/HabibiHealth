import React from 'react';
import './HeroSection.css';
const HeroSection = () => {
  return (
    <div className="hero-section">
      <h1>Fitness starts with what you eat.</h1>
      <p>Take control of your goals. Track calories, break down ingredients, and log activities with Habibi Health.</p>
      <button>START FOR FREE</button>
      <p>Already have an account? <a href="/login">Login</a></p>
    </div>
  );
};

export default HeroSection;