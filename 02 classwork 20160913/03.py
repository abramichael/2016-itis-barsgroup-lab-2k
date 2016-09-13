#d = {}
#d[0] = 100
#d['Sagit'] = 'Haliullin'
#if d.has_key(0):
#    print True
#print locals()
#for k in d.keys():
#    print k, ":", d[k]
#for k, v in d.iteritems():
#    print k, ":", v

letters = {chr(a + ord('a')): 0 for a in range(26)}

text = raw_input()
text = text.lower()

for c in text:
    if c.isalpha():
        letters[c] += 1

#c = 'a'
#while (c <= 'z'):
#    print c, letters[c]
#    c = chr(ord(c) + 1)

sorted_letters_list = sorted(letters.keys())

for c in sorted_letters_list:
    print c, letters[c]