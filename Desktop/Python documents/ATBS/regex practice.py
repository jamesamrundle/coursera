import re
text = " (123) 123 -123 1234 LOL12"
numsearch =  re.compile(r'(\d\d\d) ?(\D\D\D)')
#numsearch =  re.compile(r'?\(\d\d\d ?\)')
mo =  numsearch.search(text)

print (mo.groups())
