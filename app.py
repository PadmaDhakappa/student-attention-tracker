from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

students = [
    "Vivvica Singh", "Sanvi Sharma", "Dharshini Santhosh Kumar", "Sahar Anamika Haider",
    "Kushan Sarath", "Rohan Ambavaram", "Kimaya Anish", "Vikaas Gurumoorthy",
    "Amey Gopikrishna", "Ojas Chaturvedi", "Ishanvi Yejja", "Vikrant Reddy Maddirala"
]

def generate_data():
    data = []
    for s in students:
        attention = round(random.uniform(85, 95), 1)
        data.append({"name": s, "attention": attention})
    return data


@app.route("/")
def home():
    return render_template("index.html")   # <--- FIXED


@app.route("/data")
def data():
    student_data = generate_data()
    avg_att = round(sum(s["attention"] for s in student_data) / len(student_data), 1)
    avg_inatt = round(100 - avg_att, 1)

    return jsonify({
        "students": student_data,
        "total": len(student_data),
        "avg_att": avg_att,
        "avg_inatt": avg_inatt
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
