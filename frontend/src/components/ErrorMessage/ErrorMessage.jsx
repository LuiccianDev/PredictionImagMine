import React from "react";
import styles from "../../styles/Login.module.css";

const ErrorMessage = ({ message }) => {
  return message ? <p className={styles.error}>{message}</p> : null;
};

export default ErrorMessage;