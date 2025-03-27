import React, { useState, useEffect } from "react";
import { getLocations, createLocation } from "../../api/locations";
import LocationForm from "../../components/LocationsForm/LocationsForm";

const Locations = () => {
  const [locations, setLocations] = useState([]);

  useEffect(() => {
    fetchLocations();
  }, []);

  const fetchLocations = async () => {
    const data = await getLocations();
    setLocations(data);
  };

  const handleCreateLocation = async (locationData) => {
    await createLocation(locationData);
    fetchLocations();
  };

  return (
    <div>
      <h1>Ubicaciones</h1>
      <LocationForm onSubmit={handleCreateLocation} />
      <ul>
        {locations.map((location) => (
          <li key={location.id}>
            {location.name} - ({location.latitude}, {location.longitude}) - {location.country}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Locations;
