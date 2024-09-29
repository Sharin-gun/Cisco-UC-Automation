# CUCM AXL API Python Script

This Python script connects to a Cisco Unified Communications Manager (CUCM) CUCM 15.0.1.10000-32 using the AXL API and retrieves available services and operations. The results are saved to a file named `output.txt`.

## Prerequisites

Before using the script, ensure you have the following installed and configured:

1. **Python 3.x**: Ensure that Python 3.x is installed.
2. **Zeep Library**: The script uses the `zeep` library to interact with CUCM's AXL API.
3. **CUCM WSDL File**: Download the AXL API WSDL file from your CUCM environment and provide the local path in the script.

### Install Dependencies

To install the required Python libraries, run:

pip install zeep requests

## Configuration

In the script, update the following variables in the `cucm` dictionary:

- `server`: Replace `{cucm_ip}` with the actual IP address or hostname of your CUCM server.
- `username`: Your CUCM AXL API username.
- `password`: Your CUCM AXL API password.
- `wsdl`: Provide the path to the `AXLAPI.wsdl` file. Download this from the CUCM administration under **Application > Plugins**.

Example:

```python
cucm = {
    'server': 'https://10.0.0.1:8443/axl/',  # Replace with actual CUCM server IP
    'username': 'your_username',  # Replace with AXL username
    'password': 'your_password',  # Replace with AXL password
    'wsdl': '/path/to/AXLAPI.wsdl',  # Replace with the actual path to the WSDL file
}
```

## How to Use

1. Clone this repository or download the script.
2. Make sure you have Python 3.x installed along with the necessary libraries (`zeep`, `requests`).
3. Update the `cucm` dictionary with your CUCM server information.
4. Run the script using the command:

python cucm_axl_script.py

5. After running the script, a file called `output.txt` will be created, containing the available ports and operations retrieved from CUCM.

## Output

The output will be saved in a file named `output.txt`, which will look something like:

```
Port: AXLPort
Operation: addUser
Operation: updateUser
Operation: getUser
Operation: removeUser
...
```

## Troubleshooting

- If SSL certificate verification is an issue (e.g., if using a self-signed certificate), SSL verification is disabled in the script using `session.verify = False`. If your environment uses valid certificates, you can enable this by setting `session.verify = True`.
- Make sure the WSDL file path is correct and accessible.
- Ensure the AXL API user has the necessary permissions.