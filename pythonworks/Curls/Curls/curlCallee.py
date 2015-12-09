from curlRequester import sendCurlRequest

username = 'admin'
password = 'password'
instancesFile = 'instancesspreadout'
def BrowsePageServiceFlush():
    path = 'url/?shouldInvokeMethod=flushAllBrowseCaches'
    typeList = ['831','832','834']
    curlOnSocketsFromFile(instancesFile, path , username, password, typeList)

def curlOnSocketsFromFile(inputFileName, path,username, password):
    with open(inputFileName,'r') as fileName:
        lines = fileName.read().splitlines()
        for line in lines:
            sendCurlRequest(line,path,username,password)
