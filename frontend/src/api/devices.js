const API_URL = "http://localhost:5000/api/devices"; // Ajusta según tu backend

export const getDevices = async () => {
  const response = await fetch(API_URL);
  return response.json();
};

export const createDevice = async (deviceData) => {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(deviceData),
  });
  return response.json();
};
