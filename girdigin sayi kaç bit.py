x=int(input('bir sayı giriniz'))
i=8
k=1
while(x>=2**i):
    i=i+8
    k=k+1
kb=k/(2**10)
mb=k/(2**20)
gb=k/(2**30)
print('kilobayt: '+ str(kb))
print('megabayt: '+ str(mb))
print('gigabayt: '+ str(gb))