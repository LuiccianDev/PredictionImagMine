import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuthContext } from '../context/AuthContext';

const ProtectedRoute = ({ children }) => {
  const { user, loading } = useAuthContext();

  if (loading) {
    return <div>Cargando...</div>; // Muestra un spinner o mensaje de carga
  }

  if (!user) {
    return <Navigate to="/login" />; // Redirige al login si no está autenticado
  }

  return children; // Renderiza el componente protegido
};

export default ProtectedRoute;



/* import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuthContext } from '../context/AuthContext';

const ProtectedRoute = ({ children }) => {
  const { user } = useAuthContext();

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  return children;
};

export default ProtectedRoute; */
