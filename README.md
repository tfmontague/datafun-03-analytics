# Specification for Project 3 Python Module

## Overview

Project 3 emphasizes skills in using Git for version control, creating and managing Python virtual environments, and handling different types of data.
The project involves fetching data from the web, processing it using appropriate Python collections, and writing the processed data to files.

## Deliverable Names

- GitHub Repository:  **datafun-03-analytics**
- Documentation:      README.md
- Script:             **yourname_analytics.py**

Create a new GitHub repository with a default README.md and the required name. 
After creating it, use git to clone it down to your machine. 

## External Dependencies

This project will require the following external modules:

- requests

## Version Control with Git

Use Git for version control.
In your README.md, document the steps of initializing a new project in GitHub and on your machine.
Explain the process for creating the repository in both places,
and document your workflow as you edit, add, commit, and push to GitHub.

## Objective

Create a Python module that demonstrates skills in fetching data from the web, processing it using Python collections, and writing the processed data to different file formats.

## Requirements

Since the project uses modules beyond the Python Standard Library, create a project virtual environment. 

### 1. Environment Setup

1. Create and activate a Python virtual environment for the project.
1. Install all required packages into your local project virtual environment.
1. After installing the required dependencies, redirect the output of the pip freeze command to a requirements.txt file in your root project folder.
1. Document the process and commands you used in your README.md.
1. Add a .gitignore file to your project to exclude the virtual environment folder, your .vscode settings folder, and any other files that do not need to be committed to GitHub.

Windows example:

```Powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install requests
py -m pip freeze > requirements.txt
```

Mac example:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install requests
python3 -m pip freeze > requirements.txt
```

### 2. Project Start

In your Python file, create a docstring with a brief introduction to your project.

### 3. Import Dependencies

Organize your project imports following conventions.
For example, standard library imports first, then external library imports, then local module imports. 
Continue to practice importing your own modules and reuse your prior code when building your project folders.
Conventional package import organization example:

```python

# Standard library imports
import csv
import pathlib 

# External library imports (requires virtual environment)
import requests  

# Local module imports
import yourname_attr      
import yourname_projsetup 
```

### 4.  Data Acquisition

Use the requests library to fetch data from specified web APIs or online data sources.
This will include JSON, CSV, and plain text data.
After a successful fetch, call the appropriate write function to save the data to a file.
For example:

```python
import requests

def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

```

### 5. Write Data

Write functions to save content to different file types (e.g., text, CSV, JSON).
For example:

```python
from pathlib import Path

def write_txt_file(folder_name, filename, data):
    file_path = Path(folder_name).join_path(filename) # use pathlib to join paths
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")


def write_excel_file(folder_name, filename, data):
    file_path = Path(folder_name).join_path(filename) # use pathlib to join paths
    with open(file_path, 'wb') as file:
        file.write(response.content)
        print(f"Excel data saved to {file_path}")
```

### 6. Process Data and Generate Output

Write functions to read, process, and write results using appropriate Python collections (lists, sets, dictionaries, etc.). Demonstrate understanding of each collection data type's characteristics and usage.

Process the fetched data using appropriate Python collections and generate insightful analytics. The results of the processing should be formatted and written into text files.

Function 1. Process Text Data:
Process text with lists and sets to demonstrate proficiency in working with text files.
Analyze text data to generate statistics like word count, frequency of words, etc., and format these findings into a readable text file.

Function 2. Process CSV Data:
Process CSV files with tuples to demonstrate proficiency in working with tabular data.
Extract and analyze data from CSV files to produce meaningful statistics, summaries, or insights, and save the insights as text files.

Function 3. Process Excel Data:
Extract and analyze data from Excel files to produce meaningful statistics, summaries, or insights, and save the insights as text files.

Function 4. Process JSON Data:
Process JSON data with dictionaries to demonstrate proficiency in working with labeled data.
Parse the JSON data to extract relevant information and present it in a simplified, human-readable text format.

### 7. Implement Exception Handling

We know that reading and writing files - especially fetching items from the web is unreliable.
Even with perfect code, there are many things that can go wrong.
Use try/except/finally and implement exception handling to catch known possible errors and handle them gracefully in at least one of your functions.
For example:

```python
import requests
from pathlib import Path

def fetch_txt_data(folder_name, url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        # Will raise an HTTPError 
        # if the HTTP request returns an unsuccessful status code

        # Assuming the response content is text data
        file_path = Path(folder_name) / 'data.txt'
        with open(file_path, 'w') as file:
            file.write(response.text)
        print(f"Text data saved to {file_path}")

    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")
```

### 8. Main Function

Implement a `main()` function to test the folder creation functions and demonstrate the use of imported modules. For example:

```python
def main():
    ''' Main function to demonstrate module capabilities. '''

    print(f"Name: {yourname_attr.my_name_string}")

    txt_url = 'https://shakespeare.mit.edu/romeo_juliet/full.html'

    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv' 

    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls' 
    
    json_url = 'http://api.open-notify.org/astros.json'

    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls' 
    json_filename = 'data.json' 

    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename,excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename,json_url)

    process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'data.json', 'results_json.txt')

    # Find some data you care about. What format is it? How will you ingest the data?
    # What do you want to extract and write? What export format will you use?
    # Process at least TWO unique data sets and describe your work clearly.
    # Use the README.md and your code to showcase your ability to work with data.

```

### 9. Conditional Script Execution

Ensure the main function only executes when the script is run directly,
not when imported as a module by using standard boilerplate code.

## Module Design

The code should be clear, well-organized, and demonstrate good practices.
Include comments and docstrings for clarity.

## Evaluation Criteria

- Functionality: The project should be functional and meet all requirements.
- Documentation: The project should be well-written and well-documented.
- Presentation: The project should be presented in a clear and organized manner.
- Professionalism: The project should be submitted on-time and reflect an original, creative effort.
