Viksit: AI-Powered Document Redaction Tool
<div align="center">

A "Trust by Design" solution that automatically redacts sensitive information from documents, making them safe to share while ensuring privacy compliance.

</div>

<p align="center">
<a href="#-about-the-project">About</a> •
<a href="#-key-features">Key Features</a> •
<a href="#-getting-started">Getting Started</a> •
<a href="#-usage">Usage</a> •
<a href="#-deployment">Deployment</a> •
<a href="#-contributing">Contributing</a>
</p>



📖 About The Project
Organizations in healthcare, finance, and government struggle with manual, slow, and error-prone redaction of sensitive data, despite legal mandates like GDPR and HIPAA. Viksit provides an intelligent, automated, and highly accurate solution to protect Personally Identifiable Information (PII) and Protected Health Information (PHI) across various document formats, ensuring compliance and enabling safe data use.

Viksit is a self-contained web application that leverages a hybrid AI model, building a foundation of trust through verifiable privacy protection.

✨ Key Features
Hybrid AI Model: Combines OCR (for text), NER (for PII/PHI), and Object Detection (for signatures/barcodes) for superior accuracy.

Multiple Format Support: Processes PDF, PNG, and JPG documents, including scanned files with handwritten notes.

Side-by-Side View: An intuitive UI allows for easy comparison between the original and redacted document.

Audit Trail: Generates a detailed JSON log of all redactions for compliance and traceability.

Self-Contained & Deployable: Packaged as a single Flask application, easily containerized with Docker for simple deployment.

🛠️ Built With
Backend: Python, Flask, Gunicorn

AI/ML: spaCy, Pytesseract (Tesseract-OCR), pdf2image, Pillow

Frontend: HTML, CSS, JavaScript (served via Flask)

Containerization: Docker

🚀 Getting Started
Follow these instructions to get a local copy up and running for development and testing.

Prerequisites
You must have the following third-party software installed on your system.

Python 3.8+

Download from python.org.

Tesseract-OCR Engine

macOS: brew install tesseract

Ubuntu/Debian: sudo apt update && sudo apt install -y tesseract-ocr

Windows: Download from Tesseract at UB Mannheim and add the installation directory to your system's PATH.

Poppler

macOS: brew install poppler

Ubuntu/Debian: sudo apt update && sudo apt install -y poppler-utils

Windows: Download from Poppler for Windows, extract, and add the bin folder to your system's PATH.

Installation
Clone the repository:

git clone [https://github.com/IshanRai0506/Viksit-Intelligent-Document-Redaction](https://github.com/IshanRai0506/Viksit-Intelligent-Document-Redaction)
cd viksit

Create and activate a virtual environment:

python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate

Install Python dependencies:

pip install -r requirements.txt

Download the spaCy AI model:

python -m spacy download en_core_web_sm

Running the Application
Start the Flask server:

python app.py

Open the application:
Navigate to http://127.0.0.1:5000 in your web browser.

💻 Usage
Once the application is running, you can test its core functionality:

Upload a Document: Drag and drop a file (PDF, PNG, JPG) onto the upload area or use the "Choose File" button.

Process: Click the "Process Document" button to start the AI analysis.

Review Results:

Side-by-Side View: Compare the original document with the redacted version.

Redaction Summary: See a statistical breakdown of the sensitive data found.

Audit Log: View a detailed list of every redacted item for compliance purposes.

Download: Save the secure, redacted document and the JSON audit log to your local machine.

🐳 Deployment
This application is designed for easy deployment using Docker. A Dockerfile is included, which handles all system dependencies (Tesseract, Poppler) and sets up a production-ready environment with Gunicorn. You can deploy this application to any cloud service that supports Docker containers, such as Render, Heroku, or AWS.

🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
Distributed under the MIT License. See LICENSE file for more information.

👥 Contact
Team Viksit

Project Link: https://github.com/IshanRai0506/Viksit-Intelligent-Document-Redaction
