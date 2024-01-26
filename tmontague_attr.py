'''Start a data analytics project. '''

import pathlib


def create_project_directory(directory_name): # add type hinting to params
    """
    Creates a project sub-directory.
    :param directory_name: Name of the directory to be created, e.g. "test"
    """
    pathlib.Path(directory_name).mkdir(exist_ok=True)

def create_annual_data_directories(directory_name: str, start_year: int, end_year: int):
    """
    Creates a project sub-directory.
    :param directory_name: Name to be created, e.g. "data"
    :param start: First year to be created, e.g. 2000
    :param end: Last year to be created, e.g. 2024
    """
    create_project_directory(directory_name)
    for year in range(start_year, end_year +1):
        year_directory = pathlib.Path(directory_name).joinpath(str(year))
        create_project_directory(year_directory)
        

def create_pipeline_folders(directory_name:str, folder_list: list):
    """
    Creates a project sub-directory.
    :param director_name: Name to be created, e.g. "pipeline"
    :param folder_list: List of sub-folders to be created, e.g. ['input', input_processed', 'output']
    """
    create_project_directory(directory_name)
    for folder in folder_list:
        folder_directory = pathlib.Path(directory_name).joinpath(folder)
        create_project_directory(folder_directory)

def main():
    """Scaffold a project."""
    create_project_directory('test') # name the parameter
    create_project_directory('docs') # name the parameter
    create_annual_data_directories(directory_name='data', start_year= 2000, end_year=2024) 

    pipeline_folders = ['input','input_processed', 'output' ]
    create_pipeline_folders(directory_name='pipeline', folder_list=pipeline_folders)

tmontague_string = "movie_data_string"


if __name__ == '__main__':
    main()








# Add module block at the bottom

if __name__ == '__main__':
    main()

