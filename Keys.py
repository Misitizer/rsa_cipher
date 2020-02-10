import random, cryptomath
import rabinMiller as rm

def generateKey(keySize):
    p = rm.generateLargePrime(keySize)
    q = rm.generateLargePrime(keySize)
    n = p * q
    while True:
        e = random.randrange(2**(keySize - 1), 2**(keySize))
        if cryptomath.gcd(e, (p-1)*(q-1)) == 1:
            break
    d = cryptomath.findModInverse(e, (p-1)*(q-1))
    publicKey = (n, e)
    privateKey = (n, d)
    print('Public Key: ', publicKey)
    print('Private Key: ', privateKey)
    return (publicKey, privateKey)

def makeKeyFiles(keySize):
    publicKey, privateKey = generateKey(keySize)
    fo = open('publicKey.txt', 'w')
    fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
    fo.close()
    fo = open('privateKey.txt', 'w')
    fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
    fo.close()

def main():
    makeKeyFiles(1024)

main()