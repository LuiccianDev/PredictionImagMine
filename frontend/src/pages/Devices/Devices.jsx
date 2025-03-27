import React, { useState, useEffect } from "react";
import { getDevices, createDevice } from "../../api/devices";
import DeviceForm from "../../components/DevicesForm/DevicesForm";

const Devices = () => {
  const [devices, setDevices] = useState([]);

  useEffect(() => {
    fetchDevices();
  }, []);

  const fetchDevices = async () => {
    const data = await getDevices();
    setDevices(data);
  };

  const handleCreateDevice = async (deviceData) => {
    await createDevice(deviceData);
    fetchDevices();
  };

  return (
    <div>
      <h1>Dispositivos</h1>
      <DeviceForm onSubmit={handleCreateDevice} />
      <ul>
        {devices.map((device) => (
          <li key={device.id}>
            {device.device_name} - {device.manufacturer} ({device.type})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Devices;
