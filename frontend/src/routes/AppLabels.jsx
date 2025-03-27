import React from 'react';
import { Outlet } from 'react-router-dom';

const AppLabels = () => {
  return (
    <div>
      <h2>Sección de Etiquetas</h2>
      <Outlet />
    </div>
  );
};

export default AppLabels;
