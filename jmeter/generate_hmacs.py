import hmac
from time import time
import hashlib

shared_secret = b'SHARED' # Change this shared_secret by your shared_secret
autheventid = 2
users = 50000
usersIni = 1

def get_hmac(userId, objType, objId, perm):
    secret = shared_secret
    now = 1000*long(time())
    message = "%s:%s:%d:%s:%d" % (userId, objType, objId, perm, now)
    _hmac = hmac.new(str(secret), str(message), hashlib.sha256).hexdigest()
    khmac  = 'khmac:///sha-256;%s/%s' % (_hmac, message)
    return ','.join([khmac, userId])

hmacs = []
total = 0
ini = time()
while total < users:
    hmacs.append(get_hmac(str(total+usersIni), "AuthEvent", autheventid, "vote"))
    total += 1
with open('datas.csv', 'w') as f:
    f.writelines('\n'.join(hmacs))
print(time() - ini)
