__author__ = 'v-mudrak-8l'

from curlRequester import sendCurlRequest

username = 'krishna'
password = 'Eagles@123'
instancesFile = 'instancesspreadout'
def BrowsePageServiceFlush():
    path = 'aeo/commerce/catalog/services/BrowsePageService/?shouldInvokeMethod=flushAllBrowseCaches'
    typeList = ['831','832','834']
    curlOnSocketsFromFile(instancesFile, path , username, password, typeList)

def curlOnSocketsFromFile(inputFileName, path,username, password):
    with open(inputFileName,'r') as fileName:
        lines = fileName.read().splitlines()
        for line in lines:
            sendCurlRequest(line,path,username,password)