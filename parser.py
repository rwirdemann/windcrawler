import sys
sys.path.insert(0, 'src/vendor')
from bs4 import BeautifulSoup


url = 'https://www.geomar.de/service/wetter'


def parse(html):
    """Parses the given html and returns a tuple of weather information for a specific location.
    """
    soup = BeautifulSoup(html, "html.parser")

    (label, ts, rows) = get_rows(soup, 'Leuchtturm')
    if rows is not None:
        output = '%s %s: ' % (label, ts)
        for r in rows:
            cols = r.findAll('td')
            if len(cols) > 1:
                k = cols[0].text.strip()
                v = cols[1].text.strip()
                if k == 'Windrichtung':
                    direction = v                
                if k == 'Windgeschwindigkeit':
                    speed = v
        return (label, ts, direction, speed)


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
                return (label, ts, t.findAll('tr'))