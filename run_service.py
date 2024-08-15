from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Service Executor</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 20px;
            }
            .container {
                max-width: 600px;
                margin: 0 auto;
                background: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                text-align: center;
                color: #333;
            }
            select, input, button {
                width: calc(100% - 20px);
                padding: 10px;
                margin-bottom: 10px;
            }
            button {
                background-color: #007bff;
                color: white;
                border: none;
                cursor: pointer;
                border-radius: 5px;
            }
            button:hover {
                background-color: #0056b3;
            }
            #results {
                margin-top: 20px;
                max-height: 500px;
                overflow-y: auto;
                background: #f9f9f9;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            pre {
                white-space: pre-wrap;
                word-break: break-word;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Service Executor</h1>
            <form id="serviceForm">
                <label for="service">Select Service:</label>
                <select name="service" id="service" required>
                    <option value="nmap">nmap</option>
                    <option value="sqlmap">sqlmap</option>
                    <option value="wpscan">wpscan</option>
                    <option value="nslookup">nslookup</option>
                    <option value="whois">whois lookup</option>
                    <option value="subdomain_scanner">Subdomain scanner</option>
                    <option value="dns_lookup">DNS lookup</option>
                    <option value="check_ip">Check My IP</option>
                </select><br>
                <label for="target">Target URL/Host:</label>
                <input type="text" id="target" name="target" placeholder="Enter URL/Host" required><br>
                <label for="flags">Additional Flags:</label>
                <input type="text" id="flags" name="flags" placeholder="Enter flags (optional)"><br>
                <button type="submit">Run</button>
            </form>
            <div id="results"></div>
        </div>
        <script>
            document.getElementById('serviceForm').addEventListener('submit', function(e) {
                e.preventDefault();

                let service = document.getElementById('service').value;
                let target = document.getElementById('target').value;
                let flags = document.getElementById('flags').value;
                let resultsDiv = document.getElementById('results');
                resultsDiv.innerHTML = 'Running...';

                fetch('/run_service', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    },
                    body: 'service=' + encodeURIComponent(service) + '&target=' + encodeURIComponent(target) + '&flags=' + encodeURIComponent(flags)
                })
                .then(response => response.text())
                .then(data => {
                    resultsDiv.innerHTML = '<pre>' + data + '</pre>';
                })
                .catch(error => {
                    resultsDiv.innerHTML = 'Error: ' + error;
                });
            });

            document.getElementById('service').addEventListener('change', function() {
                let targetField = document.getElementById('target');
                if (this.value === 'check_ip') {
                    targetField.disabled = true;
                } else {
                    targetField.disabled = false;
                }
            });
        </script>
    </body>
    </html>
    '''

@app.route('/run_service', methods=['POST'])
def run_service():
    service = request.form['service']
    target = request.form['target']
    flags = request.form['flags']
    result = ""

    try:
        cmd = []
        if service == 'nmap':
            cmd = ['sudo', 'nmap'] + flags.split() + [target]
        elif service == 'sqlmap':
            cmd = ['sudo', 'sqlmap', '-u', target, '--batch'] + flags.split()
        elif service == 'wpscan':
            cmd = ['sudo', 'wpscan', '--url', target] + flags.split()
        elif service == 'nslookup':
            cmd = ['nslookup'] + [target]
        elif service == 'whois':
            cmd = ['whois'] + [target]
        elif service == 'subdomain_scanner':
            cmd = ['sublist3r', '-d', target] + flags.split()
        elif service == 'dns_lookup':
            cmd = ['dig'] + [target]
        elif service == 'check_ip':
            result = f"Your IP Address: {request.remote_addr}"
        else:
            result = "Service not recognized."

        if cmd:
            result = subprocess.run(cmd, capture_output=True, text=True).stdout
    except Exception as e:
        result = str(e)

    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)