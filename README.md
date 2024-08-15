# Service Executor Web Application

This project is a web-based tool designed for executing various network reconnaissance and penetration testing tasks. Built using Python and Flask, the application allows users to perform tasks such as **Nmap scanning**, **SQLmap testing**, **WPScan**, **nslookup**, **whois lookup**, **DNS lookup**, and a **"Check My IP"** feature.

## Features

* **Nmap Scanning**: Perform network discovery and security auditing.
* **SQLmap Testing**: Automate the process of detecting and exploiting SQL injection flaws.
* **WPScan**: Scan WordPress sites for vulnerabilities.
* **nslookup**: Query DNS to obtain domain name or IP address mapping.
* **whois Lookup**: Retrieve information about the ownership of a domain name.
* **DNS Lookup**: Fetch DNS records for a specified domain.
* **Check My IP**: Display the public IP address of the user visiting the site.

## Demo

Watch the video demonstration of how the website works: [Video Demonstration](https://github.com/user-attachments/assets/43e9b22f-c750-41a7-ab0a-3ce27fa4a28d)

## Installation

1. **Clone the Repository**:
```bash
git clone https://github.com/joshi-ji/L-B_project.git
cd L-B_project
```
*Install Dependencies*: Install the necessary Python packages:

```bash
pip install flask
```
*Run the Application*:
```bash
python3 run_service.py
```
*Access the Web Application*: Open your web browser and go to  http://127.0.0.1:5000

*Sudo Privileges Setup*: For certain tools like Nmap, SQLmap, and WPScan, sudo privileges are required. To allow these tools to run without prompting for a password, you can modify the sudoers file using sudo visudo and add the following line:
```bash
www-data ALL=(ALL) NOPASSWD: /usr/bin/nmap, /usr/bin/sqlmap, /usr/bin/wpscan
```

*Deployment*

This application can be deployed on various platforms, such as:

- Heroku
- DigitalOcean
- AWS
- Google Cloud

*Contributing*

Feel free to submit issues or pull requests if you have any suggestions or improvements.



