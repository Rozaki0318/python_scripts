import paramiko
import managed_object as obj

for host, ssh_user, key in zip(obj.HOST, obj.SSH_USER, obj.KEY):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    client.connect(host, username=ssh_user, key_filename=key)
    
    stdin, stdout, stderr = client.exec_command('uptime')
    
    for line in stdout:
        print(line)

    client.close()
