import React from "react";
import styles from "../../styles/Login.module.css";

const Button = ({ type, disabled, children }) => {
  return (
    <button type={type} className={styles.button} disabled={disabled}>
      {children}
    </button>
  );
};

export default Button;