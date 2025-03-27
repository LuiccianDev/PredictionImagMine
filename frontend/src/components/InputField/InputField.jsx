import React from "react";
import styles from "../../styles/Login.module.css";

const InputField = ({ type, name, placeholder, value, onChange, required }) => {
  return (
    <input
      type={type}
      name={name}
      placeholder={placeholder}
      value={value}
      onChange={onChange}
      required={required}
      className={styles.input}
    />
  );
};

export default InputField;