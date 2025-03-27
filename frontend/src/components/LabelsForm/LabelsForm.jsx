import React, { useState } from "react";

const LabelForm = ({ predictionId, onSubmit }) => {
  const [labelData, setLabelData] = useState({
    real_label: "",
    feedback: false,
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setLabelData({
      ...labelData,
      [name]: type === "checkbox" ? checked : value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ ...labelData, prediction_id: predictionId });
    setLabelData({ real_label: "", feedback: false });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="real_label"
        placeholder="Etiqueta real"
        value={labelData.real_label}
        onChange={handleChange}
        required
      />
      <label>
        <input
          type="checkbox"
          name="feedback"
          checked={labelData.feedback}
          onChange={handleChange}
        />
        Confirmar predicción
      </label>
      <button type="submit">Enviar Etiqueta</button>
    </form>
  );
};

export default LabelForm;
