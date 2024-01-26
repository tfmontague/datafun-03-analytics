'''tmontague_analytics_py 

Python module for fetching, processing, and writing data.
This module demonstrates handling different data types from web sources.
'''

#Import Dependencies
# Standard library imports
import csv
import json
import pathlib
import pandas as pd
from collections import Counter

# External library imports (requires virtual environment)
import requests  

# Local module imports
import tmontague_attr
import tmontague_projsetup

# Data Acquisition - fetch data from specified web APIs or online data sources.
import requests

# Fetch and save text data
def fetch_and_write_txt_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_txt_file(folder_name, filename, response.text)
    except requests.RequestException as e:
        print(f"Error fetching text data: {e}")

# Fetch and save csv data
def fetch_and_write_csv_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_csv_file(folder_name, filename, response.content.decode('utf-8'))
    except requests.RequestException as e:
        print(f"Error fetching CSV data: {e}")

# Fetch and save excel data
def fetch_and_write_excel_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_excel_file(folder_name, filename, response.content)
    except requests.RequestException as e:
        print(f"Error fetching Excel data: {e}")

#Fetch and save JSON data
def fetch_and_write_json_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_json_file(folder_name, filename, response.json())
    except requests.RequestException as e:
        print(f"Error fetching JSON data: {e}")


#Write Data - write functions to save content to different file types
from pathlib import Path

#Function 1. Process Text Data
def write_txt_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name, filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")

#Function 2. Process CSV Data
def write_csv_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name, filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w', newline='', encoding='utf-8') as file:
        file.write(data)
        print(f"CSV data saved to {file_path}")

#Function 2. Process Excel Data
def write_excel_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name, filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'wb') as file:
        file.write(data)
        print(f"Excel data saved to {file_path}")


#Function 4. Process JSON Data
def write_json_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name, filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w') as file:
        json.dump(data, file, indent=4)
        print(f"JSON data saved to {file_path}")

#Process data and generate output - also includes exception handling
def process_txt_data(input_file, output_file):
    # Count occurences of each word in movies data
    try:
        with open(input_file, 'r') as file:
            text = file.read()
        words = text.split()
        word_count = Counter(words)

        with open(output_file, 'w') as file:
            for word, count in word_count.items():
                file.write(f"{word}: {count}\n")
        print(f"Word count saved to {output_file}")
    except Exception as e:
        print(f"Error processing text data: {e}")

def process_csv_data(input_file, output_file):
    # Calculate the average Audience Score % and Profitability from the 2007-2011 movie list.
    try:
        df = pd.read_csv(input_file)

        # Ensure columns 'Audience Score %' and 'Profitability' exist in your CSV
        average_audience_score = df['Audience score %'].mean()
        average_profitability = df['Profitability'].mean()

        with open(output_file, 'w') as file:
            file.write(f"Average Audience Score %: {average_audience_score}\n")
            file.write(f"Average Profitability: {average_profitability}\n")

        print(f"Averages saved to {output_file}")
    except Exception as e:
        print(f"Error processing CSV data: {e}")

def process_excel_data(input_file, output_file):
    try:
        df = pd.read_excel(input_file)
        # Sort list of top-grossing 2020 movies from highest to lowest
        sorted_df = df.sort_values('Domestic Gross', ascending=False)
        sorted_output_file = output_file.replace('.txt', '.xlsx')
        sorted_df.to_excel(sorted_output_file, index=False)
        print(f"Data sorted by Domestic Gross and saved to {sorted_output_file}")
    except Exception as e:
        print(f"Error processing Excel data: {e}")

def process_json_data(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)
        #Parsed genres of 1980s movies
        with open(output_file, 'w') as file:
            for title in data:
                genres = title.get('genres', [])
                file.write(f"{title['title']}: {', '.join(genres)}\n")
        
        print(f"Genres extracted and saved to {output_file}")
    except Exception as e:
        print(f"Error processing JSON data: {e}")



#Main Function - Implement a main() function to test the folder creation functions and demonstrate the use of imported modules.
def main():
    """Main functions to implement a main() function to test the folder creation functions and demonstrate the use of imported modules ."""

    print(f"Name: {tmontague_attr.tmontague_string}")

    # URLs for different data types
    txt_url = 'https://raw.githubusercontent.com/jtleek/modules/master/01_DataScientistToolbox/01_01_seriesMotivation/data/movies.txt'
    csv_url = 'https://gist.githubusercontent.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea/raw/0c794a9717f18b094eabab2cd6a6b9a226903577/movies.csv'
    excel_url = 'https://github.com/parulnith/Data-Visualisation-libraries/raw/master/Data%20Visualisation%20with%20Tableau/Wordclouds%20with%20Tableau/movies.xlsx'
    json_url = 'https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies-1980s.json'

    # Folder and file names for different data types
    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel'
    json_folder_name = 'data-json'

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xlsx'
    json_filename = 'data.json'

    # Fetch and write data for all types
    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename, json_url)

    # Process data for all types
    process_txt_data(pathlib.Path(txt_folder_name, txt_filename), 'result_txt.txt')
    process_csv_data(pathlib.Path(csv_folder_name, csv_filename), 'result_csv.txt')
    process_excel_data(pathlib.Path(excel_folder_name, excel_filename), 'result_excel.txt')
    process_json_data(pathlib.Path(json_folder_name, json_filename), 'result_json.txt')

# Conditional Script Execution

if __name__ == "__main__":
    main()
