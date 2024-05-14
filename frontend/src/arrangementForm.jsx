import React, { useState } from 'react';

const ArrangementForm = () => {
  // State variables to store form data
  const [hardinessZone, setHardinessZone] = useState('');
  const [colorScheme, setColorScheme] = useState({
    red: false,
    blue: false,
    yellow: false,
    orange: false,
    pink: false,
    purple: false,
    white: false,
    black: false,
  });
  const [lightLevel, setLightLevel] = useState('');

  // Function to handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    // TO DO: This should hook up to the plant API
    console.log({ hardinessZone, colorScheme, lightLevel });
  };

  // handle changes in hardiness zone input
  const handleHardinessChange = (event) => {
    setHardinessZone(event.target.value);
  };

  // handle changes in color scheme input
  const handleColorChange = (event) => {
    const { name, checked } = event.target;
    setColorScheme((prevColorScheme) => ({
      ...prevColorScheme,
      [name]: checked,
    }));
  };

  // handle changes in light level input
  const handleLightLevelChange = (event) => {
    setLightLevel(event.target.value);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="hardinessZone">Hardiness Zone:</label>
        <input
          type="number"
          id="hardinessZone"
          value={hardinessZone}
          onChange={handleHardinessChange}
          min="1"
          max="13"
          required
        />
      </div>
      <div>
        <label>Color Scheme:</label>
        <div>
          <label>
            <input
              type="checkbox"
              name="red"
              checked={colorScheme.red}
              onChange={handleColorChange}
            />
            Red
          </label>
        </div>
        <div>
          <label>
            <input
              type="checkbox"
              name="blue"
              checked={colorScheme.blue}
              onChange={handleColorChange}
            />
            Blue
          </label>
        </div>
        <div>
          <label>
            <input
              type="checkbox"
              name="yellow"
              checked={colorScheme.yellow}
              onChange={handleColorChange}
            />
            Yellow
          </label>
        </div>
        <div>
          <label>
            <input
              type="checkbox"
              name="orange"
              checked={colorScheme.orange}
              onChange={handleColorChange}
            />
            Orange
          </label>
        </div>
        <div>
          <label>
            <input
              type="checkbox"
              name="pink"
              checked={colorScheme.pink}
              onChange={handleColorChange}
            />
            Pink
          </label>
        </div>
        <div>
          <label>
            <input
              type="checkbox"
              name="purple"
              checked={colorScheme.purple}
              onChange={handleColorChange}
            />
            Purple
          </label>
        </div>
        <div>
          <label>
            <input
              type="checkbox"
              name="white"
              checked={colorScheme.white}
              onChange={handleColorChange}
            />
            White
          </label>
          <div>
          <label>
            <input
              type="checkbox"
              name="black"
              checked={colorScheme.black}
              onChange={handleColorChange}
            />
            Black
          </label>
        </div>
        </div>
      </div>
      <div>
        <label htmlFor="lightLevel">Light Level:</label>
        <select id="lightLevel" value={lightLevel} onChange={handleLightLevelChange} required>
          <option value="">Select light level</option>
          <option value="full shade">Full Shade</option>
          <option value="part shade">Part Shade</option>
          <option value="part sun">Part Sun</option>
          <option value="full sun">Full Sun</option>
        </select>
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default ArrangementForm;
