import React, { useState } from "react";

const DeviceForm = ({ onSubmit }) => {
  const [deviceData, setDeviceData] = useState({
    device_name: "",
    manufacturer: "",
    type: "",
  });

  const handleChange = (e) => {
    setDeviceData({
      ...deviceData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(deviceData);
    setDeviceData({ device_name: "", manufacturer: "", type: "" });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="device_name"
        placeholder="Nombre del dispositivo"
        value={deviceData.device_name}
        onChange={handleChange}
        required
      />
      <input
        type="text"
        name="manufacturer"
        placeholder="Fabricante"
        value={deviceData.manufacturer}
        onChange={handleChange}
      />
      <input
        type="text"
        name="type"
        placeholder="Tipo"
        value={deviceData.type}
        onChange={handleChange}
      />
      <button type="submit">Agregar Dispositivo</button>
    </form>
  );
};

export default DeviceForm;
