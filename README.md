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

Watch the video demonstration of how the website works: [![Service Executor Demo](URL-to-video-thumbnail)](URL-to-video)

## Installation

1. **Clone the Repository**:
```bash
git clone (link unavailable)
cd repositoryname
```
*Install Dependencies*: Ensure you have Python 3.x installed. Install the necessary Python packages:

```bash
pip install flask
```
*Run the Application*:
```bash
python3 (link unavailable)
```
*Access the Web Application*: Open your web browser and go to (link unavailable).

*Sudo Privileges Setup*: For certain tools like Nmap, SQLmap, and WPScan, sudo privileges are required. To allow these tools to run without prompting for a password, you can modify the sudoers file using sudo visudo and add the following line:
```bash
www-data ALL=(ALL) NOPASSWD: /usr/bin/nmap, /usr/bin/sqlmap, /usr/bin/wpscan
```
Note: Granting sudo privileges without a password is not recommended for production environments due to security risks.

*Deployment*

This application can be deployed on various platforms, such as:

- Heroku
- DigitalOcean
- AWS
- Google Cloud
- (link unavailable)

*Contributing*

Feel free to submit issues or pull requests if you have any suggestions or improvements.

*License*

This project is licensed under the MIT License.
