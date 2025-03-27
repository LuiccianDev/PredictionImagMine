const API_URL = "http://localhost:5000/api/locations"; // Ajusta según tu backend

export const getLocations = async () => {
  const response = await fetch(API_URL);
  return response.json();
};

export const createLocation = async (locationData) => {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(locationData),
  });
  return response.json();
};
