import csv
import re
import lxml.html
import urlparse3
from crawl_url import crawl_url


class ScrapeCallback:

    def __init__(self):
        self.writer = csv.writer(open('ufo.csv', 'w'))
        self.fields = ('Date / Time', 'City', 'State', 'Shape',
                       'Duration', 'Summary', 'Posted')
        self.writer.writerow(self.fields)

    def __call__(self, html):
        tree = lxml.html.fromstring(html)
        row = []
        j: int
        tr_elements = tree.xpath('//tr')
        for j in range(1, len(tr_elements)):
            T = tr_elements[j]
            for t in T.iterchildren():
                data = t.text_content()
                print(j)
                row.append(data)
            self.writer.writerow(row)
            row = []

#        for field in self.fields:
# row.append(tree.cssselect('table > tbody > tr > td{1}'.format(field))[0].text_content())
#        self.writer.writerow(row)


if __name__ == '__main__':
    crawl_url('http://www.nuforc.org/webreports/ndxloc.html', scrape_callback=ScrapeCallback())
