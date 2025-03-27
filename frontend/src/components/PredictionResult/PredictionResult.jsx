import React from "react";
import styles from "../../styles/dashboard.module.css";

const PredictionResult = ({ selectedFile, predictionResult }) => {
  return (
    <section className={styles.section}>
      <h3>Resultado de la Predicción</h3>
      {selectedFile && <img src={URL.createObjectURL(selectedFile)} alt="Imagen subida" className={styles.imagePreview} />}
      <div>
        <p><strong>Mineral Predicho:</strong> {predictionResult.prediction}</p>
        <p><strong>Confianza:</strong> {predictionResult.confidence}%</p>
      </div>
    </section>
  );
};

export default PredictionResult;