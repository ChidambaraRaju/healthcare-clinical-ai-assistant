-- Database Schema for Healthcare Clinical AI Assistant
-- PostgreSQL 14+

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL DEFAULT 'provider',
    mfa_enabled BOOLEAN DEFAULT FALSE,
    mfa_secret VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    is_verified BOOLEAN DEFAULT FALSE,
    last_login_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Patients table
CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    mrn VARCHAR(50) UNIQUE NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(20),
    address TEXT,
    emergency_contact_name VARCHAR(200),
    emergency_contact_phone VARCHAR(20),
    allergies TEXT,
    medical_history TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Clinical documents table
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(id) ON DELETE CASCADE,
    provider_id INTEGER REFERENCES users(id),
    document_type VARCHAR(50) NOT NULL, -- progress_note, discharge_summary, consultation, etc.
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    ai_generated BOOLEAN DEFAULT FALSE,
    ai_model VARCHAR(100),
    confidence_score FLOAT,
    status VARCHAR(50) DEFAULT 'draft', -- draft, reviewed, final
    version INTEGER DEFAULT 1,
    parent_document_id INTEGER REFERENCES documents(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Medical codes table
CREATE TABLE medical_codes (
    id SERIAL PRIMARY KEY,
    code VARCHAR(20) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(20) NOT NULL, -- ICD-10, CPT, HCPCS
    full_code VARCHAR(20) UNIQUE,
    includes TEXT,
    excludes TEXT,
    notes TEXT
);

-- Document-code associations
CREATE TABLE document_codes (
    id SERIAL PRIMARY KEY,
    document_id INTEGER REFERENCES documents(id) ON DELETE CASCADE,
    code_id INTEGER REFERENCES medical_codes(id),
    suggested_by_ai BOOLEAN DEFAULT FALSE,
    confidence_score FLOAT,
    approved_by INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(document_id, code_id)
);

-- Encounters table
CREATE TABLE encounters (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(id) ON DELETE CASCADE,
    provider_id INTEGER REFERENCES users(id),
    encounter_type VARCHAR(50) NOT NULL, -- office_visit, emergency, inpatient, etc.
    encounter_date TIMESTAMP NOT NULL,
    chief_complaint TEXT,
    vitals JSONB,
    diagnosis TEXT[],
    treatment_plan TEXT,
    follow_up_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Audit log table (HIPAA compliance)
CREATE TABLE audit_logs (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    action VARCHAR(100) NOT NULL, -- view, create, update, delete
    resource_type VARCHAR(50) NOT NULL, -- patient, document, user, etc.
    resource_id INTEGER,
    ip_address INET,
    user_agent TEXT,
    details JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Refresh tokens table
CREATE TABLE refresh_tokens (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    token VARCHAR(500) UNIQUE NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX idx_patients_mrn ON patients(mrn);
CREATE INDEX idx_patients_name ON patients(last_name, first_name);
CREATE INDEX idx_documents_patient ON documents(patient_id);
CREATE INDEX idx_documents_provider ON documents(provider_id);
CREATE INDEX idx_documents_type ON documents(document_type);
CREATE INDEX idx_documents_date ON documents(created_at);
CREATE INDEX idx_encounters_patient ON encounters(patient_id);
CREATE INDEX idx_encounters_provider ON encounters(provider_id);
CREATE INDEX idx_encounters_date ON encounters(encounter_date);
CREATE INDEX idx_audit_logs_user ON audit_logs(user_id);
CREATE INDEX idx_audit_logs_resource ON audit_logs(resource_type, resource_id);
CREATE INDEX idx_audit_logs_date ON audit_logs(created_at);
CREATE INDEX idx_medical_codes_code ON medical_codes(code);
CREATE INDEX idx_medical_codes_category ON medical_codes(category);

-- Trigger for updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_patients_updated_at BEFORE UPDATE ON patients
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_documents_updated_at BEFORE UPDATE ON documents
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_encounters_updated_at BEFORE UPDATE ON encounters
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Row-level security policies (HIPAA compliance)
ALTER TABLE patients ENABLE ROW LEVEL SECURITY;
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
ALTER TABLE encounters ENABLE ROW LEVEL SECURITY;

-- Initial admin user (password should be changed immediately)
-- Password: 'admin123' (change this in production)
INSERT INTO users (email, username, password_hash, first_name, last_name, role, is_verified)
VALUES (
    'admin@clinicalai.com',
    'admin',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5NU7b5w5E5/6G',
    'System',
    'Administrator',
    'admin',
    TRUE
);

-- Grant necessary permissions (adjust based on your setup)
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO clinical_ai_user;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO clinical_ai_user;
