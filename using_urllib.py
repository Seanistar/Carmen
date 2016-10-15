
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

#print(get_page("http://www.google.com"))
words = get_page("http://www.gutenberg.org/cache/epub/1661/pg1661.txt")
print len(words)
