""" html parser for buildit code test """
import HTMLParser
import re


class BuildItParser(HTMLParser.HTMLParser):
    """ extra link information """

    def __init__(self, regex):
        """ initialise object """
        HTMLParser.HTMLParser.__init__(self)
        self.regex = regex
        self.ext_links = set([])
        self.int_links = set([])
        self.static_links = set([])

    def handle_starttag(self, tag, attrs):
        """ handle start tags for links and images """
        if tag == "a":
            for (attrib, value) in attrs:
                if attrib == "href":
                    # need to check if an internal link
                    int_path = self.regex.search(value)
                    if int_path is not None:
                        int_path = int_path.group(1)
                        self.int_links.add(int_path)
                    else:
                        # an external link
                        if not (re.match(r"^mailto:", value) or
                                re.match(r"^#", value)):
                            self.ext_links.add(value.encode('ascii', 'ignore'))
        elif tag == "img":
            for (attrib, value) in attrs:
                if attrib == "src":
                    self.static_links.add(value)
