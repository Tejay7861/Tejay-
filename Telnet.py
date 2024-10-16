from netmiko import ConnectHandler

# Define the device details for Telnet connection
device_telnet = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.101',  
    'username': 'cisco', 
    'password': 'cisco123!',  
}

try:
    connection_telnet = ConnectHandler(**device_telnet)
    print("Telnet Connection Established.")

    # Change the hostname
    new_hostname = "R1"
    connection_telnet.send_command(f'hostname {new_hostname}')
    print(f"Hostname changed to {new_hostname}.")

    # Retrieve the running configuration
    running_config = connection_telnet.send_command('show running-config')

    # Save the running configuration to a local file
    with open('running_config_telnet.txt', 'w') as file:
        file.write(running_config)
    print("Running configuration saved to running_config_telnet.txt.")

    # Close the connection
    connection_telnet.disconnect()
    print("Telnet Connection Closed.")

except Exception as e:
    print(f"An error occurred: {e}")
