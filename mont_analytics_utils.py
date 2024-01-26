''' This module provides a reusable byline for Montague Analytics' projects. '''

# importing dependencies
import math
import statistics

# defining variables
business_name: str = "Montague Analytics, LLC"
count_completed_projects: int = 3
is_veteran_owned: bool = True
average_google_rating: float = 4.7
project_types: list = ["Data Analysis", "Data Strategy", "Data Platform Solution Design", "Business Analysis", "Data Governance Consulting"]
google_rating_scores: list = [4.4, 5.0, 4.8]

# defining formatted strings
completed_projects_string: str = f"Completed Projects: {count_completed_projects}"
veteran_owned_string: str = f"Veteran Owned: {is_veteran_owned}"
google_rating_string: str = f"Average Google Rating: {average_google_rating}"
project_types_string: str = f"Project Types: {', '.join(project_types)}"

# calculating descriptive statistics
lowest = min(google_rating_scores)
highest = max(google_rating_scores)
total = sum(google_rating_scores)
count = len(google_rating_scores)
mean = statistics.mean(google_rating_scores)
mode = statistics.mode(google_rating_scores)
median = statistics.median(google_rating_scores)
standard_deviation = statistics.stdev(google_rating_scores)

stats_string: str = f"""
Descriptive Statistics for Our Google Rating Scores:
  Lowest: {lowest}
  Highest: {highest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""

# defining byline string
byline: str = f"""
{business_name}
{completed_projects_string}
{veteran_owned_string}
{google_rating_string}
{project_types_string}
{stats_string}
"""

# defining main function
def main():
    ''' Display all output '''
    print(business_name)
    print(completed_projects_string)
    print(veteran_owned_string)
    print(google_rating_string)
    print(project_types_string)
    print(stats_string)

    # If all of the above works, then the byline should work too:
    print(byline)

# conditions
if __name__ == '__main__':
    main()