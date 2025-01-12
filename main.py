import helpers

# this function is intended to run at a constant interval (i.e. every 5 minutes)

def windscribe_auto_ephemeral_port_forwarding():
	try:
		response = helpers.test_port()
		if response:
			print(response)
	except Exception as e:
		print(e)

windscribe_auto_ephemeral_port_forwarding()