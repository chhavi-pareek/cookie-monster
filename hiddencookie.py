from bs4 import BeautifulSoup

def get_hidden_xsrf(session, url, field_name):

    response = session.get(url, verify=True)
    soup = BeautifulSoup(response.text, 'html.parser')
    hidden_input = soup.find('input', {'name': field_name})
    
    if hidden_input and hidden_input.has_attr('value'):
        return hidden_input['value']
    else:
        raise ValueError(f"Hidden field '{field_name}' not found.")
