from parser import parse
import json
import sys
sys.path.insert(0, 'src/vendor')
import requests 

url = 'https://www.geomar.de/service/wetter'


def handler(event, context):
    content = requests.get(url).text
    (label, ts, direction, speed) = parse(content)
    result = {
        'spot': label,
        'timestamp': ts,
        'direction': direction,
        'speed': speed 
    }

    return {        
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(result, ensure_ascii=False)
    }