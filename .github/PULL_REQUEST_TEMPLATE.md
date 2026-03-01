---
name: Pull Request
about: Submit changes for review
title: '[PREFIX] Short description of changes'
labels: ''
assignees: ''
---

## 📋 Pull Request Checklist

Please ensure your PR meets these requirements:

- [ ] Code follows project style guidelines (Black for Python, Prettier for JS)
- [ ] All tests pass locally (`pytest -v` for backend, `npm test` for frontend)
- [ ] New features include tests
- [ ] Documentation is updated (if applicable)
- [ ] Commit messages follow conventional format
- [ ] No sensitive data or credentials committed
- [ ] HIPAA/security considerations addressed

## 📝 Description

<!-- Briefly describe what this PR does and why it's needed -->

## 🎯 Type of Change

<!-- Mark the relevant option with an "x" -->

- [ ] 🐛 Bug fix (non-breaking change which fixes an issue)
- [ ] ✨ New feature (non-breaking change which adds functionality)
- [ ] 🚀 Performance improvement
- [ ] ♻️ Code refactoring
- [ ] 📚 Documentation update
- [ ] 🔒 Security fix
- [ ] 🧪 Test addition/update
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] ⚠️ Deprecated feature removal

## 🔗 Related Issues

<!-- Link to related issues -->
<!-- Fixes #123 -->
<!-- Closes #456 -->

## 🧪 Testing

### Manual Testing Steps

1.
2.
3.

### Automated Tests

```bash
# Backend tests
cd backend && pytest -v

# Frontend tests
cd frontend && npm test

# ML service tests
cd ml && pytest -v
```

### Test Coverage

<!-- Provide coverage metrics if applicable -->
- Backend: __%
- Frontend: __%
- ML Service: __%

## 📸 Screenshots (if applicable)

<!-- Add screenshots for UI changes -->

## 🏗️ Architecture Changes

<!-- Describe any architectural changes or database migrations -->

**Database Migrations:**
<!-- List migration files -->

**API Changes:**
<!-- List endpoint changes -->

**Infrastructure Changes:**
<!-- List any infrastructure modifications -->

## 🔐 Security & HIPAA Considerations

<!-- Address any security or HIPAA-related concerns -->

- [ ] No PHI in logs or error messages
- [ ] Proper access controls maintained
- [ ] Audit logging for sensitive operations
- [ ] Data encryption (at rest and in transit)
- [ ] Dependencies reviewed for vulnerabilities

## 📦 Dependencies

<!-- List any new or updated dependencies -->

**Added:**
- package@version

**Updated:**
- package@version: old.version → new.version

**Removed:**
- package@version

## 📚 Documentation Updates

<!-- List documentation files that need updating -->

- [ ] README.md
- [ ] API.md
- [ ] ARCHITECTURE.md
- [ ] DEPLOYMENT.md
- [ ] HIPAA.md
- [ ] Other: _____

## 🚀 Deployment Notes

<!-- Special instructions for deployment -->

### Pre-deployment
- [ ] Database migrations run
- [ ] Environment variables configured
- [ ] Third-party services updated

### Post-deployment
- [ ] Cache invalidation needed
- [ ] CDN update required
- [ ] Manual verification steps

## 🧹 Breaking Changes

<!-- Describe any breaking changes and migration paths -->

## 💬 Additional Notes

<!-- Any additional context or comments -->

## ✅ Reviewer Checklist

- [ ] Code is well-documented and follows style guidelines
- [ ] Tests are sufficient and passing
- [ ] Security and HIPAA requirements met
- [ ] No sensitive information exposed
- [ ] Performance impact assessed
- [ ] Backward compatibility considered (if applicable)
- [ ] Documentation updated

---

**Note:** This PR will not be merged until:
1. All CI checks pass
2. At least one approval is received
3. All requested changes are addressed
