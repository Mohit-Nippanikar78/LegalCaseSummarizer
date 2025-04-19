# CaseSummarizer

A web-based tool that leverages AI to generate concise and professional summaries of legal case documents.

![CaseSummarizer](https://img.shields.io/badge/App-CaseSummarizer-blue)
![Python](https://img.shields.io/badge/Python-3.7+-brightgreen)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Mistral AI](https://img.shields.io/badge/AI-Mistral-purple)

## Overview

CaseSummarizer is a Streamlit application designed to help legal professionals, law students, and researchers quickly extract the essential information from lengthy legal case documents. By leveraging Mistral AI's powerful language capabilities, the tool provides accurate, concise, and professional summaries of uploaded case files.

## Features

- **Simple Upload Interface**: Upload any .txt file containing legal case text
- **AI-Powered Summarization**: Uses Mistral AI to extract key points and generate concise summaries
- **Professional Output**: Summaries maintain legal terminology and critical case information
- **Download Capability**: Save your generated summaries as text files for later use

## How It Works

1. Upload your legal case document (.txt format)
2. Review the uploaded text
3. Click "Summarize" to initiate the AI analysis
4. Receive a professionally formatted summary
5. Download the summary for your records

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/CaseSummarizer.git
cd CaseSummarizer

# Install dependencies
pip install -r requirements.txt
```

## Configuration

The application requires a Mistral AI API key to function. You'll need to:

1. Get an API key from [Mistral AI](https://www.mistral.ai/)
2. Create a `.streamlit/secrets.toml` file with your API key:

```toml
MISTRAL_API_KEY = "your-api-key-here"
```

## Usage

Run the Streamlit app:

```bash
streamlit run index.py
```

Then open your browser and navigate to the provided URL (typically http://localhost:8501).

## Requirements

- Python 3.7+
- Streamlit
- llama-index
- MistralAI API access

## License

MIT

---

Created with ❤️ for the legal community 