import tldextract

with open('domains.txt','r') as f:
    lines=f.readlines()
    for line in lines:
        ext = tldextract.extract(line.strip())
        print(ext.domain + '.' + ext.suffix)
