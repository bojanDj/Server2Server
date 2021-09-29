import paramiko

class SSHConnection(object):
    def __init__(self, host, username, password, port=22):
        self.sftp = None
        self.sftp_open = False
        
        self.transport = paramiko.Transport((host, port))
        
        self.transport.connect(username=username, password=password)
        
    def _openSFTPConnection(self):
        if not self.sftp_open:
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
            self.sftp_open = True
    
    def copy(self, local_path, remote_path):
        self._openSFTPConnection()
        self.sftp.put(local_path, remote_path)
        
    def close(self):
        if self.sftp_open:
            self.sftp.close()
            self.sftp_open = False
        self.transport.close()
        
if __name__ == "__main__":
    host = "myserver"
    username = "boki"
    pw = "pass"
    
    list = os.listdir("/")
	number_files = len(list)

    origin = '/desktop/'
    dst = '/desktop/'
    
    ssh = SSHConnection(host, username, pw)
    for x in list:
        ssh.copy(origin + x, dst + x)
    
    stdout = ssh.exec_command('python /direktorijum/executionSkript.py')[1]
    for line in stdout:
        print line

    ssh.close()