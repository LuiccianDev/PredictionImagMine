import React from 'react';
import { Outlet } from 'react-router-dom';

const AppDevices = () => {
  return (
    <div>
      <h2>Sección de Dispositivos</h2>
      <Outlet />
    </div>
  );
};

export default AppDevices;
