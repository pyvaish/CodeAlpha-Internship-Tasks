from flask import Flask, render_template, request, redirect

app = Flask(__name__)

projects = [
    {
        "id": 1,
        "name": "Website Project",
        "tasks": [
            {
                "title": "Design Homepage",
                "assigned_to": "Vaishnavi",
                "comments": ["Complete navbar first"]
            }
        ]
    }
]

# Home Page
@app.route('/')
def home():
    return render_template(
        'index.html',
        projects=projects
    )

# Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# Create Project
@app.route('/create_project', methods=['GET', 'POST'])
def create_project():

    if request.method == 'POST':

        project_name = request.form['project_name']

        new_project = {
            "id": len(projects) + 1,
            "name": project_name,
            "tasks": []
        }

        projects.append(new_project)

        return redirect('/')

    return render_template('create_project.html')

# Project Details
@app.route('/project/<int:id>')
def project(id):

    selected_project = None

    for project in projects:
        if project["id"] == id:
            selected_project = project

    return render_template(
        'project.html',
        project=selected_project
    )

# Create Task
@app.route('/create_task/<int:id>', methods=['GET', 'POST'])
def create_task(id):

    selected_project = None

    for project in projects:
        if project["id"] == id:
            selected_project = project

    if request.method == 'POST':

        title = request.form['title']
        assigned_to = request.form['assigned_to']
        comment = request.form['comment']

        task = {
            "title": title,
            "assigned_to": assigned_to,
            "comments": [comment]
        }

        selected_project["tasks"].append(task)

        return redirect(f'/project/{id}')

    return render_template(
        'create_task.html',
        project=selected_project
    )

if __name__ == '__main__':
    app.run(debug=True)