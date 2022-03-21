import paramiko

host = ["3.26.62.150", "3.26.75.61", "3.26.47.19"]
username = "cloud_user"
password = "xxxxxxxxxx"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for server in host:
    client.connect(server, username=username, password=password, allow_agent=False)
    # # to put a file
    # ftp_client = client.open_sftp()
    # ftp_client.put('/home/vnix/python/sshToServerWithParamiko/testfile','testfile')
    # ftp_client.close()
    stdin, _stdout,_stderr = client.exec_command("ls -l", get_pty=True)
    # # If root user needed
    # stdin.write(f'{password}\n')
    # stdin.flush()
    print(_stdout.read().decode())

client.close()
