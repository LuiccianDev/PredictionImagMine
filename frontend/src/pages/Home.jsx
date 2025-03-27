import React from 'react';
import { Link } from 'react-router-dom';
import Navbar from '../components/Navbar/Navbar';
import styles from '../styles/Home.module.css'; // Asegúrate de crear este archivo

const Home = () => {
  return (<>
    <Navbar />
    <main className={styles.homeContainer}>
      
      <section className={styles.hero}>
        <div className={styles.content}>
          <h1 className={styles.title}>Bienvenido a Mineral Predictor</h1>
          <p className={styles.subtitle}>
            Descubre y predice minerales con la precisión de nuestra inteligencia artificial.
          </p>
          <Link to="/dashboard" className={styles.ctaButton}>
            Comenzar a predecir Minerales
          </Link>
        </div>
      </section>
    </main>
    </>
  );
};

export default Home;

