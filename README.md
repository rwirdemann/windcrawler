# Windcrawler

Windcrawler provides a set tools for fetching real time wind data.

## Install dependcies

```
pip install -t src/vendor -r aws_requirements.txt
```

## Run tests

```
python3 crawler_test.py
```

## Run locally

```
# Fetch real time wind data at Kiel Leuchturm
python3 crawler.py
```

## Deployment

```
cd pulumi
pulumi up
curl $(pulumi stack output url)
```

## Cleanup

```
cd pulumi
pulumi destroy
pulumi stack rm
```
