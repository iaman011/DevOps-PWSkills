import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone"

response = requests.get(url)

if response.status_code == 200:
    soup1 = BeautifulSoup(response.text, 'html.parser')

    products = soup1.find_all('div', class_ = 'thumbnail')

    for product in products:
        title_tag = product.find('a', class_ = 'title')
        name = title_tag.text.strip()
        link = "https://webscrapper.io" + title_tag.get('href')

        price = product.find('h4', class_='price').text.strip()
        desc = product.find('p', class_ ='description').text.strip()

        print(f"Name: {name}")
        print(f"Price: {price}")
        print(f"Description: {desc}")
        print(f"Link: {link}")
        print("-"*50)

else:
    print("Failed to fetch the website")
    

'''
📌 How to Know What Structure to Use in Web Scraping:
📖 Step-by-Step Approach:
Step 1️⃣: Inspect the Website’s HTML Structure
Open the website you want to scrape.

Right-click on the element you want to extract (like product name, price, etc.)

Select Inspect (in Chrome, Edge, Firefox).

This opens the Developer Tools panel showing the HTML source code of the page.

Step 2️⃣: Identify the Relevant Tags and Classes
Look at the HTML structure around your target data.

Find the HTML tag (like a, h4, p) and class name (like title, price, description) for each data point you need.

Example from your case:

html
Copy
Edit
<div class="caption">
    <a class="title" href="/test-sites/e-commerce/allinone/product/531">Product Name</a>
    <h4 class="price">$100.00</h4>
    <p class="description">This is the product description.</p>
</div>
You see:

Product Name: inside an <a> tag with class="title"

Price: inside an <h4> tag with class="price"

Description: inside a <p> tag with class="description"

Step 3️⃣: Build the Scraping Code Based on the HTML Structure
Now, in Python with BeautifulSoup:

python
Copy
Edit
# Find the title tag
title_tag = product.find('a', class_='title')

# Extract the text from the title tag and clean it
name = title_tag.text.strip()

# Build the link by joining the base URL with the href attribute value
link = "https://webscraper.io" + title_tag.get('href')

# Similarly, find the price and description
price = product.find('h4', class_='price').text.strip()
desc = product.find('p', class_='description').text.strip()
Why this works:
Because you carefully matched your scraping queries with the actual tags and classes present in the website’s HTML.

Step 4️⃣: Test and Adjust
Run your scraper.

If it works, great.

If the website structure changes (like class names or tags), you might need to inspect again and adjust your scraping selectors.

📌 Summary of Approach:
Step	Action
1	Open website and use Inspect Element
2	Find HTML tags and their classes/ids
3	Write BeautifulSoup find/find_all calls accordingly
4	Test, debug, and refine

📌 Bonus Tip:
You can also use CSS Selectors or XPath for more advanced targeting, especially when classes are missing or inconsistent.

✅ Conclusion:
We decide this code structure by inspecting the web page’s HTML structure and mapping our BeautifulSoup queries to the exact tags and classes where the data lives.


'''