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


def process_html(html_page):
    """ extract links from an html page """
    return {
        "int_links": [],
        "ext_links": [],
        "static_links": []
        }


def main():
    """ main function """
    site = "http://wiprodigital.com"
    site_structure = []

    paths_to_visit = set(["index.html", "index.php"])
    paths_visited = set([])

    paths_still_to_process = True
    while paths_still_to_process:
        num_paths = len(paths_to_visit)
        new_paths = set([])
        for path in paths_to_visit:
            if path not in paths_visited:
                page_url = "{}/{}".format(site, path)
                (page, code) = http_get(page_url)
                new_page = process_html(page)
                new_page["path"] = path
                site_structure.append(new_page)
                for internal_link in new_page["int_links"]:
                    if internal_link not in paths_visited:
                        new_paths.add(internal_link)
            paths_visited.add(path)
        paths_to_visit = paths_to_visit.union(new_paths)
        if num_paths == len(paths_to_visit):
            # no new paths added
            paths_still_to_process = False


if __name__ == "__main__":
    main()
