#!/bin/bash

# Viksit - Intelligent Document Redaction Setup Script
# This script sets up the development environment for Viksit

set -e

echo "🚀 Setting up Viksit - Intelligent Document Redaction"
echo "=================================================="

# Check Python version
echo "🐍 Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✅ Python $PYTHON_VERSION found"

# Check if version is 3.8 or higher
if python3 -c 'import sys; exit(0 if sys.version_info >= (3, 8) else 1)'; then
    echo "✅ Python version is compatible"
else
    echo "❌ Python 3.8 or higher is required. Current version: $PYTHON_VERSION"
    exit 1
fi

# Create virtual environment
echo "📦 Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "ℹ️  Virtual environment already exists"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
python -m pip install --upgrade pip

# Install requirements
echo "📚 Installing requirements..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "✅ Main requirements installed"
fi

if [ -f "requirements-dev.txt" ]; then
    echo "🛠️  Installing development requirements..."
    pip install -r requirements-dev.txt
    echo "✅ Development requirements installed"
fi

# Install pre-commit hooks
if command -v pre-commit &> /dev/null; then
    echo "🪝 Installing pre-commit hooks..."
    pre-commit install
    echo "✅ Pre-commit hooks installed"
fi

# Download spaCy models
echo "🧠 Downloading language models..."
python -m spacy download en_core_web_sm || echo "⚠️  Failed to download spaCy model. You may need to run this manually."

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p uploads output temp logs models
echo "✅ Directories created"

# Set permissions
chmod +x viksit.py

# Check if everything is working
echo "🧪 Testing installation..."
if python -c "import spacy; print('✅ spaCy working')"; then
    echo "✅ Basic imports working"
else
    echo "⚠️  Some imports failed. Check the error messages above."
fi

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "📋 Next steps:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Test the installation: python viksit.py test"
echo "3. Try redacting a document: python viksit.py redact input.pdf output.pdf"
echo "4. Start the web server: python viksit.py serve"
echo ""
echo "📖 For more information, see README.md and INSTALL.md"
echo "🐛 If you encounter issues, check the troubleshooting section in INSTALL.md"