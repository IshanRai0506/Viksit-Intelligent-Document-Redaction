FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    poppler-utils \
    tesseract-ocr \
    tesseract-ocr-eng \
    libmagic1 \
    libffi-dev \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p /app/uploads /app/output /app/logs /app/models

# Download models during build
RUN python -c "import spacy; spacy.cli.download('en_core_web_sm')"

# Set environment variables
ENV PYTHONPATH=/app/src
ENV VIKSIT_ENV=production
ENV UPLOAD_FOLDER=/app/uploads
ENV OUTPUT_FOLDER=/app/output
ENV LOG_FILE=/app/logs/viksit.log

# Create non-root user
RUN useradd -m -u 1000 viksit && chown -R viksit:viksit /app
USER viksit

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:5000/health')" || exit 1

# Default command
CMD ["python", "viksit.py", "serve", "--host", "0.0.0.0", "--port", "5000"]