from datetime import date

from flask import Flask, jsonify, render_template, request

from age_logic import calculate_age, generation, next_birthday, zodiac_sign
from ml_model import predict_remaining_years

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/age", methods=["POST"])
def api_age():
    data = request.get_json(silent=True) or {}
    try:
        birth = date.fromisoformat(data.get("dob", ""))
    except ValueError:
        return jsonify(error="Please send a valid date (YYYY-MM-DD)."), 400

    today = date.today()
    if birth > today:
        return jsonify(error="Date of birth cannot be in the future."), 400
    if today.year - birth.year > 120:
        return jsonify(error="Please enter a realistic date of birth."), 400

    age = calculate_age(birth, today)
    remaining = predict_remaining_years(age["years"] + age["months"] / 12)
    lived = age["years"] + age["months"] / 12
    progress = round(lived / (lived + remaining) * 100, 1) if remaining else 100.0

    return jsonify(
        age=age,
        born_on=birth.strftime("%A"),
        zodiac=zodiac_sign(birth),
        generation=generation(birth.year),
        next_birthday=next_birthday(birth, today),
        ml={"remaining_years": remaining, "life_progress_percent": progress},
    )


if __name__ == "__main__":
    # debug=True only for local development; the live server uses gunicorn
    app.run(debug=True)
