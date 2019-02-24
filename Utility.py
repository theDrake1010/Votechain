# Utility.py
# Houses all the security algorithms and procedures
# required to generate and verify signatures and accounts

import ecdsa
import hashlib



def applySHA256(message):												#hashing messages using SHA256 algorithm
	hashMsg = hashlib.sha256((str(message).encode())).hexdigest()
	return hashMsg


def generateKeyPair():
	sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)				#Use Elliptic Curve to generate secret key "sk"
	pk = sk.get_verifying_key()											#Use sk to generate public key "pk"
	return [sk,pk]														#Return both the keys


def applySignature(sk,inputdata):										#Generates Signature of inputdata with help of secret key
	sig = sk.sign((str(inputdata)).encode())
	return sig


def verifySignature(privateKey,publicKey,data,sig):
	sk = ecdsa.SigningKey.from_string(privateKey,curve = ecdsa.SECP256k1)
	pk = ecdsa.VerifyingKey.from_string(publicKey,curve = ecdsa.SECP256k1)
	sig=applySignature(sk,data)
	try:
		pk.verify(sig,(str(data)).encode())
		return True
	except:
		return False







## BEYOND THIS LINE, EVERYTHING IS FOR TESTING PURPOSES ONLY...

if __name__ == "__main__":
	[sk,pk] = generateKeyPair()
	data = input("Enter message to hash: ")
	print("The hashed msg is: "+ applySHA256(data))
	