# app.py
from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Basic keywords to search for in resumes
KEYWORDS = ['Python', 'Docker', 'Flask', 'Machine Learning', 'Data Analysis']

# Function to analyze the resume
def analyze_resume(file_content):
    found_keywords = [keyword for keyword in KEYWORDS if keyword.lower() in file_content.lower()]
    return found_keywords

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.txt'):
            content = file.read().decode('utf-8')
            keywords = analyze_resume(content)
            return render_template('index.html', keywords=keywords, filename=file.filename)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

