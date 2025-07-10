# Importing the BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup

# Command to install the library in terminal :
# pip install beautifulsoup4

# Defining a multi-line string that contains HTML content (a simple web page)
html_doc = """
# web page 
# This is a static scraping approach because it only fetches the initial HTML content of the website.
# Any dynamic content loaded by JavaScript after the page loads (like live updates or interactive data) won't be visible here.
<html>
<head>
<title>My Page</title>
</head>
<body>

<h1>Welcome to My Page</h1>

<p class='content'> This is a paragraph.</p>

<a href="http://example.com">Example Link</a>
</body>
</html>
"""

# Creating a BeautifulSoup object to parse the HTML content and passing the variable html_doc
soup1 = BeautifulSoup(html_doc, 'html.parser') #html.parser is used to parse the html document

# Accessing and printing the <title> tag from the HTML document
print(soup1.body)
