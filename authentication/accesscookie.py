import requests
from authentication.hiddencookie import get_hidden_xsrf



def authCookie(user, password):

    url = 'https://wds-prd.rvei.edu.in:4430/sap/bc/ui5_ui5/ui2/ushell/shells/abap/Fiorilaunchpad.html'

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://wds-prd.rvei.edu.in:4430',
        'Referer': 'https://wds-prd.rvei.edu.in:4430/sap/bc/ui5_ui5/ui2/ushell/shells/abap/Fiorilaunchpad.html',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }


    session = requests.Session()

    xsrf_token = get_hidden_xsrf(session, url, 'sap-login-XSRF')

    data = {
        'sap-user': user,
        'sap-password': password,
        'sap-client': '700',
        'sap-system-login-oninputprocessing': 'onLogin',
        'sap-urlscheme': '',
        'sap-system-login': 'onLogin',
        'sap-system-login-basic_auth': '',
        'sap-accessibility': '',
        'sap-login-XSRF': xsrf_token,
        'sap-system-login-cookie_disabled': '',
        'sap-hash': '',
        'sap-language': 'EN',
    }

    response = session.post(url, headers=headers, data=data, verify=True)

    for cookie in session.cookies:
        if 'SAP_SESSIONID_FEP_700' in cookie.name:
            return cookie.value
            


