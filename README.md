# PluginJsonUpload

A simple Flask application to demonstrate file upload functionality, JSON processing, and rendering Markdown content in a web page.

## Features

- File Upload: Users can upload JSON files through a web interface.
- JSON Processing: The application reads the uploaded JSON file, processes its contents, and converts it to a Markdown table.
- Markdown Rendering: The generated Markdown table is rendered and displayed on the web page.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/derekadam3c/PluginJsonUpload.git
    cd PluginJsonUpload
    ```

2. **Create a Virtual Environment (optional)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Requirements**:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the Flask Application**:

    ```bash
    python app.py
    ```

    The application will be available at `http://127.0.0.1:5000/`.

2. **Access the Web Interface**:

    Open your preferred web browser and visit `http://127.0.0.1:5000/`. Use the provided file input to upload a JSON file.

## Usage

1. **Upload a JSON File**: Click on the "Choose File" button and select a JSON file from your computer.
2. **Submit the File**: Click on the "Upload" button to submit the file. The application will process the file and render the generated Markdown table on the web page.


## IO
**Example Input**: 

        {"elephant": 8, "tiger": 5, "kangaroo": 8, "giraffe": 7, "zebra": 5}

 **Example Output**: 
| Key | Value |
|---|---|
| elephant | 8 |
| tiger | 5 |
| kangaroo | 8 |
| giraffe | 7 |
| zebra | 5 |


