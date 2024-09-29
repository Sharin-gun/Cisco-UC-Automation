from requests.auth import HTTPBasicAuth
from zeep import Client, Settings
from zeep.transports import Transport
from requests import Session
from zeep.cache import SqliteCache

# Configuration Parameter for Connecting to CUCM 15.0.1.10000-32
cucm = {
    'server': 'https://{cucm_ip}:8443/axl/',
    'username': 'username',
    'password': 'password',
    'wsdl': "location to AXLAPI.wsdl",  # Download the WSDL from CUCM and provide the local path
}

# Establish a session with authentication
session = Session()
session.verify = False  # Disable SSL verification if using self-signed certificates (optional)
session.auth = HTTPBasicAuth(cucm['username'], cucm['password'])

# Zeep client settings
settings = Settings(strict=False, xml_huge_tree=True)
transport = Transport(cache=SqliteCache(), session=session, timeout=10)

# Create the Zeep client
client = Client(cucm['wsdl'], settings=settings, transport=transport)

# Open a text file to save the output
with open("output.txt", "w") as file:  # Opens or creates a file named output.txt in write mode
    
    # Redirect print statements to the text file
    for service in client.wsdl.services.values():
        for port in service.ports.values():
            file.write(f"Port: {port.name}\n")
            for operation in port.binding._operations.values():
                file.write(f"Operation: {operation.name}\n")
