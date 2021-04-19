data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
        {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
        {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
        {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
        {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
        {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]


def get_bmi(d):
    l = len(d)
    for i in range(0, l):
        bmi = d[i]["WeightKg"] / ((d[i]["HeightCm"] / 100) * (d[i]["HeightCm"] / 100))
        d[i]["BMI"] = bmi
        if bmi <= 18.4:
            d[i]["BMICatergory"] = "Underweight"
            d[i]["Health Risk"] = "Malnutrition"
        if 18.5 <= bmi <= 24.9:
            d[i]["BMICatergory"] = "Normal Weight"
            d[i]["Health Risk"] = "Low risk"
        if 25 <= bmi <= 29.9:
            d[i]["BMICatergory"] = "Overweight"
            d[i]["Health Risk"] = "Enhanced risk"
        if 30 <= bmi <= 34.9:
            d[i]["BMICatergory"] = "Moderately Obese"
            d[i]["Health Risk"] = "Medium risk"
        if 35 <= bmi <= 39.9:
            d[i]["BMICatergory"] = "Severely Obese"
            d[i]["Health risk"] = "High risk"
        if bmi >= 40:
            d[i]["BMICatergory"] = "Very seriously obese"
            d[i]["Health Risk"] = "Very high risk"
    print(d)


get_bmi(data)
