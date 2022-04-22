import requests
import json


def test_Dexcom_API():
    url = 'https://clarity.dexcom.com/api/subject/1594950620847472640/analysis_session'

    # header
    headers = {
        'Access-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3N3ZWV0c3BvdGRpYWJldGVzLmNvbSIsInN1YiI6IlN3ZWV0c3BvdCIsImlhdCI6MTY1MDYwMDk5NCwiY29uc2VudFBlcm1pc3Npb24iOiJsaW5rZWRTdWJqZWN0cyIsImRleGNvbUlkIjoiNWQ0ZWZkZTEtNzg4NC00Y2YzLWJlYjctMzllNTM4OGFjNDBkIiwiZXhwIjoxNjUwNjg3Mzk0LCJyb2xlIjoiT3duZXIiLCJzdWJqZWN0SWQiOiIxNTk0OTUwNjIwODQ3NDcyNjQwIn0.Sd4S5-AHMt83AdDiyKO2FCuPQ1l5UZcKYX8DLRWWXCxknnxQM39OYyVB42vwe6JHXJD0dAox4TskTeBGHaqJ-wVnGXKlfXtLnbxlDQzKSZW1LrMqeYK4tGL6WwEvA-lRJg31wzCgOrGPAJRCGnxZtUkONHt-UKLFRPyVFyrGP5vS9ttPnYAjNOUsqnjFO74hpBznvC-k07VYPyS_lw1UQ4XQ9xxf5hopWqjfUIv9Cy3dUv8a2uPNFWiMKs5KHSG_m2j9dkGtGvXEEFi7_Vu2_KhmDdUoS4JfZb0VPuQLqfFeYM2-XlqFlyoBIgxiEzIsh7aPxroCRTo7B0zVL69Kog'
    }

    # Body
    payload = {}

    # Request
    resp = requests.post(url, headers=headers, data=payload)

    # Validate
    resp_body = resp.json()
    assert resp_body['analysisSessionId'] is not None
