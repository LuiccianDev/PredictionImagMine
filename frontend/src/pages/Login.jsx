import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuthContext } from "../context/AuthContext";
import InputField from "../components/InputField/InputField";
import Checkbox from "../components//Checkbox/Checkbox";
import Button from "../components//Button/Button";
import ErrorMessage from "../components//ErrorMessage/ErrorMessage";
import styles from "../styles/Login.module.css";

const LoginForm = () => {
  const [credentials, setCredentials] = useState({ username: "", password: "" });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [rememberMe, setRememberMe] = useState(false);
  const { login } = useAuthContext();
  const navigate = useNavigate();

  const handleChange = (e) => {
    setCredentials({
      ...credentials,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      const result = await login(credentials);
      if (result) {
        if (rememberMe) {
          localStorage.setItem("authToken", result.token);
        }
        navigate("/home");
      } else {
        setError("Credenciales incorrectas.");
      }
    } catch (err) {
      setError("Error al iniciar sesión. Inténtalo de nuevo.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.loginContainer}>
      <form className={styles.loginForm} onSubmit={handleSubmit}>
        <h2 className={styles.titulo}>Iniciar Sesión</h2>
        <ErrorMessage message={error} />
        <InputField
          type="text"
          name="username"
          placeholder="Usuario"
          value={credentials.username}
          onChange={handleChange}
          required
        />
        <InputField
          type="password"
          name="password"
          placeholder="Contraseña"
          value={credentials.password}
          onChange={handleChange}
          required
        />
        <div className={styles.options}>
          <Checkbox
            checked={rememberMe}
            onChange={(e) => setRememberMe(e.target.checked)}
            label="Recordarme"
          />
          <Link to="/forgot-password" className={styles.forgotPassword}>
            Olvidé mi contraseña
          </Link>
        </div>
        <Button type="submit" disabled={loading}>
          {loading ? "Cargando..." : "Entrar"}
        </Button>
        <p className={styles.registerText}>
          ¿No tienes cuenta? <Link to="/login/signup">Regístrate aquí</Link>
        </p>
      </form>
    </div>
  );
};

export default LoginForm;
