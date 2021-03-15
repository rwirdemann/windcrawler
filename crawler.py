import requests
from bs4 import BeautifulSoup

url = 'https://www.geomar.de/service/wetter'


def get_url_content():
    return requests.get(url).text


def get_blog_content():
    content = get_url_content()
    soup = BeautifulSoup(content, "html.parser")

    rows = get_rows(soup, 'Leuchtturm')

    if rows is not None:
        output = '%s %s: ' % (rows.label, rows.timestamp)
        for r in rows.value:
            cols = r.findAll('td')
            if len(cols) > 1:
                k = cols[0].text.strip()
                v = cols[1].text.strip()
                if k == 'Windrichtung' or k == 'Windgeschwindigkeit':
                    output = '%s %s: %s' % (output, k, v)
        print(output)


class Rows:
    label = ''
    timestamp = None
    value = []

    def __init__(self, label, timestamp, value):
        self.label = label
        self.timestamp = timestamp
        self.value = value


def get_rows(soup, table):
    overview = soup.find('div', {'class': 'weather-list__overview'})
    tables = overview.findAll('table')
    for t in tables:
        head = t.find('thead')
        headers = head.findAll('th')
        if len(headers) > 1:
            ts = headers[0].text.strip()
            label = headers[1].text.strip()
            if label == table:
                return Rows(label, ts, t.findAll('tr'))


get_blog_content()
