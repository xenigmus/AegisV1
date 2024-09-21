import os
import subprocess
import shutil
from datetime import datetime

# Function to check for Aegis and other requirements
def check_requirements():
    if not shutil.which("aegis_console"):
        print("Error: 'aegis_console' not found! Please install it before running the script.")
        exit(1)
    print("All requirements are satisfied.\n")

# Function to display a banner
def display_banner():
    banner = """
    ==============================================
        Aegis Vulnerability Scanner v1.0
          Securing the Web Since 2024
    ==============================================
    """
    print(banner)

# Function to write to report file
def write_report(plugin, output):
    with open("reports.txt", "a") as report_file:
        report_file.write(f"---- {plugin} scan on {target} ----\n")
        report_file.write(f"Date: {datetime.now()}\n")
        report_file.write(output)
        report_file.write("\n\n")
    print(f"Results saved to reports.txt\n")

# Function to specify target
def specify_target():
    global target
    target = input("Enter the target URL (e.g., http://example.com): ")
    print(f"Target set to: {target}\n")

# Function to run Aegis scan with a specific plugin
def run_aegis_scan(plugin):
    if not target:
        print("Please specify the target URL first!")
        return

    print(f"Running {plugin} scan on {target}...\n")

    # Prepare Aegis commands
    commands = f"""
    aegis_console <<EOF
    target set_target {target}
    plugins
    audit {plugin}
    back
    start
    exit
    EOF
    """

    # Execute the Aegis commands
    result = subprocess.run(commands, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Capture output and save to reports
    output = result.stdout + result.stderr
    print(output)
    write_report(plugin, output)

# Reconnaissance phase
def reconnaissance():
    if not target:
        print("Please specify the target URL first!")
        return

    print(f"Running reconnaissance on {target}...\n")

    # Prepare Aegis commands for reconnaissance
    commands = f"""
    aegis_console <<EOF
    target set_target {target}
    plugins
    discovery web_spider
    back
    start
    exit
    EOF
    """

    result = subprocess.run(commands, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = result.stdout + result.stderr
    print(output)
    write_report("Reconnaissance", output)

# Automated scan with multiple plugins
def automated_scan():
    if not target:
        print("Please specify the target URL first!")
        return

    print(f"Running an automated scan on {target} with multiple plugins...\n")

    # Use multiple plugins for a comprehensive scan
    commands = f"""
    aegis_console <<EOF
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
    output = result.stdout + result.stderr
    print(output)
    write_report("Automated Scan", output)

# Main menu function
def menu():
    while True:
        print("\n----- Aegis Vulnerability Scanner -----")
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
            run_aegis_scan('csrf')
        elif choice == '4':
            run_aegis_scan('sqli')
        elif choice == '5':
            run_aegis_scan('xss')
        elif choice == '6':
            run_aegis_scan('file_include')
        elif choice == '7':
            run_aegis_scan('os_commanding')
        elif choice == '8':
            run_aegis_scan('path_disclosure')
        elif choice == '9':
            run_aegis_scan('file_upload')
        elif choice == '10':
            run_aegis_scan('click_jacking')
        elif choice == '11':
            run_aegis_scan('path_disclosure')
        elif choice == '12':
            run_aegis_scan('response_splitting')
        elif choice == '13':
            run_aegis_scan('buffer_overflow')
        elif choice == '14':
            run_aegis_scan('ldap')
        elif choice == '15':
            run_aegis_scan('xpath')
        elif choice == '16':
            run_aegis_scan('html_injection')
        elif choice == '17':
            run_aegis_scan('session_fixation')
        elif choice == '18':
            run_aegis_scan('ssl_certificate')
        elif choice == '19':
            run_aegis_scan('fingerprint_os')
        elif choice == '20':
            run_aegis_scan('basic_auth_brute')
        elif choice == '21':
            run_aegis_scan('cors_origin')
        elif choice == '22':
            run_aegis_scan('cookie_secure')
        elif choice == '23':
            run_aegis_scan('open_redirect')
        elif choice == '24':
            automated_scan()
        elif choice == '25':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 25.")

if __name__ == "__main__":
    target = None
    display_banner()
    check_requirements()
    menu()
