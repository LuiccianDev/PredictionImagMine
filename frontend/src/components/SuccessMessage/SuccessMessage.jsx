import React from "react";
import styles from "../../styles/dashboard.module.css";
import Refresh from '../../assets/refresh.svg'

const SuccessMessage = ({ resetState }) => {
  return (
    <div className={styles.successContainer}>
      <p className={styles.success}>Gracias por tu confirmación. Se ha actualizado la información.</p>
      <button onClick={resetState} className={styles.button}>
        <img src={Refresh} alt="Refrescar" />
      </button>
    </div>
  );
};

export default SuccessMessage;