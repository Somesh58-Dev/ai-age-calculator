# AI Age Calculator

A full-stack Python web app that calculates your exact age and adds a small machine-learning estimate.

**Live demo:** _add your Render link here after deploying_ https://ai-age-calculator.onrender.com

## Features
- Exact age in years, months and days, plus total days lived
- Next birthday countdown, birth weekday, zodiac sign and generation
- **ML module:** scikit-learn polynomial regression estimates remaining life expectancy
- Responsive UI with dark mode
- REST API (`POST /api/age`) with input validation
- Unit tests for the core logic

## Tech Stack
Python, Flask, scikit-learn, NumPy, HTML, CSS, JavaScript

## Project Structure
```
app.py          Flask server and API
age_logic.py    Age, zodiac, generation and birthday logic
ml_model.py     scikit-learn model (training + prediction)
templates/      HTML page
static/         CSS and JavaScript
tests/          Unit tests
```

## Run Locally
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Run Tests
```bash
pip install -r requirements-dev.txt
pytest
```

## API Example
```
POST /api/age
{"dob": "2007-02-10"}
```

## Note on the ML model
The model is trained on a small table of approximate life-expectancy values and is for
demonstration only. It is not a medical or insurance prediction.

## Future Improvements
- Train on a real public dataset (e.g. WHO life tables)

## Deployment
Deployed on Render (free tier). Build command: `pip install -r requirements.txt`, start command: `gunicorn app:app`.
