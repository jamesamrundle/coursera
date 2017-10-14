import pprint

message = "Variables do not store list values directly; they store references to  Variables do not store list values directly; they store references to lists. This is an important distinction when copying variables or passing lists as arguments in function calls."
count = {} # 'r': 12

for character in message.upper():
    count.setdefault(character,0)
    count[character] = count[character] +1

print(count)    



kats= pprint.pformat(count)
