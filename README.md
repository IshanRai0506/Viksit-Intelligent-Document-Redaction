Viksit: AI-Powered Document Redaction Tool
<div align="center">
<img src="https://www.google.com/search?q=https://placehold.co/600x300/667eea/ffffff%3Ftext%3DViksit%2BDemo%26font%3Dinter" alt="Viksit Application Screenshot">
</div>

<p align="center">
A "Trust by Design" solution that automatically redacts sensitive information from documents, making them safe to share while ensuring privacy compliance.
</p>

📖 About The Project
Organizations in healthcare, finance, and government struggle with manual, slow, and error-prone redaction of sensitive data, despite legal mandates like GDPR and HIPAA. Viksit provides an intelligent, automated, and highly accurate solution to protect Personally Identifiable Information (PII) and Protected Health Information (PHI) across various document formats, ensuring compliance and enabling safe data use.

Viksit is a self-contained web application that leverages a hybrid AI model. It combines:

Optical Character Recognition (OCR) to digitize text.

Named Entity Recognition (NER) to identify sensitive textual data.

Object Detection to find visual elements like signatures and barcodes.

This hybrid approach allows for a higher degree of accuracy than traditional text-only redaction tools, building a foundation of trust through verifiable privacy protection.

✨ Built With
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

git clone [https://github.com/your-username/viksit.git](https://github.com/your-username/viksit.git)
cd viksit

Create and activate a virtual environment:

python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\\venv\\Scripts\\activate

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
This application is designed for easy deployment using Docker. A Dockerfile is included, which handles all system dependencies (Tesseract, Poppler) and sets up a production-ready environment with Gunicorn.

You can deploy this application to any cloud service that supports Docker containers, such as Render, Heroku, or AWS.

📄 License
Distributed under the MIT License. See LICENSE for more information.

👥 Contact
Team Viksit
