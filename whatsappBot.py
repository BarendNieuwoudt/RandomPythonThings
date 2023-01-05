import json, requests

phone_number_id = ""
access_token = ""
recipient_phone_number = ""

url = f"https://graph.facebook.com/v15.0/{phone_number_id}/messages"
headers = {"Authorization": f"Bearer {access_token}", 'Content-Type': 'application/json'}

data = {
    'messaging_product': 'whatsapp',
    'to': recipient_phone_number,
	'recipient_type': 'individual',
    'type': 'text',
    'text': {
		'body': 'Player Joined'
	},
}

response = requests.post(
    url,
    headers=headers,
    data=json.dumps(data)
)

print(str(response.json()))