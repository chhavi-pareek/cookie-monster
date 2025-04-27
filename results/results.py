import requests
import json

def displayMarks(cookie):

    url = 'https://wds-prd.rvei.edu.in:4430/sap/opu/odata/sap/PIQ_COURSE_RESULTS_SRV/CourseResultSet?$skip=0&$top=100&$inlinecount=allpages&sap-client=700'

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'en',
        'Connection': 'keep-alive',
        'DataServiceVersion': '2.0',
        'MaxDataServiceVersion': '2.0',
        'Referer': 'https://wds-prd.rvei.edu.in:4430/sap/bc/ui5_ui5/ui2/ushell/shells/abap/FioriLaunchpad.html?sap-client=700&sap-language=EN',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XHR-Logon': 'accept="iframe,strict-window,window"',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    cookies = {
        'sap-usercontext': 'sap-language=EN&sap-client=700',
        'SAP_SESSIONID_FEP_700': cookie
    }

    response = requests.get(url, headers=headers, cookies=cookies, verify=False)

    print(response.status_code)

 
    response_data = json.loads(response.text)
    

    results = response_data.get('d', {}).get('results', [])

    marks_data = {}
    for course in results:
        course_name = course.get('CourseName', 'Unknown Course')
        marks = course.get('Results', 'N/A')
        marks_data[course_name] = marks


    for course, mark in marks_data.items():
        print(f"{course}: {mark}")
    
    return marks_data

