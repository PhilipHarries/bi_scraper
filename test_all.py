import re
from scraper import process_html
from BuildItParser import BuildItParser


def test_process_html_no_links():
    html = "<html><body></body></html>"
    test_regex = re.compile(r"{}(.+)$".format("http://www.test.com/"))
    parser = BuildItParser(test_regex)
    parse_object = process_html(html, parser)
    assert len(parse_object["int_links"]) == 0
    assert len(parse_object["ext_links"]) == 0
    assert len(parse_object["static_links"]) == 0


def test_process_html_only_ext_links():
    html = "<html><body><a href=\"http://www.google.com/\"></body></html>"
    test_regex = re.compile(r"{}(.+)$".format("http://www.test.com/"))
    parser = BuildItParser(test_regex)
    parse_object = process_html(html, parser)
    # assert len(parse_object["int_links"]) == 0
    # assert len(parse_object["ext_links"]) == 1
    assert len(parse_object["static_links"]) == 0
