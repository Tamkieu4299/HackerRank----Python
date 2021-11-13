#rjust
STDIN = int(input())
w = len(str(bin(STDIN)).replace('0b',''))
# Because bin(), etc returns a string started with '0b','0','0x'. And we need to print only the rest of this string.
for i in range(1, STDIN+1):
    b = bin(int(i)).replace('0b','').rjust(w, ' ')
    o = oct(int(i)).replace('0','',1).rjust(w, ' ')
    h = hex(int(i)).replace('0x','').upper().rjust(w, ' ')
    j = str(i).rjust(w, ' ')
    print (j, o, h, b)

#format
n = int(input())
width = len("{0:b}".format(n))
for i in range(1,n+1):
  print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))