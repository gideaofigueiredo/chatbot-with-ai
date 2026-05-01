# ChatWithAI

A simple Streamlit app for chatting with Google Gemini AI.

## Overview

This project provides a web chat interface where users can send messages and receive responses from the Gemini model `gemini-3-flash-preview`.

## Requirements

- Python 3.13+
- Streamlit
- google-genai
- python-dotenv

## Setup

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the environment:

- Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

- Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install streamlit google-genai python-dotenv
```

4. Create a `.env` file in the project root with your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

## Running the App

From the project folder, run:

```bash
streamlit run main.py
```

Then open the local URL shown by Streamlit in your browser.

## Project Files

- `main.py` - Streamlit application entry point
- `pyproject.toml` - project metadata
- `README.md` - project documentation

## Notes

- The app stores chat history in `st.session_state` during the browser session.
- Make sure `GEMINI_API_KEY` is set before launching the app.