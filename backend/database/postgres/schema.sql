-- Habilitar la extensión para UUID si no está activa
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Tabla de Usuarios
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Ubicaciones
CREATE TABLE locations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    latitude DOUBLE PRECISION NOT NULL,
    longitude DOUBLE PRECISION NOT NULL,
    country VARCHAR(100) NOT NULL
);

-- Tabla de Dispositivos
CREATE TABLE devices (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    device_name VARCHAR(100) NOT NULL,
    manufacturer VARCHAR(100),
    type VARCHAR(50)
);

-- Tabla de Predicciones
CREATE TABLE predictions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,  
    image_name VARCHAR(255) NOT NULL,
    image_path VARCHAR(255) NOT NULL,
    predicted_mineral VARCHAR(100) NOT NULL,
    confidence DOUBLE PRECISION NOT NULL CHECK (confidence BETWEEN 0 AND 1),
    confidence_category VARCHAR(50) GENERATED ALWAYS AS (
        CASE 
            WHEN confidence >= 0.8 THEN 'Alta'
            WHEN confidence >= 0.5 THEN 'Media'
            ELSE 'Baja'
        END
    ) STORED,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source VARCHAR(100),
    processing_time DOUBLE PRECISION,
    metadata JSONB,
    model_version VARCHAR(50),
    feedback BOOLEAN DEFAULT FALSE,
    real_label VARCHAR(100),
    location_id UUID REFERENCES locations(id) ON DELETE SET NULL,
    device_id UUID REFERENCES devices(id) ON DELETE SET NULL
);

-- Tabla de Etiquetas / Validaciones de Predicciones
CREATE TABLE labels (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    prediction_id UUID NOT NULL REFERENCES predictions(id) ON DELETE CASCADE,
    real_label VARCHAR(100) NOT NULL,
    feedback BOOLEAN NOT NULL DEFAULT FALSE,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
