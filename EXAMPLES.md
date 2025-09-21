# Quick Start Examples

This document provides quick examples to get you started with Viksit immediately.

## 1. Basic Document Redaction

### Command Line

```bash
# Redact a PDF file
python viksit.py redact document.pdf redacted_document.pdf

# Redact with specific entity types
python viksit.py redact document.pdf redacted.pdf --entities "person,phone,email"

# Preview redaction without applying changes
python viksit.py redact document.pdf preview.pdf --preview
```

### Python API

```python
from viksit import DocumentRedactor

# Initialize redactor
redactor = DocumentRedactor()

# Simple redaction
result = redactor.redact_document(
    input_path="sensitive_document.pdf",
    output_path="redacted_document.pdf"
)

print(f"Found {result['entities_found']} sensitive entities")
print(f"Redacted {result['entities_redacted']} entities")
```

## 2. Batch Processing

```bash
# Process all PDFs in a directory
python viksit.py batch ./documents ./redacted_documents --pattern "*.pdf"

# Parallel processing with 4 workers
python viksit.py batch ./documents ./output --parallel 4
```

## 3. Web Interface

```bash
# Start web server
python viksit.py serve

# Access at http://localhost:5000
# Upload documents through the web interface
```

## 4. Custom Configuration

Create a custom config file:

```yaml
# my_config.yaml
redaction:
  entity_types:
    - person
    - organization
    - phone
    - email
  confidence_threshold: 0.9
  custom_patterns:
    employee_id: "EMP-\\d{6}"
```

Use with CLI:
```bash
python viksit.py redact document.pdf output.pdf --config my_config.yaml
```

## 5. Docker Usage

```bash
# Run with Docker
docker run -v $(pwd)/docs:/app/documents viksit/redaction \
  python viksit.py redact /app/documents/input.pdf /app/documents/output.pdf

# Use Docker Compose for full stack
docker-compose up -d
```

## 6. Example Output

```
$ python viksit.py redact sample.pdf redacted.pdf --verbose

Processing: sample.pdf
Entity types: person, organization, location, phone, email, ssn
Confidence threshold: 0.85

Redacting document ████████████████████████████████████████ 100%

✅ Redaction completed successfully!
📄 Output saved to: redacted.pdf
🔍 Entities found: 23
🚫 Entities redacted: 23

Detailed results:
  person: 8
  phone: 3
  email: 5
  organization: 4
  location: 3
```

## 7. Testing Installation

```bash
# Run system tests
python viksit.py test

# Check system information
python viksit.py info

# Setup models and dependencies
python viksit.py setup
```

## 8. Common Use Cases

### Legal Document Review
```bash
# Redact client information from legal documents
python viksit.py redact contract.pdf redacted_contract.pdf \
  --entities "person,organization,phone,email,address"
```

### Medical Records
```bash
# Redact patient information from medical records
python viksit.py redact medical_record.pdf anonymized_record.pdf \
  --entities "person,phone,email,ssn,date" \
  --confidence 0.95
```

### Financial Documents
```bash
# Redact sensitive financial information
python viksit.py redact financial_report.pdf redacted_report.pdf \
  --entities "person,organization,phone,email,credit_card,ssn"
```

### Research Data
```bash
# Anonymize research documents
python viksit.py redact research_data.pdf anonymized_data.pdf \
  --entities "person,email,phone" \
  --preview  # Review before final redaction
```

## 9. API Integration

```python
# Advanced API usage
from viksit import DocumentRedactor
from viksit.config import load_config

# Load custom configuration
config = load_config("my_config.yaml")
redactor = DocumentRedactor(config)

# Process with callback for progress tracking
def progress_callback(progress):
    print(f"Progress: {progress}%")

result = redactor.redact_document(
    input_path="document.pdf",
    output_path="redacted.pdf",
    entity_types=["person", "organization"],
    confidence_threshold=0.9,
    progress_callback=progress_callback
)

# Access detailed results
for entity_type, entities in result['entities'].items():
    print(f"{entity_type}: {len(entities)} found")
    for entity in entities:
        print(f"  - {entity['text']} (confidence: {entity['confidence']})")
```

## 10. Troubleshooting Quick Fixes

```bash
# If models are missing
python -m spacy download en_core_web_sm

# If CUDA out of memory
export CUDA_VISIBLE_DEVICES=""

# If permission errors
sudo chown -R $USER:$USER ./uploads ./output

# If port already in use
python viksit.py serve --port 8080
```

For more detailed instructions, see:
- [README.md](README.md) - Full documentation
- [INSTALL.md](INSTALL.md) - Installation guide
- [CONTRIBUTING.md](CONTRIBUTING.md) - Development setup