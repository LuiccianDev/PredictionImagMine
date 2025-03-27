import React from 'react';
import { Outlet } from 'react-router-dom';

const AppUsers = () => {
  return (
    <div>
      <h2>Sección de Usuarios</h2>
      <Outlet />
    </div>
  );
};

export default AppUsers;
