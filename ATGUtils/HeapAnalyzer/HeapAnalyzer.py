import re, os, scp, paramiko, socket, logging, shutil
from Constants import DynAdminConstants
from Constants import HTTPConstants

class HeapAnalyzer:
    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(message)s')
        self.hostsAndInstances = dict()
        logging.getLogger().setLevel(logging.INFO)
        self.constants = DynAdminConstants()
        self.httpConstants = HTTPConstants()
        self.serverPattern = re.compile("^s[0-9a-zA-Z]*:")
        self.alphaNumericPattern = re.compile('[\W_]+')
        self.findActiveInstances()
        self.extractActiveHosts()


    def findActiveInstances(self):
        if(socket.gethostname().startswith(self.constants.statsHost)):
            logging.info("You're already on " + self.constants.statsHost +", skipping the scp and doing a cp")
            shutil.copyfile(self.constants.instancesFileLocation + self.constants.instancesFile, self.constants.instancesFile)
        else:
            logging.info("SCP'ing the " + self.constants.instancesFile + " from " + self.constants.statsHost + ":" + self.constants.instancesFileLocation)
            sshClient = paramiko.SSHClient()
            sshClient.load_system_host_keys()
            sshClient.connect(self.constants.statsHost)
            scpClient = scp.SCPClient(sshClient.get_transport())
            scpClient.get(self.constants.instancesFileLocation + self.constants.instancesFile)
            scpClient.close()
            sshClient.close()
            logging.info("SCPing " + self.constants.instancesFile + " to " + socket.gethostname() + " is COMPLETE")

    def extractActiveHosts(self):
        if(os.path.isfile(self.constants.instancesFile)):
            logging.info("instancesFile present..now extracting active hosts")
            with open(self.constants.instancesFile, 'r') as f:
                lines = f.read().splitlines()
                for line in lines:
                    serverName = self.alphaNumericPattern.sub('',self.serverPattern.match(line).group(0))
                    self.hostsAndInstances[serverName] = ''
                logging.info(self.hostsAndInstances.keys())
    def sshCommandOnHost(self, host, cmd):
        logging.info("executing a ssh command on host")


    # def curlOnAllSocketsFromFile(self, path):
    #     with open(self.constants.instancesFile,'r') as fileName:
    #         lines = fileName.read().splitlines()
    #         for line in lines:
    #             curlResponse = self.sendCurlRequest(line, path, False)
    #             print(line  + ":" + self.processedCurlResponseCode(curlResponse) )
    #
    # def sendCurlRequest(self,socket,component_path, basePath):
    #     dyn_admin_url = 'http://' + socket
    #     if(basePath):
    #         dyn_admin_url += self.constants.nucleusBasePath
    #
    #     dyn_admin_url += component_path
    #     try:
    #         curlResponse = requests.get(dyn_admin_url, auth=HTTPBasicAuth(self.constants.userName, self.constants.password ), timeout=5)
    #         if( self.processedCurlResponseCode(curlResponse) == 'OK'):
    #          #Good to parse the payload
    #             return curlResponse
    #         else:
    #             return None
    #     except (requests.exceptions.ConnectionError):
    #         print("ERROR:: Connection issues on " + socket)
    #         return None
    # def processedCurlResponseCode(self, curlResponse):
    #     try:
    #         status_code = curlResponse.status_code
    #         if(str(status_code) in self.httpConstants.responseCodeDictionary.keys()):
    #             return self.httpConstants.responseCodeDictionary.get(str(status_code))
    #         else:
    #             return 'UNKNOWN'
    #     except AttributeError:
    #         print("ERROR::Curl Response doesn't have attributes")
    #         return 'UNKNOWN'


def main():
    calleeObj = HeapAnalyzer()

    ##calleeObj.dumpHeapValues()
