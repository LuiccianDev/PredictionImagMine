import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Navbar from '../../components/Navbar/Navbar';
import styles from '../../styles/Profile.module.css';
import { useAuthContext } from '../../context/AuthContext'; // ✅ Importar el contexto de autenticación
import API_URL from '../../config/api';

const Profile = () => {
  const { user, loading: authLoading } = useAuthContext(); // Obtener el usuario y el estado de carga desde el contexto
  const [editing, setEditing] = useState(false);
  const [formData, setFormData] = useState({ username: '', email: '' });
  const [message, setMessage] = useState({ type: '', text: '' });
  const [profileLoading, setProfileLoading] = useState(true);

  // Actualizar el formulario con los datos del usuario cuando cambie
  useEffect(() => {
    if (user) {
      setFormData({
        username: user.username,
        email: user.email,
      });
      setProfileLoading(false);
    }
  }, [user]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const validateForm = () => {
    if (!formData.username.trim()) {
      setMessage({ type: 'error', text: 'El nombre de usuario no puede estar vacío.' });
      return false;
    }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      setMessage({ type: 'error', text: 'El correo electrónico no es válido.' });
      return false;
    }
    return true;
  };

  const handleSave = async (e) => {
    e.preventDefault();
    if (!validateForm()) return;

    try {
      await axios.put(`${API_URL}/user/profile`, formData, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('authToken')}`, // Enviar el token en la solicitud
        },
      });
      setMessage({ type: 'success', text: 'Perfil actualizado exitosamente.' });
      setEditing(false);
      // Actualizar el estado del usuario en el contexto si es necesario
    } catch (error) {
      const errorMessage = error.response?.data?.message || 'Error al actualizar el perfil.';
      setMessage({ type: 'error', text: errorMessage });
    }
  };

  if (authLoading || profileLoading) {
    return <p>Cargando datos del perfil...</p>;
  }

  if (!user) {
    return <p>No estás autenticado. Por favor, inicia sesión.</p>;
  }

  return (
    <>
      <Navbar />
      <div className={styles.profileContainer}>
        <h1>Mi Perfil</h1>
        {editing ? (
          <form onSubmit={handleSave} className={styles.profileForm}>
            <label>
              Usuario:
              <input
                type="text"
                name="username"
                value={formData.username}
                onChange={handleChange}
              />
            </label>
            <label>
              Email:
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
              />
            </label>
            <button type="submit">Guardar</button>
          </form>
        ) : (
          <div className={styles.profileDetails}>
            <p><strong>Usuario:</strong> {user.username}</p>
            <p><strong>Email:</strong> {user.email}</p>
            <button onClick={() => setEditing(true)}>Editar Perfil</button>
          </div>
        )}
        <Message type={message.type} text={message.text} />
      </div>
    </>
  );
};

const Message = ({ type, text }) => {
  if (!text) return null;
  return (
    <div className={`${styles.message} ${styles[type]}`}>
      {text}
    </div>
  );
};

export default Profile;