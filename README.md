# Viksit-Intelligent-Document-Redaction

1. Project Overview for Hackathon Judges
Team: Viksit
Objective: To create a "Trust by Design" solution that automatically redacts sensitive information (PII, PHI) from documents, making them safe to share while ensuring privacy compliance.

Organizations in healthcare, finance, and government struggle with manual, slow, and error-prone redaction of sensitive data, despite legal mandates like GDPR and HIPAA. Viksit provides an intelligent, automated, and highly accurate solution to protect PII/PHI across various document formats, ensuring compliance and enabling safe data use.

Viksit is a self-contained web application that leverages a hybrid AI model. It combines Optical Character Recognition (OCR), Named Entity Recognition (NER) for text analysis, and object detection for visual elements like signatures. This allows for a higher degree of accuracy than traditional text-only redaction tools.

This document provides instructions for setting up, running, and evaluating the application.

2. Quick Start: Local Execution (For Technical Review)
This section provides the fastest path to running the application locally. Please ensure the system prerequisites (Tesseract and Poppler) are installed first. (See Section 4 for details).

Clone the Repository (if applicable) & Navigate to Folder:
Open a terminal in the project directory containing app.py.

Set Up and Activate Virtual Environment:

# Create the environment
python -m venv venv
# Activate it (macOS/Linux)
source venv/bin/activate
# Activate it (Windows)
.\\venv\\Scripts\\activate


Install Dependencies:

pip install -r requirements.txt


Download AI Model:

python -m spacy download en_core_web_sm


Run the Application:

python app.py


Access the Tool:
Open your web browser and navigate to: https://www.google.com/search?q=http://127.0.0.1:5000

3. How to Test the Application
Once the application is running, please follow these steps to verify its functionality:

Upload a Document: Use the drag-and-drop interface or the "Choose File" button to upload a document (PDF, PNG, or JPG). Sample documents with PII should be included in the project repository.

Process: Click the "Process Document" button.

Review Results:

Side-by-Side View: Compare the original document on the left with the redacted version on the right. Verify that sensitive information (names, dates, SSNs, etc.) has been blacked out.

Redaction Summary: Check the statistics at the top to see a count of the different types of information found.

Audit Log: Review the "Redaction Log" to see a detailed list of every item that was redacted.

Download Artifacts: Test the download buttons to save the redacted document and the JSON audit log.

4. Detailed Setup Instructions & Prerequisites
This section contains detailed installation instructions for required third-party software.

a) Python (3.8+ is recommended)
The application is built with Python. Download from python.org if not already installed.

b) Tesseract-OCR Engine
Required for extracting text from images.

macOS (Homebrew): brew install tesseract

Ubuntu/Debian: sudo apt update && sudo apt install -y tesseract-ocr

Windows: Download the installer from the Tesseract at UB Mannheim page and add the installation folder to your system's PATH.

c) Poppler
Required for converting PDF files into images.

macOS (Homebrew): brew install poppler

Ubuntu/Debian: sudo apt update && sudo apt install -y poppler-utils

Windows: Download the binaries from this page, extract them, and add the bin subfolder to your system's PATH.

5. Deployment & Scalability
The application has been architected for easy deployment and scalability using Docker. This approach ensures that the environment is consistent and all system dependencies are handled automatically.

a) Dockerfile
A Dockerfile is included in the project. This file contains all the instructions to build a container image with the Python environment, Tesseract, Poppler, and all necessary libraries. This makes deployment to any modern cloud provider (like Render, Heroku, or AWS) straightforward.

b) Production Server
The Dockerfile is configured to use Gunicorn, a production-grade web server, to run the Flask application, ensuring stability and the ability to handle multiple concurrent users. The requirements.txt file should include gunicorn for deployment.
