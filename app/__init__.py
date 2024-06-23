import os
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Example data for display
work_experiences = []
educations = []
hobbies = []


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="MLH Fellow",
        url=os.getenv("URL"),
        work_experiences=work_experiences,
        educations=educations,
        hobbies=hobbies,
    )


@app.route('/work', methods=['GET', 'POST'])
def work():
    if request.method == 'POST':
        if 'title' in request.form:
            new_experience = {
                "title": request.form["title"],
                "company": request.form["company"],
                "location": request.form["location"],
                "duration": request.form["duration"],
                "description": request.form["description"],
            }
            work_experiences.append(new_experience)
        elif 'degree' in request.form:
            new_education = {
                "degree": request.form["degree"],
                "university": request.form["university"],
                "location": request.form["location"],
                "duration": request.form["duration"],
                "description": request.form["description"],
            }
            educations.append(new_education)
        return redirect(url_for('work'))
    return render_template('work.html', title="Work and Education", work_experiences=work_experiences, educations=educations, url=os.getenv("URL"))


@app.route("/hobbies", methods=["GET", "POST"])
def hobbies_page():
    if request.method == "POST":
        new_hobby = {
            "name": request.form["name"],
            "description": request.form["description"],
        }
        hobbies.append(new_hobby)
        return redirect(url_for("hobbies_page"))
    return render_template(
        "hobbies.html", title="Hobbies", hobbies=hobbies, url=os.getenv("URL")
    )


@app.route("/places")
def places():
    return render_template("places.html", title="MLH Fellow", url=os.getenv("URL"))


@app.route("/add_experience", methods=["POST"])
def add_experience():
    new_experience = {
        "title": request.form["title"],
        "company": request.form["company"],
        "location": request.form["location"],
        "duration": request.form["duration"],
        "description": request.form["description"],
    }
    work_experiences.append(new_experience)
    return redirect(url_for("index"))


@app.route("/add_education", methods=["POST"])
def add_education():
    new_education = {
        "degree": request.form["degree"],
        "university": request.form["university"],
        "location": request.form["location"],
        "duration": request.form["duration"],
        "description": request.form["description"],
    }
    educations.append(new_education)
    return redirect(url_for("index"))


@app.route("/add_hobby", methods=["POST"])
def add_hobby():
    new_hobby = {
        "name": request.form["name"],
        "description": request.form["description"],
    }
    hobbies.append(new_hobby)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)