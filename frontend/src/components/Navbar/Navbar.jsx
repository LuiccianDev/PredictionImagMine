import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import styles from './Navbar.module.css';
import { useAuthContext } from '../../context/AuthContext.jsx';
import logo from '../../assets/mineria-en-la-nube.png'
import Menu from '../../../src/assets/menu.svg'
const Navbar = () => {
  const { user, logout, loading } = useAuthContext();
  const [isMenuOpen, setIsMenuOpen] = useState(false); // Estado para el menú móvil

  if (loading) return null; // 🔹 Esperar a que termine la carga

  return (
    <nav className={styles.navbar}>
      {/* Logo */}
      <Link to="/" className={styles.navbar__logo}>
        <img src={logo} alt="" />
      </Link>

      {/* Menú hamburguesa (solo en móviles) */}
      <button
        className={styles.navbar__toggle}
        onClick={() => setIsMenuOpen(!isMenuOpen)}
      >
        <img src={Menu} alt="" />
      </button>

      {/* Enlaces de navegación */}
      <div
        className={`${styles.navbar__links} ${isMenuOpen ? styles.open : ''}`}
      >
        {/* Enlaces comunes (siempre visibles) */}
        <Link to="/">Inicio</Link>

        {/* Enlaces para usuarios autenticados */}
        {user ? (
          <>
            {/* <Link to="/dashboard">Dashboard</Link> */}
            <Link to="/prediction">Predecir</Link>
            <Link to="/presentation">Presentación</Link>
            <Link to="/profile">Perfil</Link>
            <button onClick={logout} className={styles.navbar__logout}>
              Salir
            </button>
          </>
        ) : (
          // Enlaces para usuarios no autenticados
          <>
            <Link to="/about">Acerca de</Link>
            <Link to="/contact">Contacto</Link>
            <Link to="/login">Iniciar sesión</Link>
            <Link to="/signup">Registrarse</Link>
          </>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
/* import React from 'react';
import { Link } from 'react-router-dom';
import styles from './Navbar.module.css';
import { useAuthContext } from '../../context/AuthContext.jsx';

const Navbar = () => {
  const { user, logout, loading } = useAuthContext();

  if (loading) return null; // 🔹 Esperar a que termine la carga

  return (
    
    user && (
      <nav className={styles.navbar}>
        <Link to="/login/home">Inicio</Link>
        <Link to="/login/dashboard">Dashboard</Link>
        <Link to="/login/presentation">Presentación</Link>
        <Link to="/login/profile">Profle</Link>
        <button onClick={logout}>Salir</button>
      </nav>
    )

  );
};

export default Navbar; */

