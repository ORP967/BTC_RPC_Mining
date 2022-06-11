from __future__ import print_function
from multiprocessing import Process
import json
import requests
import time

# Information I need to log into my RPC
rpcport = 18332
rpcuser = 'Chocolatier'
rpcpassword = 'RPCs'
rpcip = '127.0.0.1'

# Bitcoin mining information would go here
MAX_NONCE = int(1000000)

# Way I use to connect and retrieve information from my RPC
serverURL = 'http://' + str(rpcuser) + ':' + str(rpcpassword)+ '@' + str(rpcip)+":" + str(rpcport)

class RPCHost(object):
    def __init__(self, url):
        self._session = requests.Session()
        self._url = url
        self._headers = {'content-type': 'application/json'}
    def call(self, rpcMethod, *params):
        payload = json.dumps({"method": rpcMethod, "params": list(params), "jsonrpc": "2.0"})
        tries = 5
        hadConnectionFailures = False
        while True:
            try:
                response = self._session.post(self._url, headers=self._headers, data=payload)
            except requests.exceptions.ConnectionError:
                tries -= 1
                if tries == 0:
                    raise Exception('Failed to connect for remote procedure call.')
                hadFailedConnections = True
                print("Couldn't connect for remote procedure call, will sleep for five seconds and then try again ({} more tries)".format(tries))
                time.sleep(10)
            else:
                if hadConnectionFailures:
                    print('Connected for remote procedure call after retry.')
                break
        if not response.status_code in (200, 500):
            raise Exception('RPC connection failure: ' + str(response.status_code) + ' ' + response.reason)
        responseJSON = response.json()
        if 'error' in responseJSON and responseJSON['error'] != None:
            raise Exception('Error in RPC call: ' + str(responseJSON['error']))
        return responseJSON['result']
    
# host is used to get information on the RPC API
# full list is on https://developer.bitcoin.org/reference/rpc/index.html
host = RPCHost(serverURL)

# getblocktemplate replaces getwork
template = host.call("getblocktemplate", {"rules": ["segwit"]})

# This is where I get stuck. What to do with the information I recieve. Running a loop on this template gives me the following information:

#for i in template:
#    print(i)
capabilities
version
rules
vbavailable
vbrequired
previousblockhash
transactions
coinbaseaux
coinbasevalue
longpollid
target
mintime
mutable
noncerange
sigoplimit
sizelimit
weightlimit
curtime
bits
height
default_witness_commitment
# Where do we go from here. What information do I need, how to process it and what can I discard?
