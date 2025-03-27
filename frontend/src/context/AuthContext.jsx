import React, { createContext, useState, useContext, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { API_URL } from '../config/api';
const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true); // Estado de carga
  const navigate = useNavigate();

  // Función para obtener la información del usuario desde el backend
  const fetchUser = async (token) => {
    try {
      const response = await fetch(`${API_URL}/auths/user`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      const data = await response.json();

      if (data.user) {
        setUser(data.user); // Establecer el estado del usuario
        localStorage.setItem('user', JSON.stringify(data.user)); // Guardar en localStorage
      } else {
        // Si no hay usuario, limpiar el localStorage
        localStorage.removeItem('authToken');
        localStorage.removeItem('user');
        setUser(null);
      }
    } catch (error) {
      console.error('Error obteniendo usuario:', error);
      localStorage.removeItem('authToken');
      localStorage.removeItem('user');
      setUser(null);
    } finally {
      setLoading(false); // Finalizar la carga
    }
  };

  // Al cargar la aplicación, verificar el token y obtener el usuario
  useEffect(() => {
    const token = localStorage.getItem('authToken');
    const storedUser = localStorage.getItem('user');

    if (token) {
      // Si hay un token, obtener la información del usuario
      fetchUser(token);
    } else {
      // Si no hay token, limpiar el estado y finalizar la carga
      setUser(null);
      setLoading(false);
    }
  }, []);

  // Función para iniciar sesión
  const login = async (credentials) => {
    try {
      const response = await fetch(`${API_URL}/auths/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(credentials),
      });

      if (!response.ok) {
        throw new Error('Credenciales incorrectas.');
      }

      const data = await response.json();
      setUser(data.user);
      localStorage.setItem('authToken', data.token);
      localStorage.setItem('user', JSON.stringify(data.user));
      return data;
    } catch (error) {
      console.error('Error en login:', error);
      throw error; // Lanzar el error para manejarlo en el componente
    }
  };

  // Función para cerrar sesión
  const logout = () => {
    setUser(null);
    localStorage.removeItem('authToken');
    localStorage.removeItem('user');
    navigate('/'); // Redirigir al login
  };

  return (
    <AuthContext.Provider value={{ user, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuthContext = () => useContext(AuthContext);