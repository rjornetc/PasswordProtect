from Crypto.Cipher import DES3


class Password:
	def __init__(self,user,serv,passw):
		self.user = user
		self.serv = serv
		self.clearpassw = passw
		self.passw = passw

	def encrypt(self,iv):
		if len(self.user) < 16:
			self.user += ' ' * (16-len(self.user))
		des3 = DES3.new(self.user, DES3.MODE_CFB,iv)
		if len(self.clearpassw) < 24:
			if len(self.clearpassw) < 16:
				self.clearpassw += ' ' * (16-len(self.clearpassw))
			else:
				self.clearpassw += ' ' * (24-len(self.clearpassw))
			# self.clearpassw += ' ' * (16 - len(self.clearpassw) % 16)
		self.passw =  des3.encrypt(self.clearpassw)
		return self.passw

	def decrypt(self,iv):
		des3 = DES3.new(self.user, DES3.MODE_CFB, iv)
		self.clearpassw = des3.decrypt(self.passw)
		return self.clearpassw

