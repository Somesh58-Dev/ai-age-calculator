"""Small ML module: estimates remaining life expectancy from current age.

The training table below holds APPROXIMATE, rounded values (inspired by
public life-table figures for India). It is meant for demonstration only,
not for any medical or insurance use.
"""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

# (age, average remaining years of life) - approximate sample data
SAMPLE_DATA = [
    (0, 70.0), (10, 62.0), (20, 53.0), (30, 44.5), (40, 36.0),
    (50, 28.0), (60, 20.5), (70, 14.0), (80, 8.5), (90, 5.0), (100, 3.0),
]


def train_model():
    """Train a polynomial regression (degree 3) on the sample table."""
    ages = np.array([row[0] for row in SAMPLE_DATA]).reshape(-1, 1)
    remaining = np.array([row[1] for row in SAMPLE_DATA])
    model = make_pipeline(PolynomialFeatures(degree=3), LinearRegression())
    model.fit(ages, remaining)
    return model


_MODEL = train_model()


def predict_remaining_years(age_years: float) -> float:
    """Return estimated remaining years (never negative)."""
    value = float(_MODEL.predict(np.array([[age_years]]))[0])
    return max(round(value, 1), 0.0)
