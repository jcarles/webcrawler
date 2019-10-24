from download import download
import re


def crawl_url(url, scrape_callback):
    # download the sitemap file
    sitemap = download(url)
    sitemap = sitemap.decode('ISO-8859-1')  # encoding may vary!

    # extract the sitemap links
    links = re.findall('<FONT style=FONT-SIZE:11pt FACE="Calibri" COLOR=#000000><A HREF=(.*?)>', sitemap)
    # download each link
    for link in links:
        print('http://www.nuforc.org/webreports/'.strip() + link.strip())
        html = download('http://www.nuforc.org/webreports/'.strip() + link.strip())
        # scrape html here
        # ...
        links = []
        if scrape_callback:
            links.extend(scrape_callback(html) or [])
