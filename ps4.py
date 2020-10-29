"""
CS4812, Prof. Ginsparg, Fall 2020
PS4, Problem 6
Conner Swenberg, cls364
"""

N = 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
p = 37975227936943673922808872755445627854565536638199
q = 40094690950920881030683735292761468389214899724061
c = pow(2,329) + 1


def encode_char(c):
  if c == ' ':
    return '00'
  n = ord(c)-96
  if n<10:
    return '0'+str(n)
  return str(n)

def decode_char(c):
  n = int(c)
  if n == 0:
    return ' '
  return chr(n + 96)

def encode_str(s):
  ret = ''
  for c in s:
    ret += encode_char(c)
  return ret

def decode_str(s):
  ret = ''
  i = 0
  while i<len(s)-1:
    ret += decode_char(s[i:i+2])
    i += 2
  return ret

b = 534803707672284108767377089597594956657892408930004128356378575045514019008129707864379980131366984

# taken from the internet: https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
        q = a // m 
        t = m 
        m = a % m 
        a = t 
        t = y 
        y = x - q * y 
        x = t 
    if (x < 0) : 
        x = x + m0 
    return x 

# i
print('part (i)')

d = modInverse(c, (p-1)*(q-1))
a = pow(b, d, N)
print(a)
print(decode_str(str(a)))

# ii
print('\npart (ii)')

b = 863832673712279575523354501283017978569873212006883353047966454906373467595226625635911718579173268

a = pow(b, d, N)
print(decode_str(str(a)))


# iii
print('\npart (iii)')

b = 1063771093404585971753478084418685375920278616019416214794102261412164317458424335976765564476312671
r = 9284176999527642442290355964223398961695537286349406211823296524543716284456735918035101038144170

d = modInverse(c, r)
a = pow(b, d, N)
print(decode_str('0'+str(a)))
