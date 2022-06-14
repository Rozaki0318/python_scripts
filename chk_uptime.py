import paramiko

HOST = 'XXXXXX'
SSH_USER = 'XXXXX'
KEY = '/home/ozaki/.ssh/XXXXX.pem'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect(HOST, username=SSH_USER, key_filename=KEY)

stdin, stdout, stderr = client.exec_command('uptime')
for line in stdout:
    print(line)

client.close()
