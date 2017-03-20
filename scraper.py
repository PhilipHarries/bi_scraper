""" python site scraping tool """

import unicodedata
import requests


def http_get(url):
    """ simple wrapper around http get """
    try:
        request = requests.get(url)
        # not concerned with returning nice utf-8, as only the urls count
        text = unicodedata.normalize('NFKD', request.text
                                     ).encode('ascii', 'ignore')
        return (text, 200)
    except requests.HTTPError as http_error:
        if request.status_code == 404:
            print "{} not found: {}".format(url, http_error)
            return ("", 404)
        else:
            # simplify all other errors as 500's
            print "error retrieving {}: {}".format(url, http_error)
            return ("", 500)


def main():
    """ main function """
    site = "http://wiprodigital.com"

    paths_to_visit = set(["index.html", "index.php"])
    paths_visited = set([])

    for path in paths_to_visit:
        if path not in paths_visited:
            page_url = "{}/{}".format(site, path)
            print "retrieving {}".format(page_url)
            (page, code) = http_get(page_url)
            print page  # process page for new paths
        paths_visited.add(path)


if __name__ == "__main__":
    main()
