text = '''But I'd use "on" in something like "You can reach me on my cell-phone at (867)555-5309." – ruakh816-679-3017 Jan 24 '12 at 3:46 ...'''

def isPhoneNumber(text):
	if len(text) != 12:
		return False #not phone num size
	for i in range(0,3):
		if not text[i].isdecimal():
			return False # no area code
	if text[3] != '-':
		return False #missing dash
	for i in range(4,7):
		if not text[i].isdecimal():
			return False #no first 3 digits
	if text[7] != '-':
		return False # missing second dash
	for i in range(8,12):
		if not text[i].isdecimal():
			return False #missing numbers
	else:
		print(True)


print(text)
string= "1234567890AB"

for i in string:
    print(string[i:i+6])
