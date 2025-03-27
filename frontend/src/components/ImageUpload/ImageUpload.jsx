import React from 'react';
import styles from './ImageUpload.module.css';

const ImageUpload = ({ onFileChange, onUpload }) => (
  <div className={styles.imageUpload}>
    <input type="file" onChange={onFileChange} />
    <button onClick={onUpload}>Subir Imagen</button>
  </div>
);

export default ImageUpload;
