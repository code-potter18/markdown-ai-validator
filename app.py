import os
from flask import Flask, render_template, request
from agent.markdown_agent import create_markdown_agent

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

agent = create_markdown_agent()

@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    if request.method == "POST":
        uploaded_file = request.files.get("file")
        if uploaded_file and uploaded_file.filename.endswith(".md"):
            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(file_path)

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            issues = agent.tools[0](content)

            for i, issue in enumerate(issues, start=1):
                results.append(f"{i}. Issue: {issue['issue']}\n   Fix: {issue['fix']}")

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
