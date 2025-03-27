import React from 'react';
import { Outlet } from 'react-router-dom';

const AppLocation = () => {
  return (
    <div>
      <h2>Sección de Ubicación</h2>
      <Outlet />
    </div>
  );
};

export default AppLocation;
