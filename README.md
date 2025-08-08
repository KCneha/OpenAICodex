# OpenAICodex

This repository contains a minimal Flask application that serves a static webpage for experimenting with prompt inputs.

## Features
- Text area for arbitrary text blocks
- Separate fields for system and user prompts
- Generate button that sends the data to a dummy backend agent
- Output area displaying the dummy agent's response

## Running the app
1. Install dependencies:
   ```bash
   pip install flask
   ```
2. Start the development server:
   ```bash
   python app.py
   ```
3. Open `http://localhost:5000` in your browser.

The backend currently uses a placeholder agent that simply echoes the submitted values.
