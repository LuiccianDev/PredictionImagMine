# PyPredictImagenMineral

## Descripción del Proyecto

Este proyecto es una aplicación completa para la identificación de minerales mediante un modelo de clasificación entrenado. Incluye un backend desarrollado en Flask, un frontend en React, y un módulo para el entrenamiento del modelo.

---

## Estructura del Proyecto

- **Backend**: API RESTful con Flask para manejar autenticación, predicciones y lógica de negocio.
- **Frontend**: Interfaz de usuario desarrollada con React y Vite.
- **Model Train**: Código para entrenar y evaluar el modelo de clasificación de minerales.
- **Datasets**: Conjuntos de datos para entrenamiento, validación y prueba.
- **Resultados**: Métricas y gráficos generados durante el entrenamiento del modelo.

---

## Configuración del Proyecto

### Requisitos Previos

1. **Python**: Versión 3.8 o superior.
2. **Node.js**: Versión 16 o superior.
3. **Base de Datos**: MySQL, PostgreSQL o SQLite.
4. **Docker** (opcional): Para contenedorización.

### Variables de Entorno

Crea un archivo `.env` en las carpetas `backend` y `frontend` con las siguientes configuraciones:

#### Backend (`backend/.env`)
```
FLASK_ENV=development
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///database.db
MODEL_PATH=models/mineral_classifier_v2.h5
```

#### Frontend (`frontend/.env`)
```
VITE_API_URL=http://localhost:5000/api
```

---

## Instalación

### Backend

1. Navega a la carpeta `backend`:
   ```bash
   cd backend
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Inicializa la base de datos:
   ```bash
   python init_db.py
   ```

4. Ejecuta el backend:
   ```bash
   python -m backend
   ```

### Frontend

1. Navega a la carpeta `frontend`:
   ```bash
   cd frontend
   ```

2. Instala las dependencias:
   ```bash
   npm install
   ```

3. Ejecuta el servidor de desarrollo:
   ```bash
   npm run dev
   ```

### Entrenamiento del Modelo

1. Navega a la carpeta `model_train`:
   ```bash
   cd model_train
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Ejecuta el script de entrenamiento:
   ```bash
   python -m model_train --run
   ```

---

## Uso del Proyecto

1. Accede al frontend en tu navegador en `http://localhost:3000`.
2. Regístrate o inicia sesión.
3. Sube una imagen de un mineral para obtener una predicción.
4. Consulta los resultados en el panel de usuario.

---

## Funcionalidades Principales

- **Autenticación**: Registro e inicio de sesión con validación de correos Gmail.
- **Predicción**: Clasificación de imágenes de minerales.
- **Entrenamiento**: Código para entrenar y evaluar modelos personalizados.
- **Panel de Usuario**: Visualización de resultados y métricas.

---

## Despliegue

### Usando Docker

1. Construye y ejecuta los contenedores:
   ```bash
   docker-compose up --build
   ```

2. Accede al frontend en `http://localhost:3000` y al backend en `http://localhost:5000`.

---

## Contribuciones

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y haz un commit:
   ```bash
   git commit -m "Añadida nueva funcionalidad"
   ```
4. Envía tus cambios:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
5. Abre un Pull Request.

---

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.