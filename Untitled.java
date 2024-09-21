import os
import subprocess

# Function to specify target
def specify_target():
    global target
    target = input("Enter the target URL (e.g., http://example.com): ")
    print(f"Target set to: {target}\n")

# Function to run W3AF scan with a specific plugin
def run_w3af_scan(plugin):
    if not target:
        print("Please specify the target URL first!")
        return

    print(f"Running {plugin} scan on {target}...\n")

    # Prepare W3AF commands
    commands = f"""
    w3af_console <<EOF
    target set_target {target}
    plugins
    audit {plugin}
    back
    start
    exit
    EOF
    """

    # Execute the W3AF commands
    result = subprocess.run(commands, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Print the output from W3AF
    print(result.stdout)
    print(result.stderr)

# Reconnaissance phase (can be expanded with discovery plugins)
def reconnaissance():
    if not target:
        print("Please specify the target URL first!")
        return

    print(f"Running reconnaissance on {target}...\n")

    # Reconnaissance phase using discovery plugins
    commands = f"""
    w3af_console <<EOF
    target set_target {target}
    plugins
    discovery web_spider
    back
    start
    exit
    EOF
    """

    result = subprocess.run(commands, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)
    print(result.stderr)

# Automated scan with multiple plugins
def automated_scan():
    if not target:
        print("Please specify the target URL first!")
        return

    print(f"Running an automated scan on {target} with multiple plugins...\n")

    # Use multiple plugins for a comprehensive scan
    commands = f"""
    w3af_console <<EOF
    target set_target {target}
    plugins
    audit csrf
    audit sqli
    audit xss
    audit file_include
    audit os_commanding
    audit path_disclosure
    audit response_splitting
    audit file_upload
    audit click_jacking
    audit cookie_secure
    audit xpath
    audit buffer_overflow
    audit ldap
    audit unvalidated_redirects
    audit cors_origin
    back
    start
    exit
    EOF
    """

    result = subprocess.run(commands, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)
    print(result.stderr)

# Main menu function
def menu():
    while True:
        print("\n----- W3AF Vulnerability Scanner -----")
        print("1. Specify Target")
        print("2. Reconnaissance")
        print("3. CSRF Scan")
        print("4. SQL Injection Scan")
        print("5. XSS Scan")
        print("6. File Inclusion Scan")
        print("7. OS Command Injection Scan")
        print("8. Path Disclosure Scan")
        print("9. Remote File Upload Scan")
        print("10. Clickjacking Scan")
        print("11. Directory Traversal Scan")
        print("12. HTTP Response Splitting Scan")
        print("13. Buffer Overflow Scan")
        print("14. LDAP Injection Scan")
        print("15. XPath Injection Scan")
        print("16. HTML Injection Scan")
        print("17. Session Fixation Scan")
        print("18. SSL/TLS Vulnerability Scan")
        print("19. Information Disclosure Scan")
        print("20. Weak Authentication Mechanisms")
        print("21. CORS Vulnerability Scan")
        print("22. Insecure Cookies Scan")
        print("23. Open Redirect Scan")
        print("24. Automated Scan")
        print("25. Exit")
        
        choice = input("Enter your choice (1-25): ")

        if choice == '1':
            specify_target()
        elif choice == '2':
            reconnaissance()
        elif choice == '3':
            run_w3af_scan('csrf')
        elif choice == '4':
            run_w3af_scan('sqli')
        elif choice == '5':
            run_w3af_scan('xss')
        elif choice == '6':
            run_w3af_scan('file_include')
        elif choice == '7':
            run_w3af_scan('os_commanding')
        elif choice == '8':
            run_w3af_scan('path_disclosure')
        elif choice == '9':
            run_w3af_scan('file_upload')
        elif choice == '10':
            run_w3af_scan('click_jacking')
        elif choice == '11':
            run_w3af_scan('path_disclosure')
        elif choice == '12':
            run_w3af_scan('response_splitting')
        elif choice == '13':
            run_w3af_scan('buffer_overflow')
        elif choice == '14':
            run_w3af_scan('ldap')
        elif choice == '15':
            run_w3af_scan('xpath')
        elif choice == '16':
            run_w3af_scan('html_injection')
        elif choice == '17':
            run_w3af_scan('session_fixation')
        elif choice == '18':
            run_w3af_scan('ssl_certificate')
        elif choice == '19':
            run_w3af_scan('fingerprint_os')
        elif choice == '20':
            run_w3af_scan('basic_auth_brute')
        elif choice == '21':
            run_w3af_scan('cors_origin')
        elif choice == '22':
            run_w3af_scan('cookie_secure')
        elif choice == '23':
            run_w3af_scan('open_redirect')
        elif choice == '24':
            automated_scan()
        elif choice == '25':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 25.")

if __name__ == "__main__":
    target = None
    menu()
