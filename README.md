# ICAPS-Citation-Count
Scrapes Google Scholar for the citation count of all papers at a particular ICAPS conference (given the DBLP page for the conference proceedings).

## Usage
Uncomment at least one of the `gen_csv` lines in icaps-scrape.py and execute the file. Add more years, as necessary, at the top of the file.

## Notes
* The **Result** column is one of the following:
  * `SINGLE` if only one result is returned (expected)
  * `MULTI` for multiple results (should be manually verified to get the citation count)
  * `NONE` if for some reason the title returns nothing on Google Scholar
* Use the paper URL to get a sense if the right paper was found (many URLs should point to the AAAI library)
* The script requires [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)
* If you open the CSV in a spreadsheet application, | is used as the text delimiter (for title's with commas)
* Google Scholar seems to limit the queries that can be performed. The use of a cookie tries to side-step this, but it doesn't always work. You may need to run the script for different years on different machines or reconnect to a VPN. There shouldn't be any issue pulling down one full year at a time though.
* The scholar.py file is a modified version of [this project](https://github.com/ckreibich/scholar.py).

