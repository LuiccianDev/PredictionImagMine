const API_URL = "http://localhost:5000/api/labels"; // Ajusta según tu backend

export const getLabels = async () => {
  const response = await fetch(API_URL);
  return response.json();
};

export const createLabel = async (labelData) => {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(labelData),
  });
  return response.json();
};
