import requests


class Sender(object):
	"""duid, messagetring for sender"""
	def __init__(self, server):
		super(Sender, self).__init__()
		
		self.server = server
		
		self.api_friend_message = server+"/openqq/send_friend_message"
		self.api_send_group_message = server+"/openqq/send_group_message"	
		self.api_send_discuss_message = server+"/openqq/send_discuss_message"


	def send_message(self, uid, message, type):
		recipient = "?uid={}&content={}".format(uid, message)
		if type == "friend":
			r = requests.get(self.api_friend_message+recipient)
			print(r.text)
		if type == "group":
			r = requests.get(self.api_send_group_message+recipient)
			print(r.text)
		if type == "discuss":
			r = requests.get(self.api_send_discuss_message+recipient)
			print(r.text)
		