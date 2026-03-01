# Healthcare Clinical AI Assistant

A production-ready AI-powered clinical documentation assistant designed to help healthcare professionals generate, analyze, and manage clinical documentation efficiently and securely.

## 🏥 Overview

This application uses advanced machine learning models to assist with:
- Clinical note generation from patient encounters
- Medical code suggestion (ICD-10, CPT)
- Document summarization and analysis
- HIPAA-compliant data handling
- Secure authentication and authorization

## 📋 Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Development](#development)
- [Testing](#testing)
- [Deployment](#deployment)
- [Security & HIPAA](#security--hipaa)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **AI-Powered Documentation**: Generate clinical notes using state-of-the-art ML models
- **Real-time Suggestions**: Get intelligent code and terminology suggestions
- **Secure Data Handling**: End-to-end encryption and HIPAA-compliant storage
- **Multi-tenant Architecture**: Support for multiple healthcare organizations
- **Audit Logging**: Comprehensive audit trails for compliance
- **Role-Based Access Control**: Granular permissions for different user types

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │   ML Service    │
│   (Next.js)     │◄──►│   (FastAPI)     │◄──►│   (PyTorch)     │
└────────┬────────┘    └────────┬────────┘    └─────────────────┘
         │                     │
         │                     │
         ▼                     ▼
┌─────────────────┐    ┌─────────────────┐
│   CloudFront    │    │   AWS Fargate   │
└─────────────────┘    └────────┬────────┘
                                │
                                ▼
                     ┌─────────────────┐
                     │  PostgreSQL     │
                     │  (Encrypted)    │
                     └─────────────────┘
```

## 🔧 Prerequisites

- **Node.js**: >= 18.x
- **Python**: >= 3.11
- **PostgreSQL**: >= 14
- **Docker**: >= 24.x
- **Docker Compose**: >= 2.x
- **AWS CLI**: >= 2.x (for deployment)

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/healthcare-clinical-ai-assistant.git
cd healthcare-clinical-ai-assistant
```

### 2. Environment Setup

```bash
# Copy environment template
cp .env.example .env

# Edit with your configuration
nano .env
```

### 3. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python -m alembic upgrade head

# Start development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### 5. ML Service Setup

```bash
cd ml

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download/pre-load models
python scripts/download_models.py

# Start inference server
python -m uvicorn inference.main:app --reload --port 8001
```

## ⚙️ Configuration

### Required Environment Variables

```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/clinical_ai
DATABASE_POOL_SIZE=20

# JWT Secret (generate with: openssl rand -hex 32)
JWT_SECRET_KEY=your-secret-key-here
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60

# ML Service
ML_SERVICE_URL=http://localhost:8001
MODEL_CACHE_DIR=/app/models

# AWS (for deployment)
AWS_REGION=us-east-1
AWS_ECR_REPOSITORY=clinical-ai
ECS_CLUSTER_NAME=clinical-ai-cluster
CLOUDFRONT_DISTRIBUTION_ID=your-distribution-id

# Security
ENCRYPTION_KEY=your-encryption-key
ALLOWED_ORIGINS=https://yourdomain.com
RATE_LIMIT_PER_MINUTE=100
```

## 🚀 Development

### Backend Development

```bash
cd backend

# Format code
black app/
flake8 app/
mypy app/

# Run tests
pytest -v

# With coverage
pytest --cov=app --cov-report=html
```

### Frontend Development

```bash
cd frontend

# Lint
npm run lint

# Format
npm run format

# Run tests
npm run test
```

### ML Development

```bash
cd ml

# Run tests
pytest -v

# Train model (example)
python scripts/train.py --config configs/default.yaml
```

## 🧪 Testing

### Run All Tests

```bash
# Backend
cd backend && pytest -v

# Frontend
cd frontend && npm run test

# ML Service
cd ml && pytest -v
```

### Integration Tests

```bash
docker-compose -f docker-compose.test.yml up --abort-on-container-exit
```

## 🌐 Deployment

### Docker Build

```bash
# Build all services
docker-compose build

# Or build individually
docker build -t clinical-ai-backend ./backend
docker build -t clinical-ai-frontend ./frontend
docker build -t clinical-ai-ml ./ml
```

### AWS Deployment (via CI/CD)

The GitHub Actions workflow automatically:
1. Runs tests and security scans
2. Builds Docker images
3. Pushes to GitHub Container Registry
4. Deploys backend to AWS Fargate
5. Deploys frontend to CloudFront

Manual deployment commands:

```bash
# Deploy to Fargate
aws ecs update-service --cluster clinical-ai-cluster --service backend --force-new-deployment

# Invalidate CloudFront cache
aws cloudfront create-invalidation --distribution-id YOUR_ID --paths "/*"
```

## 🔒 Security & HIPAA

### HIPAA Compliance Features

- **Encryption**: All data encrypted at rest (AES-256) and in transit (TLS 1.3)
- **Audit Logging**: Complete audit trail of all data access and modifications
- **Access Controls**: Role-based access with principle of least privilege
- **Data Retention**: Configurable retention policies
- **Business Associate Agreement**: Available upon request

### Security Best Practices

- Regular security audits and penetration testing
- Dependency scanning (Snyk, Dependabot)
- Secrets management (AWS Secrets Manager)
- Automated vulnerability scanning in CI/CD
- Security headers and CSP policies

See [SECURITY.md](SECURITY.md) for detailed security guidelines.

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Workflow

- All PRs must pass CI checks
- At least one approval required
- Follow commit message format: `type(scope): description`
- Include tests for new features
- Update documentation as needed

## 📚 Documentation

- [API Documentation](docs/API.md)
- [Architecture Overview](docs/ARCHITECTURE.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [ML Model Documentation](docs/ML_MODELS.md)
- [HIPAA Compliance Guide](docs/HIPAA.md)

## 🐛 Troubleshooting

### Common Issues

**Backend won't start**
```bash
# Check database connection
psql $DATABASE_URL

# Verify migrations
python -m alembic current
```

**Frontend build fails**
```bash
# Clear cache
rm -rf .next node_modules
npm install
```

**ML service errors**
```bash
# Check model downloads
ls -la $MODEL_CACHE_DIR

# Verify GPU availability (if applicable)
nvidia-smi
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- **Documentation**: [docs/](docs/)
- **Issues**: [GitHub Issues](https://github.com/your-org/healthcare-clinical-ai-assistant/issues)
- **Security**: security@yourdomain.com

## 🙏 Acknowledgments

- Medical advisors and healthcare professionals who provided domain expertise
- Open-source community for excellent ML frameworks
- Healthcare AI research community

---

**⚠️ Disclaimer**: This tool is intended to assist, not replace, professional medical judgment. Always verify AI-generated content before clinical use.
