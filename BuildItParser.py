""" html parser for buildit code test """
import HTMLParser


class BuildItParser(HTMLParser.HTMLParser):
    """ extra link information """

    def __init__(self):
        """ initialise object """
        HTMLParser.HTMLParser.__init__(self)
        self.ext_links = set([])
        self.int_links = set([])
        self.static_links = set([])

    def handle_starttag(self, tag, attrs):
        """ handle start tags for links and images """
        if tag == "a":
            for (attrib, value) in attrs:
                if attrib == "href":
                    # need to check if an internal link
                    self.ext_links.add(value)
        elif tag == "img":
            for (attrib, value) in attrs:
                if attrib == "src":
                    self.static_links.add(value)
