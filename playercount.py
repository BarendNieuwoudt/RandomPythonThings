import smtplib, ssl, time, mcstatus, json, requests

players = 0

while True:
	server = mcstatus.JavaServer.lookup("Minecraft Server IP")
	status = server.status()

	if players < status.players.online:
		sender_email = "SomeBody@gmail.com"
		context = ssl.create_default_context()
		
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as s:
			s.login(sender_email, "Some App Auth Code")
			s.sendmail(sender_email, "receiver Email Address", "Email Content")
	
	players = status.players.online
	print("{0} players - {1} ms".format(players, status.latency))
	time.sleep(5)
