from urllib.request import urlopen
from bs4 import BeautifulSoup

my_url = 'http://mksclicks.com/videos.php'

# opening up connection and grabbing the html data
connection = urlopen(my_url)
page_html = connection.read()
connection.close()

# html parsing
page_soup = BeautifulSoup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class": "col_one_third"})
print(len(containers))

# extracting the video link and location of shooting
for container in containers:
    link = container.div.div.iframe["src"]
    print(link.lstrip('/'))
    title_container = container.findAll("div", {"class": "fbox-desc"})
    title = title_container[0].h3.span.text.strip()
    print(title)



