# Valtix POV Test Runner

This repo contains python scripts that can be run automated tests to validate the security functionality of the Valtix Security Service

## Getting Started

1. Clone this repo
2. Setup a virtual environment - ` python -m venv .venv`
3. Activate the virtual environment - `source .venv/bin/activate`
4. pip install the requirements - ` pip install -r requirements.txt`
5. Run test harness - `python ./egress.py` or `python ./ingress.py`

## Ingress Tests Included

- waf phpinject1-933100
- waf phpinject2-933120
- waf localfileexec1-930120
- waf localfileexec2-930120
- waf remotefileexec-931100
- waf remotecodeexec-932100
- waf xss-941310
- waf xss2-941310
- waf sqlinjection-942140
- waf sqlinjection2-942220
- waf sessionfixation-943100
- waf sessionfixation2-943120
- waf httpheaderinjection
- waf httpheaderinjection2-921160
- waf av
- waf httpresponsesplitting-921120
- waf httpresponsesplitting2-921120
- ids zip
- ids pdf
- ids solarwinds-nt1
- ids solarwinds-nt2
- ids nt3
- ids nt4
- l7dos L7Dos

## Egress Tests Included

- url-filtering block-github-test-repo
- fqdn-filtering block-news
- dlp dlp-block-ssn
- dlp dlp-us-phone
- ids cnc
- cnc nt1
- cnc solarwinds-nt2
- DLP PII Send US Phone Number
- DLP PII US Social Security
- DLP PII US Bank Routing Numbers
- DLP PII RSA Key
- DLP PII AWS Access Key

## Changelog

9.20 Added `requirements.txt`

9.14. Added East-West Testing

7.27 changes

- updated webrequest to handle connection reset and other exceptions
- added siege for L7DoS testing
