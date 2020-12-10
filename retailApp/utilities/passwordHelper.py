import secrets

import string

import hashlib


class passwordHasher:

	def getPassSalt(self):

		return ''.join(secrets.choice(string.ascii_letters +string.digits) for _ in range(20))

	def getPassHash(self, plain):

		return str(hashlib.sha256(plain.encode()).hexdigest())

	def validatePassword(self, plain, givenPass):

		return self.getPassHash(plain) == givenPass