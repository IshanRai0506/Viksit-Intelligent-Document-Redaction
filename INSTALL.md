# Installation Guide

This guide provides detailed instructions for installing Viksit - Intelligent Document Redaction on different platforms and environments.

## Table of Contents

- [System Requirements](#system-requirements)
- [Quick Installation](#quick-installation)
- [Development Installation](#development-installation)
- [Docker Installation](#docker-installation)
- [Cloud Deployment](#cloud-deployment)
- [Troubleshooting](#troubleshooting)

## System Requirements

### Minimum Requirements

- **Operating System**: Windows 10+, macOS 10.15+, Ubuntu 18.04+
- **Python**: 3.8 or higher
- **RAM**: 4 GB minimum, 8 GB recommended
- **Storage**: 2 GB free space
- **CPU**: 2 cores minimum, 4 cores recommended

### Recommended Requirements

- **RAM**: 16 GB or more
- **Storage**: SSD with 10 GB free space
- **GPU**: NVIDIA GPU with CUDA support (optional, for faster processing)
- **CPU**: 8 cores or more

### Dependencies

The following system dependencies are required:

**Ubuntu/Debian**:
```bash
sudo apt-get update
sudo apt-get install python3-dev python3-pip python3-venv
sudo apt-get install poppler-utils tesseract-ocr
sudo apt-get install libmagic1 libffi-dev
```

**macOS**:
```bash
# Using Homebrew
brew install python3 poppler tesseract
brew install libmagic
```

**Windows**:
```powershell
# Using Chocolatey
choco install python3 poppler tesseract
# Or download and install manually from official websites
```

## Quick Installation

### For End Users

1. **Download and install Python 3.8+** from [python.org](https://www.python.org/downloads/)

2. **Install Viksit using pip**:
   ```bash
   pip install viksit-redaction
   ```

3. **Download required models**:
   ```bash
   viksit-setup
   ```

4. **Verify installation**:
   ```bash
   viksit --version
   viksit test-installation
   ```

### Using Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv viksit-env

# Activate virtual environment
source viksit-env/bin/activate  # Linux/macOS
# Or on Windows:
viksit-env\Scripts\activate

# Install Viksit
pip install viksit-redaction

# Setup models
viksit-setup
```

## Development Installation

### From Source

1. **Clone the repository**:
   ```bash
   git clone https://github.com/IshanRai0506/Viksit-Intelligent-Document-Redaction.git
   cd Viksit-Intelligent-Document-Redaction
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # Or on Windows: venv\Scripts\activate
   ```

3. **Install in development mode**:
   ```bash
   pip install -e .
   pip install -r requirements-dev.txt
   ```

4. **Install pre-commit hooks**:
   ```bash
   pre-commit install
   ```

5. **Download models and test data**:
   ```bash
   python setup.py develop
   python setup.py download_models
   python setup.py download_test_data
   ```

6. **Run tests to verify installation**:
   ```bash
   pytest tests/
   ```

### Development Dependencies

The development installation includes additional tools:

- **Testing**: pytest, pytest-cov, pytest-mock
- **Code Quality**: black, flake8, isort, mypy
- **Documentation**: sphinx, sphinx-rtd-theme
- **Pre-commit**: pre-commit hooks for code quality
- **Debugging**: ipdb, jupyter

## Docker Installation

### Using Pre-built Image

```bash
# Pull the latest image
docker pull viksit/intelligent-redaction:latest

# Run the container
docker run -p 5000:5000 -v $(pwd)/documents:/app/documents viksit/intelligent-redaction:latest
```

### Building from Source

```bash
# Clone repository
git clone https://github.com/IshanRai0506/Viksit-Intelligent-Document-Redaction.git
cd Viksit-Intelligent-Document-Redaction

# Build image
docker build -t viksit-redaction .

# Run container
docker run -p 5000:5000 -v $(pwd)/documents:/app/documents viksit-redaction
```

### Docker Compose

Create a `docker-compose.yml` file:

```yaml
version: '3.8'

services:
  viksit:
    image: viksit/intelligent-redaction:latest
    ports:
      - "5000:5000"
    volumes:
      - ./documents:/app/documents
      - ./output:/app/output
      - ./config:/app/config
    environment:
      - VIKSIT_CONFIG=/app/config/config.yaml
      - LOG_LEVEL=INFO
    restart: unless-stopped

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    restart: unless-stopped

  postgres:
    image: postgres:13
    environment:
      POSTGRES_DB: viksit
      POSTGRES_USER: viksit
      POSTGRES_PASSWORD: your_password_here
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    restart: unless-stopped

volumes:
  postgres_data:
```

Run with:
```bash
docker-compose up -d
```

## Cloud Deployment

### AWS EC2

1. **Launch EC2 instance** (recommended: t3.large or larger)

2. **Install Docker**:
   ```bash
   sudo yum update -y
   sudo yum install -y docker
   sudo service docker start
   sudo usermod -a -G docker ec2-user
   ```

3. **Deploy using Docker**:
   ```bash
   docker run -d --name viksit \
     -p 80:5000 \
     -v /home/ec2-user/documents:/app/documents \
     viksit/intelligent-redaction:latest
   ```

### Google Cloud Platform

1. **Create VM instance**:
   ```bash
   gcloud compute instances create viksit-instance \
     --image-family=debian-10 \
     --image-project=debian-cloud \
     --machine-type=n1-standard-2 \
     --boot-disk-size=20GB
   ```

2. **SSH and install**:
   ```bash
   gcloud compute ssh viksit-instance
   sudo apt-get update
   sudo apt-get install -y docker.io
   sudo docker run -d --name viksit -p 80:5000 viksit/intelligent-redaction:latest
   ```

### Azure Container Instances

```bash
az container create \
  --resource-group myResourceGroup \
  --name viksit-redaction \
  --image viksit/intelligent-redaction:latest \
  --dns-name-label viksit-redaction \
  --ports 5000
```

### Kubernetes

Create deployment files:

```yaml
# viksit-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: viksit-redaction
spec:
  replicas: 2
  selector:
    matchLabels:
      app: viksit-redaction
  template:
    metadata:
      labels:
        app: viksit-redaction
    spec:
      containers:
      - name: viksit
        image: viksit/intelligent-redaction:latest
        ports:
        - containerPort: 5000
        resources:
          requests:
            memory: "2Gi"
            cpu: "1"
          limits:
            memory: "4Gi"
            cpu: "2"
---
apiVersion: v1
kind: Service
metadata:
  name: viksit-service
spec:
  selector:
    app: viksit-redaction
  ports:
  - port: 80
    targetPort: 5000
  type: LoadBalancer
```

Deploy:
```bash
kubectl apply -f viksit-deployment.yaml
```

## Configuration

### Environment Variables

Create a `.env` file:

```bash
# Application settings
VIKSIT_ENV=production
SECRET_KEY=your-secret-key-here
DEBUG=false

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/viksit

# Redis (for caching and job queue)
REDIS_URL=redis://localhost:6379/0

# File storage
UPLOAD_FOLDER=/app/uploads
MAX_FILE_SIZE=100MB

# Model settings
MODEL_PATH=/app/models
CONFIDENCE_THRESHOLD=0.85

# Logging
LOG_LEVEL=INFO
LOG_FILE=/app/logs/viksit.log

# Security
ALLOWED_ORIGINS=https://yourdomain.com
SESSION_TIMEOUT=3600

# Performance
WORKER_PROCESSES=4
WORKER_TIMEOUT=300
```

### Production Configuration

For production deployments, create a `config/production.yaml`:

```yaml
app:
  debug: false
  secret_key: "your-production-secret-key"
  
database:
  url: "postgresql://user:password@db:5432/viksit"
  pool_size: 20
  max_overflow: 30

redis:
  url: "redis://redis:6379/0"
  
storage:
  type: "s3"  # or "local", "gcs"
  bucket: "viksit-documents"
  region: "us-west-2"
  
security:
  allowed_origins:
    - "https://app.viksit.com"
    - "https://api.viksit.com"
  rate_limiting:
    enabled: true
    requests_per_minute: 100
    
monitoring:
  enabled: true
  sentry_dsn: "your-sentry-dsn"
  metrics_endpoint: "/metrics"
```

## Troubleshooting

### Common Installation Issues

**Issue**: `pip install` fails with permission errors
**Solution**:
```bash
# Use virtual environment or user installation
pip install --user viksit-redaction
```

**Issue**: `ModuleNotFoundError: No module named 'cv2'`
**Solution**:
```bash
pip install opencv-python
```

**Issue**: Tesseract not found
**Solution**:
```bash
# Ubuntu/Debian
sudo apt-get install tesseract-ocr

# macOS
brew install tesseract

# Windows - download from: https://github.com/UB-Mannheim/tesseract/wiki
```

**Issue**: CUDA out of memory
**Solution**:
```bash
# Use CPU mode
export CUDA_VISIBLE_DEVICES=""
# Or reduce batch size in config
```

### Performance Issues

**Slow processing**:
- Enable GPU acceleration if available
- Increase number of worker processes
- Use SSD storage for better I/O performance
- Optimize model selection for your use case

**High memory usage**:
- Reduce batch size
- Process documents one at a time
- Use streaming processing for large files
- Monitor memory usage with system tools

### Docker Issues

**Container won't start**:
```bash
# Check logs
docker logs viksit-container-name

# Check resource usage
docker stats

# Restart container
docker restart viksit-container-name
```

**Port conflicts**:
```bash
# Use different port
docker run -p 8080:5000 viksit/intelligent-redaction:latest
```

### Getting Help

If you encounter issues not covered here:

1. Check the [FAQ](https://docs.viksit.dev/faq)
2. Search [existing issues](https://github.com/IshanRai0506/Viksit-Intelligent-Document-Redaction/issues)
3. Create a new issue with:
   - System information (`viksit --system-info`)
   - Error messages and logs
   - Steps to reproduce
   - Expected vs actual behavior

4. Join our community:
   - 💬 [Discord](https://discord.gg/viksit)
   - 📧 [Support email](mailto:support@viksit.dev)
   - 📖 [Documentation](https://docs.viksit.dev)

---

For the latest installation instructions, always refer to the [official documentation](https://docs.viksit.dev/installation).