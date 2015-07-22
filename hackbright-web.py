from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student_search")
def get_student_form():
    """Show form for searching for a student. """

    return render_template("student_search.html")


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github','jhacks')
    print github
    first, last, github = hackbright.get_student_by_github(github)
    print first, last,github
    html = render_template("student_info.html",first=first,last=last,github=github)
    return html



@app.route("/addStudent")
def send_add_form():
    return render_template("student_add.html")

@app.route("/student_add", methods=['POST'])
def student_add():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name,last_name,github)

    return "Student added!"


if __name__ == "__main__":
    app.run(debug=True)