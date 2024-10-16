from netmiko import ConnectHandler

# Define the device details for SSH connection
device_ssh = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.101',  # Replace with device's IP
    'username': 'prne',
    'password': 'cisco123!',
}

try:
    connection_ssh = ConnectHandler(**device_ssh)
    print("SSH Connection Established.")

    # Enter privileged EXEC mode
    connection_ssh.send_command('enable')

    # Enter global configuration mode
    connection_ssh.send_command('configure terminal')

    # Change the hostname
    new_hostname = "R2"
    connection_ssh.send_command(f'hostname {new_hostname}')
    print(f"Hostname changed to {new_hostname}.")

    # Exit configuration mode
    connection_ssh.send_command('end')

    # Retrieve the running configuration
    running_config = connection_ssh.send_command('show running-config')

    # Save the running configuration to a local file
    with open('running_config_ssh.txt', 'w') as file:
        file.write(running_config)
    print("Running configuration saved to running_config_ssh.txt.")

    # Close the connection
    connection_ssh.disconnect()
    print("SSH Connection Closed.")

except Exception as e:
    print(f"An error occurred: {e}")
