''' P2: Scripting Project Organization: This module provides functions for creating a series of project folders. '''

#import dependencies
import math
import statistics
import time
import pathlib
import mont_analytics_utils

#function 1 - For item in Range: Create a function to generate folders for a given range (e.g., years).
def create_folders_for_range(start, end):
    """Create a function to generate folders for a given range (e.g., years)
    
    :param start: First year to be created, e.g. 2000
    :param end: Last year to be created, e.g. 2024

    :returns: A list of created folder paths
    """
    folders = []
    for year in range(start, end):
        folder_path = pathlib.Path(f"{year}")
        folder_path.mkdir(exist_ok=True)
        folders.append(str(folder_path))
    return folders

#function 2 - For Item in List: Develop a function to create folders from a list of names.
def create_folders_from_list(folder_list, to_lowercase=False, remove_spaces=False):
    """Create folders from a list of names.
    
    param: folder_list: List of folder names to be created.
    param: to_lowercase: Convert folder names to lowercase if True.
    param: remove_spaces: Remove spaces from folder names if True.
    
    returns: list of created folder paths
    """
    folders = []
    for name in folder_list:
        if to_lowercase:
            name = name.lower()
        if remove_spaces:
            name = name.replace(" ", "")
        folder_path = pathlib.Path(name)
        folder_path.mkdir(exist_ok=True)
        folders.append(str(folder_path))
    return folders

#function 3 - List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
def create_prefixed_folders(folder_list, prefix):
    """Create prefixed folders
    
    param: folder_list: List of folder names to be created.
    param: prefix: Prefix to be added to each folder name.
    
    returns: list: 
    """
    return create_folders_from_list([f"{prefix}{name}" for name in folder_list])

#function 4 - While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
def create_folders_periodically(duration):
    """Create folders periodically every 5 seconds for a specified duration.
    
    param:  duration (int): Duration in seconds for which the folders will be created.
    
    returns: A list of created folder paths.
    """
    start_time = time.time()
    folders = []
    counter = 0
    while time.time() - start_time < duration:
        folder_name = f"PeriodicFolder_{counter}"
        folder_path = pathlib.Path(folder_name)
        folder_path.mkdir(exist_ok=True)
        folders.append(str(folder_path))
        print(f"Folder created: {folder_path}")
        time.sleep(5) #wait for 5 seconds before creating the next folder
        counter += 1

def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f"Byline: {mont_analytics_utils.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start=2020, end=2023)

    # Call function 2 to create folders given a list
    folder_list = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_list)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

# Conditional Script Execution
"""Ensure the main function only executes when the script is run directly, not when imported as a module by using standard boilerplate code."""

if __name__ == '__main__':
    main()

