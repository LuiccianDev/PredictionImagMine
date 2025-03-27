import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';


const PredictionDetail = () => {
  const { id } = useParams();
  const [prediction, setPrediction] = useState(null);
  const [correction, setCorrection] = useState('');
  const [feedbackMessage, setFeedbackMessage] = useState('');

  useEffect(() => {
    const fetchPrediction = async () => {
      try {
        const response = await axios.get(
          (import.meta.env.VITE_API_URL || 'http://localhost:3000/api') + `/predict/${id}`
        );
        setPrediction(response.data);
      } catch (error) {
        console.error('Error al cargar el detalle de la predicción:', error);
      }
    };
    fetchPrediction();
  }, [id]);

  const handleCorrectionSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post(
        (import.meta.env.VITE_API_URL || 'http://localhost:3000/api') + '/predict/confirm',
        {
          predictionId: id,
          correctedName: correction,
        }
      );
      setFeedbackMessage('Predicción corregida exitosamente.');
    } catch (error) {
      console.error('Error al enviar la corrección:', error);
      setFeedbackMessage('Error al enviar la corrección.');
    }
  };

  return (
    <div className={styles.detailContainer}>
      {prediction ? (
        <>
          <h1>Detalle de la Predicción</h1>
          <img
            src={prediction.imageUrl}  // Asumiendo que la API devuelve la URL de la imagen
            alt="Imagen de predicción"
            className={styles.predictionImage}
          />
          <p><strong>Mineral Predicho:</strong> {prediction.mineral}</p>
          <p><strong>Confianza:</strong> {prediction.confidence}%</p>
          <form onSubmit={handleCorrectionSubmit} className={styles.correctionForm}>
            <label>
              ¿Deseas corregir el nombre del mineral?
              <input
                type="text"
                value={correction}
                onChange={(e) => setCorrection(e.target.value)}
                placeholder="Ingresa el nombre correcto"
              />
            </label>
            <button type="submit">Enviar Corrección</button>
          </form>
          {feedbackMessage && <p className={styles.feedback}>{feedbackMessage}</p>}
        </>
      ) : (
        <p>Cargando detalles...</p>
      )}
    </div>
  );
};

export default PredictionDetail;
