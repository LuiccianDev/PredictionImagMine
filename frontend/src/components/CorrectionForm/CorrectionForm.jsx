import React from "react";
import styles from "../../styles/dashboard.module.css";

const CorrectionForm = ({ confirmation, setConfirmation, correction, setCorrection, MINERALS_LIST, handleCorrectionSubmit }) => {
  return (
    <form onSubmit={handleCorrectionSubmit}>
      <label>
        ¿Es correcto el mineral predicho?
        <select value={confirmation} onChange={(e) => setConfirmation(e.target.value)} required className={styles.select}>
          <option value="" disabled>Selecciona</option>
          <option value="si">Sí</option>
          <option value="no">No</option>
        </select>
      </label>
      {confirmation === "no" && (
        <select
          value={correction}
          onChange={(e) => setCorrection(e.target.value)}
          required
          className={styles.inputText}
        >
          <option value="" disabled>Selecciona un mineral</option>
          {MINERALS_LIST.map((mineral, index) => (
            <option key={index} value={mineral}>{mineral}</option>
          ))}
        </select>
      )}
      <button type="submit" className={styles.button}>Enviar Confirmación/Corrección</button>
    </form>
  );
};

export default CorrectionForm;