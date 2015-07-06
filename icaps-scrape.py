
PROCEEDINGS = {
    'icaps03': (2003,"http://dblp.uni-trier.de/db/conf/aips/icaps2003.html"),
    'icaps04': (2004,"http://dblp.uni-trier.de/db/conf/aips/icaps2004.html"),
    'icaps05': (2005,"http://dblp.uni-trier.de/db/conf/aips/icaps2005.html"),
    'icaps06': (2006,"http://dblp.uni-trier.de/db/conf/aips/icaps2006.html")
}

import scholar, urllib2, csv, random, time

try:
    from bs4 import BeautifulSoup
except ImportError:
    try:
        from BeautifulSoup import BeautifulSoup
    except ImportError:
        print('We need BeautifulSoup, sorry...')
        sys.exit(1)

# Javascript command to copy all of the titles from the dblp page.
# copy($.map($('.title').contents(), function (n,i) {return n.textContent}))

def gen_csv(conf, csv_file):
    
    print "\nWorking with conference %s" % conf
    
    page=urllib2.urlopen(PROCEEDINGS[conf][1])
    soup = BeautifulSoup(page.read())
    
    #data = [['Result', 'Title', 'URL', 'Year', 'Citations', 'Versions', 'Cluster ID', 'PDF Link', 'Citations list', 'Versions list']]
    data = [['Result', 'Title', 'URL', 'Year', 'Citations', 'Versions', 'Cluster ID']]
    for title in map(lambda x: x.string, soup.findAll('span',{'class':'title'})):
        print "Searching for \"%s\"" % title
        year = str(PROCEEDINGS[conf][0])
        
        # Pause to try and avoid Scholar Limits
        time.sleep(1 + random.random() * 2)
        
        scholar.main(['--cookie-file', 'random-cookie', '--after', year, '--before', year, '-t', '-c', '3', '-p', title], data)
    
    with open(csv_file, 'wb') as f:
        writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for d in data:
            writer.writerow(d)

#gen_csv('icaps03', 'icaps03.csv')
#gen_csv('icaps04', 'icaps04.csv')
#gen_csv('icaps05', 'icaps05.csv')
#gen_csv('icaps06', 'icaps06.csv')
