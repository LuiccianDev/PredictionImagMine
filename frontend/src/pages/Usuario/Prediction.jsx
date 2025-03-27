import React, { useState } from "react";
import Navbar from "../../components/Navbar/Navbar";
import axios from "axios";
import styles from "../../styles/dashboard.module.css";
import { useAuthContext } from "../../context/AuthContext";
import FileUpload from "../../components/FileUpload/FileUpload";
import PredictionResult from "../../components/PredictionResult/PredictionResult";
import CorrectionForm from "../../components/CorrectionForm/CorrectionForm";
import SuccessMessage from "../../components/SuccessMessage/SuccessMessage";
import {API_URL} from "../../config/api";

const Predicción = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [predictionResult, setPredictionResult] = useState(null);
  const [confirmation, setConfirmation] = useState("");
  const [correction, setCorrection] = useState("");
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState(null);

  const { user } = useAuthContext();
  const user_id = user?.id;

  /* const API_URL = import.meta.env.VITE_API_URL || "http://localhost:5000/api"; */

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
    setPredictionResult(null);
    setError(null);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setError("Por favor, selecciona un archivo.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);
    formData.append("user_id", user_id);
    try {
      const response = await axios.post(`${API_URL}/predictions/predict`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      setPredictionResult(response.data);
    } catch (error) {
      setError("Error al subir la imagen.");
      console.error("Error en la predicción:", error);
    }
  };

  const handleCorrectionSubmit = async (e) => {
    e.preventDefault();

    if (!predictionResult) return;

    try {
      await axios.post(`${API_URL}/predictions/correct`, {
        prediction_id: predictionResult.id,
        confirmation,
        correctMineral: confirmation === "no" ? correction : predictionResult.prediction,
        user_id: user_id,
      });

      setSubmitted(true);
      alert("Información enviada. ¡Gracias!");
    } catch (error) {
      setError("Error al enviar la corrección.");
      console.error("Error en la corrección:", error);
    }
  };

  const MINERALS_LIST = ["biotite", "bornite", "quartz", "chrysocolla", "pyrite", "malachite", "muscovite"];

  const resetState = () => {
    setSelectedFile(null);
    setPredictionResult(null);
    setConfirmation("");
    setCorrection("");
    setSubmitted(false);
    setError(null);
  };

  return (
    <>
      <Navbar />
      <div className={styles.dashboardContainer}>
        <h2 className={styles.title}>Dashboard</h2>

        <FileUpload
          selectedFile={selectedFile}
          handleFileChange={handleFileChange}
          handleUpload={handleUpload}
          error={error}
        />

        {predictionResult && (
          <>
            <PredictionResult selectedFile={selectedFile} predictionResult={predictionResult} />
            <CorrectionForm
              confirmation={confirmation}
              setConfirmation={setConfirmation}
              correction={correction}
              setCorrection={setCorrection}
              MINERALS_LIST={MINERALS_LIST}
              handleCorrectionSubmit={handleCorrectionSubmit}
            />
          </>
        )}

        {submitted && <SuccessMessage resetState={resetState} />}
      </div>
    </>
  );
};

export default Predicción;
