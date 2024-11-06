# Find all image tags and print their source URLs
images = soup.find_all('img')
for img in images:
    img_url = img.get('src')
    print(f"Image URL: {img_url}")

# Find the first table on the page
table = soup.find('table')

# Loop through all rows in the table (ignoring the header)
for row in table.find_all('tr')[1:]:  # Skipping the first row (header)
    cols = row.find_all('td')
    if len(cols) > 0:
        data = [col.get_text(strip=True) for col in cols]  # Extract text from each column
        print(data)


# Find the "Next" page link
next_page = soup.find('a', text='Next')  # Modify based on the site's pagination structure
if next_page:
    next_url = next_page.get('href')
    print(f"Next page URL: {next_url}")
    # Continue scraping the next page...


# Example: Save scraped links to a CSV file
with open('scraped_links.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Link Text", "Link URL"])  # Header row
    for link in links:
        href = link.get('href')
        text = link.get_text()
        writer.writerow([text, href])

import requests
from bs4 import BeautifulSoup

# Step 1: Send an HTTP request to the webpage
url = 'https://example.com'  # Replace with the target URL
response = requests.get(url)

# Step 2: Check if the request was successful
if response.status_code == 200:
    # Step 3: Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Step 4: Extract data from the parsed HTML
    # Example: Extract all the links from the page
    links = soup.find_all('a')  # Find all anchor tags (links)
    
    for link in links:
        href = link.get('href')  # Get the value of the href attribute
        text = link.get_text()  # Get the text inside the link
        print(f"Link Text: {text}, Link URL: {href}")
    
    # Example: Extracting all headings (h1, h2, h3, etc.)
    headings = soup.find_all(['h1', 'h2', 'h3'])  # Find h1, h2, and h3 tags
    for heading in headings:
        print(f"Heading: {heading.get_text()}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

BeautifulSoup(response.content, 'html.parser') parses the HTML content from the response. html.parser is the default parser that BeautifulSoup uses.
Extracting Data:

soup.find_all() is used to find multiple elements by their tag names or attributes. For example:
soup.find_all('a'): Extracts all anchor tags (<a>), which are typically used for links.
soup.find_all(['h1', 'h2', 'h3']): Extracts headings with tags <h1>, <h2>, and <h3>.
link.get('href'): Extracts the value of the href attribute, which contains the link URL.
link.get_text(): Extracts the visible text inside the link tag.
Error Handling:

# Find all image tags and print their source URLs
images = soup.find_all('img')
for img in images:
    img_url = img.get('src')
    print(f"Image URL: {img_url}")

table = soup.find('table')

# Loop through all rows in the table (ignoring the header)
for row in table.find_all('tr')[1:]:  # Skipping the first row (header)
    cols = row.find_all('td')
    if len(cols) > 0:
        data = [col.get_text(strip=True) for col in cols]  # Extract text from each column
        print(data)


# Find the "Next" page link
next_page = soup.find('a', text='Next')  # Modify based on the site's pagination structure
if next_page:
    next_url = next_page.get('href')
    print(f"Next page URL: {next_url}")
    # Continue scraping the next page...

import csv

# Example: Save scraped links to a CSV file
with open('scraped_links.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Link Text", "Link URL"])  # Header row
    for link in links:
        href = link.get('href')
        text = link.get_text()
        writer.writerow([text, href])

import json

# Example: Save scraped data as JSON
scraped_data = [{"text": link.get_text(), "url": link.get('href')} for link in links]
with open('scraped_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(scraped_data, json_file, ensure_ascii=False, indent=4)
