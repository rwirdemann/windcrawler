from crawler import parse
import sys
sys.path.insert(0, 'src/vendor')
import requests

url = 'https://www.geomar.de/service/wetter'


def handler(event, context):
    content = requests.get(url).text
    out = parse(content)
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': out
    }