import requests
from bs4 import BeautifulSoup
import urllib.parse

# Function to extract forms from a web page
def get_forms(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.find_all('form')


def get_form_details(form):
    details = {}
    try:
        action = form.attrs.get('action').lower()
    except:
        action = ""
    method = form.attrs.get('method', 'get').lower()
    inputs = []
    for input_tag in form.find_all('input'):
        input_type = input_tag.attrs.get('type', 'text')
        input_name = input_tag.attrs.get('name')
        inputs.append({'type': input_type, 'name': input_name})
    details['action'] = action
    details['method'] = method
    details['inputs'] = inputs
    return details


def submit_form(form_details, url, payload):
    target_url = urllib.parse.urljoin(url, form_details['action'])
    inputs = form_details['inputs']
    data = {}
    for input in inputs:
        if input['type'] == 'text' or input['type'] == 'search':
            data[input['name']] = payload
        else:
            data[input['name']] = 'test' 
    if form_details['method'] == 'post':
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)
    
import subprocess


def verify_xss_with_xsstrike(target_url):
    try:
        # Build the xsstrike command with the target URL
        xsstrike_command = ['python', 'XSStrike/xsstrike.py', '-u', target_url]

        # Execute the xsstrike command
        print(f"Running XSStrike against {target_url}......")
        result = subprocess.run(xsstrike_command, capture_output=True, text=True)

        
        print(result.stdout)
 
        if "XSS found" in result.stdout or "Injection found" in result.stdout:
            print(f"[!!!] XSS vulnerability found in {target_url}.")
        else:
            print(f"[+] No XSS vulnerabilities found in {target_url}.")

    except Exception as e:
        print(f"Error running XSStrike: {e}")



def scan_xss(url):
    forms = get_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    xss_test_script = "<script>alert('XSS')</script>"
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        print(f"[+] Testing form in {form_details['action']} with method {form_details['method']}")
        response = submit_form(form_details, url, xss_test_script)
        if xss_test_script in response.content.decode():
            print(f"[!!!] XSS Detected on {url}")
            print(f"[*] Form details: {form_details}")
            is_vulnerable = True
        else:
            print(f"[+] No XSS detected in form.")
    return is_vulnerable

# Main script execution
if __name__ == "__main__":
    target_url = input("Enter URL to scan for XSS: ")
    print(f"Scanning {target_url} for XSS vulnerabilities...")
    is_vulnerable = scan_xss(target_url)
    print(f'Confirming XSS Vulnerabilites......')
    verify_xss_with_xsstrike(target_url)

    if not is_vulnerable:
        print("No XSS..... vulnerabilities detected.")

