import urllib
import re
import sys

depth = 20
mails = set()
sites = []
searched_sites = []
try:
    sites.append(str(sys.argv[1]))
except:
    try:
        sites.append(raw_input("Site: "))
    except:
        print "Site set to https://github.com/mircotroue/"
        sites.append("https://github.com/mircotroue/")
try:
    depth = int(sys.argv[2])
except:
    try:
        depth = int(input("Depth: "))
    except:
        print "Depth set to 20."
        depth = 20


def find_mails(string):
    patt = r"( [-.\w]+?@[-.\w]+?\.\w+ |mailto:[-.\w]+?@[-.\w]+?\.\w+)"
    res = []
    for match in re.finditer(patt, string):
        m = match.group()
        m = m.replace(" ", "")
        m = m.replace("mailto:", "")
        print "\t Found mail: " + m
        res.append(m)
    return res


def find_sites(string):
    patt = r"( http://[-.\w]+?\.\w+? | https://[-.\w]+?\.\w+? | www\.[-.\w]+?\.\w+? |href=\"http://.*?\")"
    res = []
    for match in re.finditer(patt, html):
        m = match.group()
        m = m.replace(" ", "")
        m = m.replace("href=\"", "")
        m = m.replace("\"", "")
        if (m[-4] != "." and m[-5] != "." and m.rfind("/") > -1):
            i = m.rfind("/")
            m = m[0:i+1]
        res.append(m)
    return res

print "Searching mails at " + sites[0] + " with " + str(depth) + " child sites"
while len(sites) > 0:
    site = sites.pop()
    try:
        html = urllib.urlopen(site).read()
    except:
        html = ""
    i = html.find("</head>")
    if i > -1:
        html = html[i+7:]
    mails.update(find_mails(html))
    current_links = find_sites(html)
    for i in current_links:
        if (i not in sites) and (i not in searched_sites) and len(searched_sites) < depth:
            print "Found site: " + i
            sites.append(i)
            searched_sites.append(i)
print "Searched on " + str(len(searched_sites)) + " sites"
print "Found mails: " + str(mails)[3:]
