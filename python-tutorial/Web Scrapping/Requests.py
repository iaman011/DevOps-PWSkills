# First, we need a way to send a message to the website and fetch its content.
# For this, we import the 'requests' library which allows us to make HTTP requests.
import requests
# (If not installed, you can install it using: pip install requests)

# Next, to help us read and understand the messy HTML content returned by the website,
# we use a library called 'BeautifulSoup' from the 'bs4' module.
from bs4 import BeautifulSoup
# (If not installed, you can install it using: pip install beautifulsoup4)

# 📝 Step 1: Now, we decide which website we want to scrape.
# In this case, it’s a simple site called 'http://quotes.toscrape.com' which displays famous quotes.
url = "http://quotes.toscrape.com"

# Using 'requests.get()', we send a GET request to this URL, and it brings back the webpage's content.
response = requests.get(url)

# 📝 Step 2: The website responds with its HTML content.
# But it’s all mixed up in HTML tags, so we need to parse it.
# We use 'BeautifulSoup' to neatly arrange this content using the 'html.parser'.
soup = BeautifulSoup(response.text, 'html.parser')

# 📝 Step 3: Now comes the treasure hunt part.
# Inside the webpage, quotes are placed within <span> tags having the class 'text'.
# So we search for all such tags and collect them into the 'quotes' list.
quotes = soup.find_all('span', class_='text')

# Similarly, the names of the people who said these quotes are inside <small> tags with class 'author'.
# We collect all these authors into the 'authors' list.
authors = soup.find_all('small', class_='author')

# 📝 Step 4: Time to display our collected treasures.
# Using a loop, we pair each quote with its corresponding author using 'zip()',
# and then print them out nicely one by one.
for quote, author in zip(quotes, authors):
    print(f"{quote.text} - {author.text}")


# Requests + BeautifulSoup can only scrape the static HTML that is sent when the server responds.

# If a website loads extra content via JavaScript after the page loads (like infinite scroll, live notifications, etc.), Requests won’t see those.

