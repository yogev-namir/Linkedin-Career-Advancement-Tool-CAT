import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Set up the Selenium WebDriver
driver = webdriver.Chrome()

# Go to the webpage that lists the courses
driver.get('https://www.linkedin.com/learning/search?entityType=COURSE')

# Click the "Sign in" button
sign_in_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.nav__button-secondary"))
)
sign_in_button.click()

time.sleep(30)
# Wait for the initial list of courses to load
wait = WebDriverWait(driver, 5)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ember-view.search-layout__results')))
time.sleep(10)

# Initialize a list to hold all scraped courses
scraped_courses = []

# Initialize a variable to track the previous length of scraped courses
previous_length = 0

# Specify the CSV file name
csv_file_name = 'scraped_courses.csv'

# Define the fieldnames based on the dictionary keys
fieldnames = ['name', 'rank', 'reviews', 'learners']

# Loop to keep scrolling/loading new courses until you reach 10,000
# Scroll to the bottom of the page or click the 'show more' button
# This will depend on how the page loads new content
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

while True:
    try:
        # Attempt to find and click the 'show more' button
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        show_more_button = driver.find_element(By.CSS_SELECTOR, 'button.finite-scroll__load-button')
        show_more_button.click()
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(1)

    except Exception as e:
        pass

    time.sleep(2)
    # Use the CSS selector to find all elements matching the criteria
    courses = driver.find_elements(By.CSS_SELECTOR, "li.search-body__result-card")
    # Process and append new courses dynamically
    for course in courses[len(scraped_courses):]:  # Start from the last known course
        try:
            name = course.find_element(By.CSS_SELECTOR, 'a.entity-link .lls-card-headline').text
        except NoSuchElementException:
            name = None  # or name = ''

        try:
            rank = course.find_element(By.CSS_SELECTOR,
                                       'span.reviews-average-rating > span > span[aria-hidden="true"]').text
        except NoSuchElementException:
            rank = None  # or rank = ''

        try:
            reviews = course.find_element(By.CSS_SELECTOR, 'span.reviews-average-rating span > span:nth-child(3)').text
        except NoSuchElementException:
            reviews = None  # or reviews = ''

        try:
            learners = course.find_element(By.CSS_SELECTOR, 'li.lls-card-meta-list-item .lls-card-viewer-count').text
        except NoSuchElementException:
            learners = None  # or learners = ''

        scraped_courses.append({'name': name,
                                'rank': rank,
                                'reviews': reviews,
                                'learners': learners})

    new_courses = scraped_courses[previous_length:]

    with open(csv_file_name, mode='a', newline='', encoding='utf-8') as file:
        # Create a DictWriter object
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Check if the file is empty to decide on writing headers
        file.seek(0, 2)  # Move to the end of the file
        if file.tell() == 0:  # Check if the file is empty
            # Write the header (the field names) if the file is empty
            writer.writeheader()

        # Write the rows of data
        for course in new_courses:
            writer.writerow(course)

    print(f"Gathered courses: {len(scraped_courses)}")

    if len(courses) == previous_length:
        try:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            show_more_button = driver.find_element(By.CSS_SELECTOR, 'button.finite-scroll__load-button')
            show_more_button.click()
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(1)  # Ensure any new courses have time to load
        except Exception as e:
            # Handle exception if 'show more' button not found or other issues
            pass
        courses = driver.find_elements(By.CSS_SELECTOR, "li.search-body__result-card")

        if len(courses) == previous_length:
            # If the number of courses hasn't increased, stop the loop
            print("No new courses added. Stopping.")
            break

    # Update previous_length for the next iteration
    previous_length = len(courses)

# Close the driver when done
driver.quit()

print(f'Data has been appended to {csv_file_name}')

