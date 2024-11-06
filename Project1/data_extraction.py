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



Sure! Below is a code structure for performing web scraping using BeautifulSoup and requests in Python. This template provides the basic structure of a web scraping project, from importing necessary libraries to extracting data from a web page.

Step 1: Install Required Libraries
Before starting, ensure you have BeautifulSoup and requests installed. You can install them using pip:

bash
Copier le code
pip install beautifulsoup4 requests
Step 2: Code Structure for Web Scraping
python
Copier le code
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
Step 3: Detailed Breakdown of the Code Structure
Importing Libraries:

requests: Used to make an HTTP request to fetch the HTML content of the web page.
BeautifulSoup: Used to parse and extract data from the HTML content.
Sending an HTTP Request:

requests.get(url) sends an HTTP GET request to the URL and fetches the content of the webpage.
Checking for a Successful Response:

You check if the status_code is 200, which indicates the request was successful. If not, you can handle errors (like retrying the request or logging an error).
Parsing HTML with BeautifulSoup:

BeautifulSoup(response.content, 'html.parser') parses the HTML content from the response. html.parser is the default parser that BeautifulSoup uses.
Extracting Data:

soup.find_all() is used to find multiple elements by their tag names or attributes. For example:
soup.find_all('a'): Extracts all anchor tags (<a>), which are typically used for links.
soup.find_all(['h1', 'h2', 'h3']): Extracts headings with tags <h1>, <h2>, and <h3>.
link.get('href'): Extracts the value of the href attribute, which contains the link URL.
link.get_text(): Extracts the visible text inside the link tag.
Error Handling:

If the request fails (for example, if the page does not exist), it will print an error message with the status code.
Step 4: Customizing the Scraper
You can adapt this basic structure for different tasks. Below are some common modifications:

Example 1: Extracting Images
To extract image URLs (<img> tags):

python
Copier le code
# Find all image tags and print their source URLs
images = soup.find_all('img')
for img in images:
    img_url = img.get('src')
    print(f"Image URL: {img_url}")
Example 2: Extracting Data from Tables
If you want to extract data from tables, you can use:

python
Copier le code
# Find the first table on the page
table = soup.find('table')

# Loop through all rows in the table (ignoring the header)
for row in table.find_all('tr')[1:]:  # Skipping the first row (header)
    cols = row.find_all('td')
    if len(cols) > 0:
        data = [col.get_text(strip=True) for col in cols]  # Extract text from each column
        print(data)
Example 3: Handling Pagination
If the website has pagination (e.g., multiple pages with a "Next" button), you can follow these steps:

Extract the link to the next page (if any).
Make a request to that page.
Repeat the process until all pages have been scraped.
python
Copier le code
# Find the "Next" page link
next_page = soup.find('a', text='Next')  # Modify based on the site's pagination structure
if next_page:
    next_url = next_page.get('href')
    print(f"Next page URL: {next_url}")
    # Continue scraping the next page...
Step 5: Store the Scraped Data
After scraping the data, you might want to save it into a file (like CSV or JSON) for later use.

Example: Save Data to CSV
python
Copier le code
import csv

# Example: Save scraped links to a CSV file
with open('scraped_links.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Link Text", "Link URL"])  # Header row
    for link in links:
        href = link.get('href')
        text = link.get_text()
        writer.writerow([text, href])
Example: Save Data to JSON
python
Copier le code
import json

# Example: Save scraped data as JSON
scraped_data = [{"text": link.get_text(), "url": link.get('href')} for link in links]
with open('scraped_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(scraped_data, json_file, ensure_ascii=False, indent=4)
