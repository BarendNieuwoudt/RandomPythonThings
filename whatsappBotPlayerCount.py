import smtplib, ssl, time, mcstatus, json, requests

players = 0
access_token = ""

while True:
	server = mcstatus.JavaServer.lookup("MC Server IP")
	status = server.status()

	if players != status.players.online:
		players = status.players.online
	
		data = {
			'messaging_product': 'whatsapp',
			'to': "SOME NUMBER",
			'recipient_type': 'individual',
			'type': 'text',
			'text': {'body': f"Player Online: {players}"},
		}
	
		response = requests.post(
			f"https://graph.facebook.com/v15.0/PHONENUMBERID/messages",
			headers={"Authorization": f"Bearer {access_token}", 'Content-Type': 'application/json'},
			data=json.dumps(data)
		)
		
	print("{0} players - {1} ms".format(players, status.latency))
	time.sleep(5)