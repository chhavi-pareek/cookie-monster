from bs4 import BeautifulSoup

def get_hidden_xsrf(data, field_name):
    
    soup = BeautifulSoup(data, 'html.parser')
    hidden_input = soup.find('input', {'name': field_name})
    
    if hidden_input and hidden_input.has_attr('value'):
        print (hidden_input['value'])
        return hidden_input['value']
    else:
        print(f"Hidden field '{field_name}' not found.")
        return None


