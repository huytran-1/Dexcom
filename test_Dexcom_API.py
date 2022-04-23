
#This is just an outline
#There should also be try-catch block and conditions for the flow, which can be added in real code

import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import re


def test_Dexcom_API():
    # first url
    url = 'https://clarity.dexcom.com/users/auth/dexcom_sts'

    # Start session
    session = requests.Session()

    # Send GET request to the first url, now allowing redirecting to maintain the cookie
    resp = session.get(url, allow_redirects=False)

    # Set redirecting url
    redirect_url = resp.headers["Location"]

    # Send GET request to the next url
    resp = session.get(redirect_url)

    # This should be redirected to login
    print(resp.url)

    # login payload
    payload = {
        "idsrv.xsrf": "27o0cL1T23YtwVMKbQ51tLKKqWJgvDZPzhlSlGLIZt8kVfH8weSVn8W6iDrnZwfDF60Qkbnx1AiYtE5NvzwGhOhv8JDxOxmju2GOVdtPwwE",
        # this is unique for each session
        "username": "nilepatest001",
        "password": "Password@1"
    }
    encoded_data = urlencode(payload)

    # Set the next url
    next_url = resp.url

    # Send POST request to the login
    # This will not redirect to the next page due to the unique code will not be generated
    resp = session.post(next_url, data=encoded_data)

    # This will show error message - testing purpose
    print(resp.content)

    # If this can redirect all the way to clarity.dexcom.com
    # We can use BeautifulSoup lib to get the access token
    # Example:
    soup = BeautifulSoup(resp.content, 'html.parser')
    token = soup.find('script', text=re.compile('window.ACCESS_TOKEN'))

    # Now with the token, it is easy to hit analysis_session
    final_url = 'https://clarity.dexcom.com/api/subject/1594950620847472640/analysis_session'

    headers = {
        'Access-Token': token
    }

    response = requests.post(final_url, headers=headers)
    body = response.json()
    assert body['analysisSessionId'] is not None
