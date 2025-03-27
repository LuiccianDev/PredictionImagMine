import React from 'react';
import styles from '../styles/Presentation.module.css';
import { Link } from 'react-router-dom';
import Navbar from "../components/Navbar/Navbar";
const Presentation = () => {
  return (<>
    <Navbar/>
    <div className={styles.presentationContainer}>
      
      <h1>Modelo de Predicción de Minerales</h1>
      <p>
        Bienvenido al sistema de predicción de minerales. Este modelo utiliza técnicas avanzadas de inteligencia artificial para analizar imágenes y determinar el tipo de mineral presente con alta precisión.
      </p>
      <div className={styles.features}>
        <h2>Características</h2>
        <ul>
          <li>Alta precisión en la detección</li>
          <li>Análisis en tiempo real</li>
          <li>Interfaz intuitiva y fácil de usar</li>
          <li>Actualización constante con nuevos datos</li>
        </ul>
      </div>
      <div className={styles.demoSection}>
        <h2>Demostración Interactiva</h2>
        <p>Prueba nuestro sistema con imágenes de ejemplo y descubre cómo funciona la predicción en tiempo real.</p>
        <button className={styles.demoButton}>Ver Demo</button>
      </div>
      <div className={styles.techInfo}>
        <h2>Tecnología</h2>
        <p>
          Utilizamos redes neuronales convolucionales (CNN) para analizar imágenes y algoritmos de aprendizaje profundo para mejorar continuamente la precisión del modelo.
        </p>
        <img src="/assets/images/model-diagram.png" alt="Diagrama del modelo" className={styles.diagram} />
      </div>
      <div className={styles.cta}>
        <p>¿Listo para empezar? Inicia Session y accede al dashboard y comienza a analizar tus imágenes.</p>
        <Link to="/login" className={styles.ctaButton}>
          Iniciar Sesión
        </Link>
      </div>
    </div>
    </>
  );
};

export default Presentation;
