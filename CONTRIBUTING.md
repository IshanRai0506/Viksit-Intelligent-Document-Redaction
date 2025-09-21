# Contributing to Viksit - Intelligent Document Redaction

Thank you for your interest in contributing to Viksit! This document provides guidelines for contributing to the project.

## Table of Contents

- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Code Style](#code-style)
- [Testing](#testing)
- [Documentation](#documentation)
- [Submitting Changes](#submitting-changes)
- [Issue Reporting](#issue-reporting)

## Getting Started

1. **Fork the repository** and clone your fork
2. **Set up development environment** as described in README.md
3. **Create a new branch** for your feature or bugfix
4. **Make your changes** following our guidelines
5. **Test your changes** thoroughly
6. **Submit a pull request**

## Development Workflow

### Setting Up Development Environment

```bash
# Clone your fork
git clone https://github.com/yourusername/Viksit-Intelligent-Document-Redaction.git
cd Viksit-Intelligent-Document-Redaction

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run initial tests
pytest tests/
```

### Branch Naming

Use descriptive branch names:
- `feature/entity-extraction-improvement`
- `bugfix/pdf-parsing-error`
- `docs/api-documentation-update`

## Code Style

### Python Code Style

We follow PEP 8 with some modifications:

- Line length: 88 characters (Black default)
- Use type hints for all functions
- Use docstrings for all public functions and classes

### Formatting Tools

```bash
# Format code with Black
black src/ tests/

# Check with flake8
flake8 src/ tests/

# Sort imports with isort
isort src/ tests/

# Type checking with mypy
mypy src/
```

### Example Code Style

```python
from typing import List, Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)


class DocumentRedactor:
    """Intelligent document redaction system.
    
    This class provides methods for detecting and redacting
    sensitive information from various document formats.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None) -> None:
        """Initialize the document redactor.
        
        Args:
            config: Optional configuration dictionary
        """
        self.config = config or {}
        self._initialize_models()
    
    def redact_document(
        self, 
        input_path: str, 
        output_path: str,
        entity_types: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Redact sensitive information from a document.
        
        Args:
            input_path: Path to input document
            output_path: Path for redacted output
            entity_types: List of entity types to redact
            
        Returns:
            Dictionary containing redaction results and statistics
            
        Raises:
            FileNotFoundError: If input file doesn't exist
            ValueError: If unsupported file format
        """
        # Implementation here
        pass
```

## Testing

### Test Structure

- `tests/unit/` - Unit tests for individual components
- `tests/integration/` - Integration tests for component interactions
- `tests/performance/` - Performance and benchmark tests
- `tests/fixtures/` - Test data and fixtures

### Writing Tests

```python
import pytest
from viksit.redactor import DocumentRedactor


class TestDocumentRedactor:
    """Test suite for DocumentRedactor class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.redactor = DocumentRedactor()
    
    def test_redact_document_basic(self):
        """Test basic document redaction functionality."""
        # Arrange
        input_path = "tests/fixtures/sample_document.pdf"
        output_path = "/tmp/test_output.pdf"
        
        # Act
        result = self.redactor.redact_document(input_path, output_path)
        
        # Assert
        assert result["status"] == "success"
        assert result["entities_found"] > 0
    
    @pytest.mark.parametrize("file_format", ["pdf", "docx", "txt"])
    def test_supported_formats(self, file_format):
        """Test redaction works with supported file formats."""
        # Test implementation
        pass
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test categories
pytest tests/unit/
pytest tests/integration/

# Run performance tests
pytest tests/performance/ -m slow
```

## Documentation

### Code Documentation

- Use clear, descriptive docstrings
- Include type hints for all parameters and return values
- Provide examples in docstrings when helpful
- Document complex algorithms and business logic

### API Documentation

When adding new API endpoints:

1. Update OpenAPI/Swagger specifications
2. Add examples to documentation
3. Update API section in README.md

### User Documentation

- Update README.md for user-facing changes
- Add examples for new features
- Update configuration documentation
- Create tutorials for complex workflows

## Submitting Changes

### Pull Request Process

1. **Create descriptive PR title**:
   - ✅ "Add support for DOCX file redaction"
   - ❌ "Fix bug"

2. **Write clear PR description**:
   - What changes were made
   - Why the changes were necessary
   - How to test the changes
   - Any breaking changes

3. **Ensure all checks pass**:
   - All tests pass
   - Code coverage maintained
   - Linting passes
   - Documentation updated

4. **Request reviews** from maintainers

### PR Template

```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added for new functionality
```

## Issue Reporting

### Bug Reports

Include:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version, etc.)
- Sample documents (if applicable and non-sensitive)

### Feature Requests

Include:
- Clear description of the feature
- Use case and motivation
- Proposed implementation approach
- Acceptance criteria

### Security Issues

For security vulnerabilities:
- Do not create public issues
- Email security@viksit.dev
- Include detailed description and reproduction steps
- We will respond within 48 hours

## Code Review Guidelines

### For Authors

- Keep PRs focused and reasonably sized
- Write clear commit messages
- Respond to feedback constructively
- Test thoroughly before submitting

### For Reviewers

- Be constructive and specific in feedback
- Focus on code quality, security, and maintainability
- Ask questions if something is unclear
- Approve when satisfied with changes

## Release Process

### Version Numbering

We follow [Semantic Versioning](https://semver.org/):
- MAJOR version for incompatible API changes
- MINOR version for backwards-compatible functionality
- PATCH version for backwards-compatible bug fixes

### Release Checklist

- [ ] Version number updated
- [ ] CHANGELOG.md updated
- [ ] Documentation updated
- [ ] All tests pass
- [ ] Performance regression tests pass
- [ ] Security review completed

## Getting Help

- 💬 Join our [Discord community](https://discord.gg/viksit)
- 📧 Email: dev@viksit.dev
- 📖 Read the [documentation](https://docs.viksit.dev)
- 🐛 Check [existing issues](https://github.com/IshanRai0506/Viksit-Intelligent-Document-Redaction/issues)

Thank you for contributing to Viksit! 🚀