import requests
import json


def test_Dexcom_API():
    url = 'https://clarity.dexcom.com/api/subject/1594950620847472640/analysis_session'

    # header
    headers = {
        'Access-Token': '' #need fresh token after login
    }

    # Body
    payload = {}

    # Request
    resp = requests.post(url, headers=headers, data=payload)

    # Validate
    resp_body = resp.json()
    assert resp_body['analysisSessionId'] is not None
