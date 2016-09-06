inp = int(raw_input("Enter input> "))

k = 1
s = 0
str_out = ""

d = inp % 10
s += k * d
str_out += str(d)
k *= -1
inp = inp / 10

while inp != 0:
    d = inp % 10
    s += k * d

    sign_k = "-" if k < 0 else "+"

    str_out += sign_k + str(d)
    k *= -1
    inp = inp / 10

print "=".join([str_out, str(s)])
