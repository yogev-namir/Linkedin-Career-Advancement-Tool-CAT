# import pandas as pd
#
# # Read the CSV into a DataFrame
# df = pd.read_csv('scraped_courses.csv', encoding='utf-8')
#
# # Display the first few rows of the DataFrame to confirm
# print(df.head())

import pandas as pd
import re

# Load the CSV file into a DataFrame
# Replace 'path_to_your_csv_file.csv' with the actual path to your CSV file
df = pd.read_csv('job_skills.csv', encoding='utf-8')

# Define a function to extract the job title and publisher from a LinkedIn URL
def extract_info_from_url(url):
    # Regex to match the pattern in the URL
    match = re.search(r'linkedin\.com/jobs/view/(.+?)-at-(.+?)-\d+', url)
    if match:
        # Replace hyphens with spaces and capitalize for the job title
        job_title = match.group(1).replace('-', ' ').title()
        # Replace hyphens with spaces and capitalize for the publisher
        publisher = match.group(2).replace('-', ' ').title()
        return job_title, publisher
    else:
        return 'Not Found', 'Not Found'

# Assuming the URL is in the first column and skills in the second
df['Job Title'], df['Publisher'] = zip(*df.iloc[:, 0].apply(extract_info_from_url))

# Select only the relevant columns to keep: 'Job Title', 'Publisher', and 'job_skills'
df = df[['Job Title', 'Publisher', 'job_skills']]

# Save the result back to a new CSV file if needed
df.to_csv('job_skills_parsed.csv', index=False)

# Display the DataFrame
print(df)
