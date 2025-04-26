import requests
from accesscookie import authCookie
import json

def marks(course_id):

    url = f'https://fes-prd1.rvei.edu.in:4430/sap/opu/odata/sap/PIQ_COURSE_RESULTS_SRV/CourseResultSet(CourseID=\'{course_id}\',AcadYearID=\'2023\',CLASS=\'ODD\',SessionID=\'901\',ProgramOfStudyID=\'00000000\',ProgramType=\'REGU\')?$expand=BookedEvents,DetailedAppraisals,CourseDetails,CourseContact,OtherCoursesModule,OtherCoursesProf&sap-client=700'
    
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'en',
        'Connection': 'keep-alive',
        'DataServiceVersion': '2.0',
        'MaxDataServiceVersion': '2.0',
        'Referer': 'https://fes-prd1.rvei.edu.in:4430/sap/bc/ui5_ui5/ui2/ushell/shells/abap/Fiorilaunchpad.html?sap-client=700&sap-language=EN',
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
        'SAP_SESSIONID_FEP_700': authCookie('RVCE23BCS029', 'iloveprateek')
    }

    response = requests.get(url, headers=headers, cookies=cookies, verify=False)

    print(response.status_code)

 
    response_data = json.loads(response.text)
    

    detailed_appraisals = response_data.get('d', {}).get('DetailedAppraisals', {}).get('results', [])

    marks_data = {}
    for appraisal in detailed_appraisals:
        field_name = appraisal.get('AppraisalType', 'Unknown Field')
        marks = appraisal.get('Result', 'N/A')
        marks_data[field_name] = marks
    

    for field, mark in marks_data.items():
        print(f"{field}: {mark}")
    
    return marks_data
    


marks(50170698)