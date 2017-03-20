# bi_scraper
BuildIT demo scraper

# how to run
To run the demo scraper, simply run ./run.sh

 - this assumes that you are running on a unix system with python and virtualenv installed
 - if this is not the case, you will need a python environment with the requirements listed in requirements.txt

# outstanding issues
 - the scraper does not know that urls that end in / may be the same as those that do not:
   - i.e. http://example.com/links and http://example.com/links/
 - the scraper does not account for url fragments and anchors
   - http://example.com/index.html#anchor1 will be listed as a different page to index.html#anchor2 or index.html
   - http://example.com/something.php?x=y will appear as a different link to http://example.com/something.php?a=b
 - sites that have http and https presences are likely to be indexed poorly
 - relative links "/blog.html" are not correctly identified as internal links
 - the scraper should take a parameter of which site to index
 - configurable output would be nice
 - tests were omitted in order to complete in a timely manner - they would need to be urgently added
 - it would be nice to track broken links / 404 / 500's
 - redirects are followed uncritically, and appear as additional entries to the structure
 - (provision has been made to capture http codes, so the last points should be easy to add)

# assumptions
 - sites can be crawled by initially starting at index.html or index.php
 - robots.txt can be ignored
 - if a sitemap is present, it can be found at sitemap.xml
