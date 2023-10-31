from flask import Flask, request, send_file, make_response, render_template, url_for, send_from_directory
from markupsafe import Markup
import json
from docx import Document
import os
from io import BytesIO
import markdown2
import markdown

app = Flask(__name__)
# markdown2.markdown(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

# This method takes the uploaded file and stores it on the server in the uploads folder.
# This method also outputs where the file was saved.

# Define a directory to store uploaded files

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    # Ensure that the filename does not include the uploads/ prefix
    filename = filename.replace('uploads/', '', 1)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/upload1', methods=['GET', 'POST'])
def upload_file_1():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.json'):
            json_data = json.load(file)

            markdown_text = "# Table of JSON Data\n\n"
            markdown_text += "| Key | Value |\n"
            markdown_text += "|---|---|\n"
            for key, value in json_data.items():
                markdown_text += f"| {key} | {value} |\n"
            
            output_filename = 'output1.md'
            # output_filepath = os.path.join(UPLOAD_FOLDER, output_filename)
            # output_filepath = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
            # absolute_filepath = os.path.abspath(output_filepath)
            output_filepath = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)

            with open(output_filepath, 'w') as md_file:
                md_file.write(markdown_text)

            # Convert Markdown to HTML - Needed markdown2 so we could specify table format
            html_content = markdown2.markdown(markdown_text, extras=["tables"])

            return render_template('display_markdown.html', html_content=Markup(html_content), md_link=output_filename, location=output_filepath)

    return render_template("display_markdown.html", content=None)


@app.route('/upload2', methods=['POST'])
def upload_file_2():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file and file.filename.endswith('.json'):
        try:
            json_data = json.load(file)
            markdown_text = "# Table of JSON Data\n\n"
            markdown_text += "| Key | Value |\n"
            markdown_text += "|---|---|\n"

            for key, value in json_data.items():
                markdown_text += f"| {key} | {value} |\n"

            response = make_response(markdown_text)
            response.headers["Content-Disposition"] = "attachment; filename=output.md"
            response.mimetype = 'text/markdown'
            return response

        except Exception as e:
            return str(e)
    
    return 'Invalid file format. Please upload a JSON file.'

@app.route('/upload3', methods=['POST'])
def upload_file_3():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file and file.filename.endswith('.json'):
        try:
            json_data = json.load(file)
            doc = Document()
            for key, value in json_data.items():
                table = doc.add_table(rows=1, cols=2)
                hdr_cells = table.rows[0].cells
                hdr_cells[0].text = 'Key'
                hdr_cells[1].text = 'Value'
                row_cells = table.add_row().cells
                row_cells[0].text = str(key)
                row_cells[1].text = str(value)
                doc.add_paragraph()

            # Save the document to a BytesIO object
            f = BytesIO()
            doc.save(f)
            f.seek(0)

            return send_file(f, as_attachment=True, download_name='output.docx', mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        
        except Exception as e:
            return str(e)
    
    return 'Invalid file format. Please upload a JSON file.'

if __name__ == '__main__':
    app.run(debug=True)
