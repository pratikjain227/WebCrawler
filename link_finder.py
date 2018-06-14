from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = "http://www.mksclicks.com"
        self.page_url = page_url
        self.links = set()

# abstract method
    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(value)
        print(self.links)


finder = LinkFinder("abc", "abc")
finder.feed('<a href = "www.mksclicks.com"></a>')
