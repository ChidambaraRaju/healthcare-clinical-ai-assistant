# Contributing to Healthcare Clinical AI Assistant

Thank you for your interest in contributing to the Healthcare Clinical AI Assistant! We welcome contributions from developers, healthcare professionals, researchers, and anyone passionate about improving healthcare through technology.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Reporting Issues](#reporting-issues)
- [Documentation](#documentation)

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](../CODE_OF_CONDUCT.md).

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL 14+
- Docker and Docker Compose (optional)

### Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/healthcare-clinical-ai-assistant.git
   cd healthcare-clinical-ai-assistant
   ```

3. Set up your development environment:
   ```bash
   # Backend
   cd backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

   # Frontend
   cd ../frontend
   npm install

   # ML Service
   cd ../ml
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## Development Workflow

### Branching Strategy

- `main`: Production-ready code
- `develop`: Development branch
- `feature/*`: New features
- `bugfix/*`: Bug fixes
- `hotfix/*`: Critical production fixes

### Creating a Feature Branch

```bash
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name
```

### Making Changes

1. Write code following our coding standards
2. Add tests for new functionality
3. Ensure all tests pass
4. Update documentation as needed

## Coding Standards

### Backend (Python)

- Follow PEP 8 style guide
- Use Black for formatting
- Use type hints where appropriate
- Write docstrings for all functions and classes
- Keep functions focused and small

```bash
# Format code
black app/

# Check style
flake8 app/

# Type checking
mypy app/
```

### Frontend (TypeScript/React)

- Follow ESLint and Prettier configurations
- Use functional components with hooks
- Write unit tests for components
- Use TypeScript for type safety

```bash
# Lint
npm run lint

# Format
npm run format

# Type check
npm run type-check
```

### Commit Messages

Follow conventional commits format:

```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Test additions/changes
- `chore`: Maintenance tasks

Examples:
- `feat(auth): add MFA support`
- `fix(api): resolve patient search timeout issue`
- `docs(readme): update installation instructions`

## Testing

### Backend Tests

```bash
cd backend
pytest -v
pytest --cov=app --cov-report=html
```

### Frontend Tests

```bash
cd frontend
npm run test
npm run test:coverage
```

### Integration Tests

```bash
docker-compose -f docker-compose.test.yml up
```

### Test Coverage Requirements

- New features must include tests
- Aim for >80% code coverage
- All PRs must pass CI tests

## Submitting Changes

### Pull Request Process

1. Update your branch with latest changes:
   ```bash
   git fetch origin
   git rebase origin/develop
   ```

2. Push your changes:
   ```bash
   git push origin feature/your-feature-name
   ```

3. Create a Pull Request on GitHub
4. Fill out the PR template completely
5. Wait for CI checks to pass
6. Address review feedback
7. Get at least one approval
8. Merge when approved

### PR Review Checklist

- [ ] Code follows project style guidelines
- [ ] Tests included and passing
- [ ] Documentation updated
- [ ] No sensitive data committed
- [ ] HIPAA/security considerations addressed
- [ ] No breaking changes (or documented)

## Reporting Issues

### Bug Reports

Use the GitHub issue tracker with the Bug Report template.

### Feature Requests

Use the Feature Request template for new feature ideas.

### Security Issues

⚠️ **Do not report security issues publicly!**

Email security@yourdomain.com with security vulnerabilities.

## Documentation

### API Documentation

Add/update API docs using FastAPI's automatic documentation:
- Add request/response models
- Include examples
- Document error responses

### User Documentation

Update user-facing docs in the `docs/` directory:
- Getting Started
- Feature guides
- Troubleshooting

### Developer Documentation

Keep developer docs current:
- Architecture diagrams
- Development setup
- Testing guidelines

## Development Guidelines

### Healthcare Domain Considerations

- **HIPAA Compliance**: Never commit PHI or real patient data
- **Medical Accuracy**: Consult healthcare professionals for medical features
- **Clinical Safety**: Prioritize patient safety over speed

### Security Guidelines

- Use environment variables for secrets
- Never hardcode credentials
- Follow OWASP security guidelines
- Regular dependency updates
- Security-focused code reviews

### Performance Guidelines

- Profile before optimizing
- Use database indexes appropriately
- Implement caching where beneficial
- Optimize ML model inference
- Monitor resource usage

## Getting Help

- **Documentation**: Check the [docs/](../docs) directory
- **Issues**: Browse [GitHub Issues](https://github.com/your-org/healthcare-clinical-ai-assistant/issues)
- **Discussions**: Join our [GitHub Discussions](https://github.com/your-org/healthcare-clinical-ai-assistant/discussions)
- **Email**: dev@yourdomain.com

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project website (optional)

Thank you for contributing! 🙏
