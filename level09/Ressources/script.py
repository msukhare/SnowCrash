with open("token", "r") as f:
	token = f.read()
	final_token = ""
	for i, v in enumerate(token[:-1]):
		final_token += chr(ord(v) - i)
	print(final_token)
