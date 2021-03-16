import sys
sys.path.insert(0, 'src/vendor')
import requests
from parser import parse


url = 'https://www.geomar.de/service/wetter'

if __name__ == '__main__':
    content = requests.get(url).text
    (label, ts, direction, speed) = parse(content)
    print(label, ts, direction, speed)