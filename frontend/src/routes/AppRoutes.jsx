import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Home from '../pages/Home';
import Login from '../pages/Login';
import Signup from '../pages/Signup';
import ProtectedRoute from './ProtectedRoute';
import Presentation from '../pages/Presentation';
import Prediction from '../pages/Usuario/Prediction';
import PredictionDetail from '../pages/Usuario/PredictionDetail';
import Profile from '../pages/Usuario/Profile';

const AppRoutes = () => {
  return (
    
      <Routes>
        {/* Ruta raíz: Redirige a /home o /login según autenticación */}
        <Route path="/" element={<Navigate to="/home" />} />

        {/* Rutas públicas */}
        <Route path="/home" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />

        {/* Rutas protegidas */}
        
        <Route
          path="/presentation"
          element={
            <ProtectedRoute>
              <Presentation />
            </ProtectedRoute>
          }
        />
        <Route
          path="/prediction"
          element={
            <ProtectedRoute>
              <Prediction />
            </ProtectedRoute>
          }
        />
        <Route
          path="/prediction/:id"
          element={
            <ProtectedRoute>
              <PredictionDetail />
            </ProtectedRoute>
          }
        />
        <Route
          path="/profile"
          element={
            <ProtectedRoute>
              <Profile />
            </ProtectedRoute>
          }
        />

        {/* Ruta 404: Página no encontrada */}
        <Route path="*" element={<div>Página no encontrada</div>} />
      </Routes>
  
  );
};

export default AppRoutes;


/* import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from '../pages/Home';
import Login from '../pages/Login';
import Signup from '../pages/Signup';
import ProtectedRoute from './ProtectedRoute';
import Presentation from '../pages/Presentation';
import Prediction from '../pages/Prediction';
import PredictionDetail from '../pages/PredictionDetail';
import Profile from '../pages/Profile';
import Dashboard from '../pages/Dashboard';

const AppRoutes = () => {
  return (

      <Routes>
  
        <Route 
          path="/login/home" 
          element={<Home />} 
        />
        <Route 
          path="/login" 
          element={<Login />} 
        />
        <Route 
          path="/login/signup" 
          element={<Signup />} 
        />

        <Route 
          path="/dashboard" 
          element={<Dashboard />} 
        />
        <Route 
          path="/login/dashboard" 
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>} 
        />
        <Route 
          path="/login/presentation" 
          element={
            <ProtectedRoute>
              <Presentation/>
            </ProtectedRoute>} 
        />
        <Route 
          path="/login/predict" 
          element={
            <ProtectedRoute>
              <Prediction />
            </ProtectedRoute>} 
        />
        <Route 
          path="/login/prediction/:id" 
          element={
              <ProtectedRoute>
                <PredictionDetail />
              </ProtectedRoute>} 
        />
        <Route 
          path="/login/profile" 
          element={
            <ProtectedRoute>
              <Profile />
            </ProtectedRoute>} 
        />
      </Routes>
  );
};

export default AppRoutes; */
