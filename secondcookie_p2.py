import requests

url = 'https://wds-prd.rvei.edu.in:4430/sap/bc/ui5_ui5/ui2/ushell/shells/abap/Fiorilaunchpad.html?sap-client=700&sap-language=EN'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
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

cookies = {
    'sap-usercontext': 'sap-language=EN&sap-client=700',
    'MYSAPSSO2': 'AjQxMDMBABhSAFYAQwBFADIAMwBCAEMAUwAwADIAOQACAAY3ADAAMAADABBGAEUAUAAgACAAIAAgACAABAAYMgAwADIANQAwADQAMgA2ADEAMAAzADgABQAEAAAACAYAAlgACQACRQD/APwwgfkGCSqGSIb3DQEHAqCB6zCB6AIBATELMAkGBSsOAwIaBQAwCwYJKoZIhvcNAQcBMYHIMIHFAgEBMBowDjEMMAoGA1UEAxMDRkVQAggKIBgHAhIXATAJBgUrDgMCGgUAoF0wGAYJKoZIhvcNAQkDMQsGCSqGSIb3DQEHATAcBgkqhkiG9w0BCQUxDxcNMjUwNDI2MTAzODEzWjAjBgkqhkiG9w0BCQQxFgQUIWG7jCCfUQrqwaBNauetG/OnZ0kwCQYHKoZIzjgEAwQvMC0CFG/PSRHtCmh5Y0KIrnlDecw1V8O0AhUAyshzDZ0TG3h7dp5OCJZtuI/Mp8U=',
    'SAP_SESSIONID_FEP_700': 'DvTIiy8s1ZFPGFHOhAv_f44Fh1siihHwrckK1KQ060Q=',
}

response = requests.get(url, headers=headers, cookies=cookies, verify=True)

print(response.status_code)
print(response.cookies)
