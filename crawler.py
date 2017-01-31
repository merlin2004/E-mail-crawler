import urllib
import re
import sys

depth = 0
mails = set()
sites = []
searched_sites = []
try:
    sites.append(str(sys.argv[1]))
except:
    try:
        sites.append(raw_input("Site: "))
    except:
        print "Site set to https://www.phoenixcontact.com/"
        sites.append("https://www.phoenixcontact.com/")
try:
    depth = int(sys.argv[2])
except:
    try:
        depth = int(input("Depth: "))
    except:
        print "Depth set to 100."
        depth = 100


print ""
print ('\x1b[1;37;41m' + '*********** E-Mail Crawler ************' + '\x1b[0m')
print ('\x1b[1;37;41m' + '****** Hacking is not a crime ! *******' + '\x1b[0m')
print ('\x1b[1;37;41m' + '******      Open your Eyes      *******' + '\x1b[0m')
print ""


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
        # if (m[-4] != "." and m[-5] != "." and m.rfind("/") > -1):
        # i = m.rfind("/")
        # m = m[0:i+1]
        datei = open("blacklist.txt")
        not_allowed = False
        for line in datei:
            if m.endswith(line):
                not_allowed = True
        datei.close()
        if not_allowed is False and m.find("=") == -1 and m.find("?") == -1:
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
            #print "Found site: " + i
            sites.append(i)
            searched_sites.append(i)
print "Searched on " + str(len(searched_sites)) + " sites"
print ('\x1b[5;30;42m' + 'Found mails: ' + str(mails)[3:]  + '\x1b[0m')
