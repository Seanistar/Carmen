class WebCrawler:
    def __init__(self):
        pass

    def get_page(self, url):
        try:
            import urllib
            return urllib.urlopen(url).read()
        except:
            return ""
    
    def get_next_target(self, page):
        start_link = page.find('<a href=')
        if start_link == -1:
            return None, 0
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote
    
    def get_all_links(self, page):
        links = []
        while True:
            url, endpos = self.get_next_target(page)
            if url:
                links.append(url)
                page = page[endpos:]
            else:
                break
        return links

    def union(self, p, q):
        for e in q:
            if e not in p:
                p.append(e)
                
    def crawl_web(self, seed):
        tocrawl = [seed]
        crawled = []
        while tocrawl:
            page = tocrawl.pop()
            if page not in crawled:
                content = self.get_page(page)
                self.union(tocrawl, self.get_all_links(content))
                crawled.append(page)
        return crawled

    def crawl_index(self, seed):
        tocrawl = [seed]
        crawled = []
        index = {}
        graph = {}
        while tocrawl:
            page = tocrawl.pop()
            if page not in crawled:
                content = self.get_page(page)
                self.add_page_to_index(index, page, content)
                outlinks = self.get_all_links(content)
                graph[page] = outlinks
                self.union(tocrawl, outlinks)
                crawled.append(page)
        return index, graph
    
    def add_page_to_index(self, index, url, content):
        words = content.split()
        for word in words:
            self.add_to_index(index, word, url)

    def add_to_index(self, index, keyword, url):
        '''for entry in index:
            if entry[0] == keyword:
                entry[1].append(url)
                return
        index.append([keyword, [url]])'''
        if keyword in index:
            index[keyword].append(url)
        else:
            index[keyword] = [url]

    def lookup(self, index, keyword):
        if keyword in index:
            return index[keyword]
        else:
            return None

    def compute_ranks(self, graph):
        d = 0.8
        numloops = 10

        ranks = {}
        npages = len(graph)
        for page in graph:
            ranks[page] = 1.0 / npages

        for i in range(0, numloops):
            newranks = {}
            for pgae in graph:
                newrank = (1 - d) / npages
                for node in graph:
                    if page in graph[node]:
                        newrank = newrank + d * (ranks[node] / len(graph[node]))
                newranks[page] = newrank
            ranks = newranks
        return ranks
