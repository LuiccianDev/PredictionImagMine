import React from "react";
import styles from "../../styles/Dashboard.module.css";
import UploadIcon from '../../assets/upload.svg'
const FileUpload = ({ selectedFile, handleFileChange, handleUpload, error }) => {
  return (
    <section className={styles.section}>
      <h3>Subir Imagen</h3>
      <label htmlFor="file-upload" className={styles.uploadButton}>
        <img src={UploadIcon} alt="Subir" className={styles.uploadIcon} />
        {selectedFile ? selectedFile.name : "Seleccionar archivo"}
      </label>
      <input id="file-upload" type="file" onChange={handleFileChange} className={styles.inputFile} />
      <button onClick={handleUpload} className={styles.button}>Subir y Procesar</button>
      {error && <p className={styles.error}>{error}</p>}
    </section>
  );
};

export default FileUpload;