# Viksit - Intelligent Document Redaction

## Overview

Viksit is an intelligent document redaction system that automatically identifies and redacts sensitive information from documents using advanced machine learning and natural language processing techniques. The system can detect and redact various types of sensitive data including Personal Identifiable Information (PII), financial data, medical information, and other confidential content.

## Features

- **Automatic PII Detection**: Identifies names, addresses, phone numbers, email addresses, and social security numbers
- **Financial Data Redaction**: Detects credit card numbers, bank account details, and financial identifiers
- **Medical Information Protection**: Identifies and redacts medical record numbers, patient IDs, and health information
- **Custom Entity Recognition**: Supports custom patterns and entities for organization-specific sensitive data
- **Multiple File Formats**: Supports PDF, DOC, DOCX, TXT, and image files
- **Batch Processing**: Process multiple documents simultaneously
- **Audit Trail**: Maintains logs of all redaction activities
- **Preview Mode**: Review redactions before applying them permanently

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/IshanRai0506/Viksit-Intelligent-Document-Redaction.git
   cd Viksit-Intelligent-Document-Redaction
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download required models**:
   ```bash
   python setup.py download_models
   ```

## Usage

### Command Line Interface

**Basic redaction**:
```bash
python redact.py --input document.pdf --output redacted_document.pdf
```

**Batch processing**:
```bash
python redact.py --input-dir ./documents --output-dir ./redacted --batch
```

**Custom entity types**:
```bash
python redact.py --input document.pdf --entities person,organization,location --output redacted.pdf
```

**Preview mode**:
```bash
python redact.py --input document.pdf --preview --output preview.pdf
```

### Python API

```python
from viksit import DocumentRedactor

# Initialize redactor
redactor = DocumentRedactor()

# Redact a single document
result = redactor.redact_document(
    input_path="document.pdf",
    output_path="redacted_document.pdf",
    entity_types=["person", "organization", "phone", "email"]
)

# Batch redaction
results = redactor.batch_redact(
    input_directory="./documents",
    output_directory="./redacted"
)
```

### Web Interface

1. **Start the web server**:
   ```bash
   python app.py
   ```

2. **Open browser** and navigate to `http://localhost:5000`

3. **Upload documents** and configure redaction settings

4. **Download redacted documents**

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Model settings
MODEL_PATH=./models
CONFIDENCE_THRESHOLD=0.85

# Database settings (optional)
DATABASE_URL=sqlite:///viksit.db

# Logging
LOG_LEVEL=INFO
LOG_FILE=viksit.log

# API settings
API_HOST=0.0.0.0
API_PORT=5000
```

### Custom Configuration

Create a `config.yaml` file for advanced settings:

```yaml
redaction:
  entity_types:
    - person
    - organization
    - location
    - phone
    - email
    - ssn
    - credit_card
  
  confidence_threshold: 0.85
  
  custom_patterns:
    employee_id: "EMP-\\d{6}"
    project_code: "PRJ-[A-Z]{3}-\\d{4}"

output:
  format: "pdf"
  quality: "high"
  watermark: true
  
logging:
  level: "INFO"
  file: "viksit.log"
  max_size: "10MB"
```

## Development Setup

### For Contributors

1. **Fork the repository** on GitHub

2. **Clone your fork**:
   ```bash
   git clone https://github.com/yourusername/Viksit-Intelligent-Document-Redaction.git
   cd Viksit-Intelligent-Document-Redaction
   ```

3. **Install development dependencies**:
   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Install pre-commit hooks**:
   ```bash
   pre-commit install
   ```

5. **Run tests**:
   ```bash
   pytest tests/
   ```

6. **Code formatting**:
   ```bash
   black src/
   flake8 src/
   ```

### Project Structure

```
Viksit-Intelligent-Document-Redaction/
├── src/
│   ├── viksit/
│   │   ├── __init__.py
│   │   ├── redactor.py
│   │   ├── models/
│   │   ├── utils/
│   │   └── api/
│   └── web/
├── tests/
├── docs/
├── models/
├── requirements.txt
├── requirements-dev.txt
├── setup.py
├── config.yaml
└── README.md
```

## API Documentation

### REST API Endpoints

- `POST /api/redact` - Redact a single document
- `POST /api/batch-redact` - Batch redaction
- `GET /api/status/{job_id}` - Check redaction job status
- `GET /api/download/{job_id}` - Download redacted document

### Example API Usage

```bash
# Single document redaction
curl -X POST \
  http://localhost:5000/api/redact \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@document.pdf' \
  -F 'entities=["person","organization"]'

# Check status
curl http://localhost:5000/api/status/job_123456

# Download result
curl http://localhost:5000/api/download/job_123456 -o redacted_document.pdf
```

## Docker Deployment

### Using Docker

1. **Build the image**:
   ```bash
   docker build -t viksit-redaction .
   ```

2. **Run the container**:
   ```bash
   docker run -p 5000:5000 -v ./documents:/app/documents viksit-redaction
   ```

### Using Docker Compose

```bash
docker-compose up -d
```

## Testing

### Run all tests
```bash
pytest tests/
```

### Run specific test categories
```bash
# Unit tests
pytest tests/unit/

# Integration tests
pytest tests/integration/

# Performance tests
pytest tests/performance/
```

### Test coverage
```bash
pytest --cov=src tests/
```

## Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'spacy'`
**Solution**: Install spaCy models:
```bash
python -m spacy download en_core_web_sm
```

**Issue**: `CUDA out of memory`
**Solution**: Reduce batch size or use CPU mode:
```bash
export CUDA_VISIBLE_DEVICES=""
```

**Issue**: Poor redaction accuracy
**Solution**: Adjust confidence threshold in config:
```yaml
redaction:
  confidence_threshold: 0.75  # Lower for more sensitive detection
```

### Performance Optimization

- Use GPU acceleration when available
- Process documents in batches
- Adjust model parameters based on document types
- Use multi-threading for batch processing

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md).

### Reporting Issues

Please report issues using the [GitHub Issues](https://github.com/IshanRai0506/Viksit-Intelligent-Document-Redaction/issues) page.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [spaCy](https://spacy.io/) for NLP processing
- Uses [PyMuPDF](https://pymupdf.readthedocs.io/) for PDF handling
- Powered by [Transformers](https://huggingface.co/transformers/) for deep learning models

## Support

For support and questions:
- 📧 Email: support@viksit.dev
- 💬 Discussions: [GitHub Discussions](https://github.com/IshanRai0506/Viksit-Intelligent-Document-Redaction/discussions)
- 📖 Documentation: [docs.viksit.dev](https://docs.viksit.dev)

---

**Note**: This is an intelligent document redaction tool. Always review redacted documents to ensure all sensitive information has been properly handled according to your organization's data protection policies.