import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import styles from '../styles/Signup.module.css';
import axios from 'axios';
import { API_URL } from "../config/api"; // Ensure this matches the named export

const Signup = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    confirmPassword: '',
  });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Validación de contraseñas
    if (formData.password !== formData.confirmPassword) {
      setError('Las contraseñas no coinciden');
      return;
    }

    // Validación de que el correo sea de Gmail
    const emailRegex = /^[a-zA-Z0-9._%+-]+@gmail\.com$/;
    if (!emailRegex.test(formData.email)) {
      setError('Por favor, introduce un correo electrónico válido de Gmail');
      return;
    }

    try {
      // Se envían los datos al backend. Usa el endpoint adecuado.
      const response = await axios.post(
        (`${API_URL}/auths/signup`), //! Endpoint cambion cone l bacjkend 
        {
          username: formData.username,
          email: formData.email,
          password: formData.password,
        }
      );
      
      // Si el registro es exitoso, redirige al usuario a la página de login
      navigate('/login');
    } catch (err) {
      console.error('Error al crear cuenta:', err);
      setError('Error al crear la cuenta. Inténtalo de nuevo.');
    }
  };

  return (
    <div className={styles.signupContainer}>
      <form className={styles.signupForm} onSubmit={handleSubmit}>
        <h2>Crear Cuenta</h2>
        {error && <p className={styles.error}>{error}</p>}
        <input
          type="text"
          name="username"
          placeholder="Nombre de usuario"
          value={formData.username}
          onChange={handleChange}
          required
        />
        <input
          type="email"
          name="email"
          placeholder="Correo electrónico (Gmail)"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Contraseña"
          value={formData.password}
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="confirmPassword"
          placeholder="Confirmar contraseña"
          value={formData.confirmPassword}
          onChange={handleChange}
          required
        />
        <button type="submit">Crear Cuenta</button>
      </form>
    </div>
  );
};

export default Signup;
