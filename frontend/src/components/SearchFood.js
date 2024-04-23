// src/components/SearchFood.js

import React, { useState } from 'react';
import './SearchFood.css';

export const SearchFood = () => {
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    // Implement search logic here
    console.log('Searching for:', searchTerm);
  };

  return (
    <div className="search-food-container">
      <h2>Discover Foods</h2>
      <form onSubmit={handleSearchSubmit} className="search-food-form">
        <input
          type="text"
          placeholder="Search for foods..."
          value={searchTerm}
          onChange={handleSearchChange}
          className="search-food-input"
        />
        <button type="submit" className="search-food-button">Search</button>
      </form>
    </div>
  );
};

export default SearchFood;