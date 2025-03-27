import React, { useState } from "react";

const LocationForm = ({ onSubmit }) => {
  const [locationData, setLocationData] = useState({
    name: "",
    latitude: "",
    longitude: "",
    country: "",
  });

  const handleChange = (e) => {
    setLocationData({
      ...locationData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(locationData);
    setLocationData({ name: "", latitude: "", longitude: "", country: "" });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="name"
        placeholder="Nombre de la ubicación"
        value={locationData.name}
        onChange={handleChange}
        required
      />
      <input
        type="number"
        step="any"
        name="latitude"
        placeholder="Latitud"
        value={locationData.latitude}
        onChange={handleChange}
        required
      />
      <input
        type="number"
        step="any"
        name="longitude"
        placeholder="Longitud"
        value={locationData.longitude}
        onChange={handleChange}
        required
      />
      <input
        type="text"
        name="country"
        placeholder="País"
        value={locationData.country}
        onChange={handleChange}
      />
      <button type="submit">Agregar Ubicación</button>
    </form>
  );
};

export default LocationForm;
