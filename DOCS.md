# Viksit Project Documentation Index

Welcome to the Viksit Intelligent Document Redaction project! This directory contains all the documentation you need to get started, contribute, and deploy the system.

## 📚 Documentation Overview

### Getting Started
- **[README.md](README.md)** - Main project overview, features, and quick start guide
- **[EXAMPLES.md](EXAMPLES.md)** - Quick start examples and common use cases
- **[INSTALL.md](INSTALL.md)** - Detailed installation guide for all platforms

### For Users
- **[viksit.py](viksit.py)** - Command-line interface with all available commands
- **[config.yaml](config.yaml)** - Complete configuration example with all options
- **[requirements.txt](requirements.txt)** - Python dependencies for end users

### For Developers
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Complete guide for contributors
- **[requirements-dev.txt](requirements-dev.txt)** - Development dependencies
- **[setup.sh](setup.sh)** - Automated development environment setup

### For Deployment
- **[Dockerfile](Dockerfile)** - Container configuration for Docker deployment
- **[docker-compose.yml](docker-compose.yml)** - Full stack deployment with database
- **[.gitignore](.gitignore)** - Git ignore rules for the project

### Legal
- **[LICENSE](LICENSE)** - MIT License terms

## 🚀 Quick Navigation

### I want to...

**Use Viksit for document redaction:**
1. Start with [README.md](README.md) overview
2. Follow [INSTALL.md](INSTALL.md) for installation
3. Try [EXAMPLES.md](EXAMPLES.md) for quick start

**Contribute to the project:**
1. Read [CONTRIBUTING.md](CONTRIBUTING.md)
2. Run [setup.sh](setup.sh) for development setup
3. Check the issue tracker for tasks

**Deploy Viksit in production:**
1. Review [INSTALL.md](INSTALL.md) deployment section
2. Configure using [config.yaml](config.yaml) as template
3. Use [Docker](Dockerfile) or [docker-compose.yml](docker-compose.yml)

**Understand the CLI:**
1. Run `python viksit.py --help`
2. Check [viksit.py](viksit.py) for all commands
3. See [EXAMPLES.md](EXAMPLES.md) for usage examples

## 📋 Project Structure

```
Viksit-Intelligent-Document-Redaction/
├── README.md              # Main project documentation
├── INSTALL.md             # Installation instructions
├── EXAMPLES.md            # Usage examples
├── CONTRIBUTING.md        # Contributor guidelines
├── LICENSE                # License information
├── viksit.py             # Command-line interface
├── config.yaml           # Configuration template
├── setup.sh              # Development setup script
├── requirements.txt      # Python dependencies
├── requirements-dev.txt  # Development dependencies
├── Dockerfile            # Docker container configuration
├── docker-compose.yml    # Multi-service deployment
└── .gitignore           # Git ignore rules
```

## 🔄 Workflow Examples

### First-time User
```bash
git clone https://github.com/IshanRai0506/Viksit-Intelligent-Document-Redaction.git
cd Viksit-Intelligent-Document-Redaction
chmod +x setup.sh
./setup.sh
python viksit.py test
python viksit.py redact sample.pdf redacted.pdf
```

### Developer Setup
```bash
git clone https://github.com/yourusername/Viksit-Intelligent-Document-Redaction.git
cd Viksit-Intelligent-Document-Redaction
./setup.sh
pre-commit install
pytest tests/
```

### Production Deployment
```bash
git clone https://github.com/IshanRai0506/Viksit-Intelligent-Document-Redaction.git
cd Viksit-Intelligent-Document-Redaction
docker-compose up -d
```

## 🆘 Getting Help

1. **Check documentation first** - Most questions are answered in the docs
2. **Search existing issues** - Your question might already be answered
3. **Ask in discussions** - For general questions and help
4. **Create an issue** - For bugs and feature requests
5. **Join the community** - Discord/forums for real-time help

## 📊 Documentation Status

| Document | Status | Last Updated | Purpose |
|----------|--------|--------------|---------|
| README.md | ✅ Complete | 2024-01 | Project overview |
| INSTALL.md | ✅ Complete | 2024-01 | Installation guide |
| EXAMPLES.md | ✅ Complete | 2024-01 | Usage examples |
| CONTRIBUTING.md | ✅ Complete | 2024-01 | Developer guide |
| viksit.py | ✅ Complete | 2024-01 | CLI interface |
| config.yaml | ✅ Complete | 2024-01 | Configuration |

## 🔗 External Resources

- **Project Repository**: https://github.com/IshanRai0506/Viksit-Intelligent-Document-Redaction
- **Documentation Site**: https://docs.viksit.dev (planned)
- **Community Discord**: https://discord.gg/viksit (planned)
- **Issue Tracker**: https://github.com/IshanRai0506/Viksit-Intelligent-Document-Redaction/issues

---

**Note**: This project is under active development. Documentation is updated regularly to reflect the latest features and changes. If you find any outdated information, please [create an issue](https://github.com/IshanRai0506/Viksit-Intelligent-Document-Redaction/issues/new) or submit a pull request.