
kilomen=open("matako.txt","r")
print(kilomen.read())
kilomen.close()

kilomen=open("matako.txt",'w')
kilomen.write("issa cat")
kilomen.close()

kilomen=open("matako.txt","r")
print(kilomen.read())
kilomen.close()

hui="matako mema huonekana asubuhi"
filo=open("kukumanga.txt","w")
k=filo.write(hui)
print(k)
filo.close()



with open("matako.txt") as r:
    print(r.read())
if None:
    print("ka  ni goshodo modo")
else:
    print('aii nyonya')



poo=print("kude kude")
if poo==None:
    print(2)
else:
    print(4)

run={"iwobi":[25,90,78],"matako":[98,0,9],"githo":[45,87,9]}
print(run["iwobi"])

gugulethu=[4,45,{'pudesh':3,9:[3,4]},7]
print(gugulethu[2][9][1])

a=6
b=a
a+=2
print(a)
print(b)

a="hello"
b=a
a+=" punyeto"
print(a)
print(b)

a=["haga","duba","kuma"]
b=a
a.append("tiddies")
print(a)
print(b)

gugulet={2:34,'error':5674,78:546,"ortho":45}
gugulet['error']=6
gugulet[7]=780
print(gugulet)

lamnda={1:"gari",2:"nyumba",3:"ndege"}
print(1 in lamnda)
print(4 in lamnda)
print( 5 not in lamnda)
print("nyumba" in lamnda)

polis={1:"kanis",True:False,"One":"Acen",8:678,9:45,7:[1,2,3]}
print(polis.get("One"))
print(polis.get(4,"not in list"))
print(polis.get(15))
print(polis .get(1))


sudu={1:23,'one':"acen",True:False}
print(sudu.get(1))


hujinatao={1:34,4:56,8:97,7:34,7:32}
print(hujinatao.get(7,45)+hujinatao.get(0,1))


yobrat=(1,2,3,4,5,[1,2,3,4,5],[5,4,3,2,1])
yobrat[5][4]="jaba"
yobrat[6].append("jaba")
print(yobrat)

kongwea='ma','me','mi','mo','mu'
print(kongwea)

kil=''
print(kil)

lopo=()
print(lopo)

poki=(9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9)
print(poki[2:6])
print(poki[0:5])



dondosa=45,35,46,36,12,23,76,98,87,65,41
print(dondosa[::-2])
print(dondosa[::-1])
print(dondosa[7:1:-2])
print(dondosa[2:6:2])

contra="my","nunu","is","wet"
print(contra[::-1])

guru="my nunu is wet"
print(guru[::-1])

mawe=89,54,36,76,87,98,7765,43,21,12,34,56,78,90,98,76,54,32,1
print(mawe[:8])
print(mawe[8:])

jingtin=34,23,12,23,45,67,89,98,76,54,32,22
print(jingtin[:])
print(jingtin[4:100])
print(jingtin[4:-1])
print(jingtin[8:-1])



bigG=67,87,76,56,45,34,23,12,34,56,78,90,98,76,54,32
print(bigG[1::4])
print(bigG[3::2])

aii=43,54,54,34,23,43,56,54,34,23,24,24,34,56
print(aii[::-1])
print(aii[::2])
print(aii[:1:])
print(aii[4:-1])

kulagang=[o**3 for o in range(5)]
print(kulagang)


kongo=[k**2 for k in range(10) if k**2%2==0]
print(kongo)


libido=[21, 32, 43, 54, 65, 76, 87, 98, 98]
hujintamao="kumambekse: {2} {1} {0}".format(libido[8],libido[6],libido[4])
print(hujintamao)
print(hujintamao[12]+hujintamao[13])
print(int(hujintamao[12])+int(hujintamao[13]))

octavian="{j} {z}".format(j=56, z=45)
print(octavian)

print(",".join(["Hennessy",'jaba']))

print("sipendi,jaba,mabati".split(","))

print("JABA NJEMA SI MABATI".lower())

print("jaba njema ni mabati".upper())

print("morio anzenza".endswith("anzenza"))

print("morio wa aba".endswith("wa"))

print("plankton secret formula".startswith('plankton'))

print('krabby patty secret formula'.startswith("patty"))

print('jaba fi life wayaseh'.replace("wayaseh",'yuhdunno'))

print("GUGULETHU".lower())
print("wena".upper())
print("vybz kartel".startswith("vybz"))
print("vybz kartel".endswith('kartel'))
print("hujuma,jaba,miti,kangeta".split(","))
print(",".join(["otto","von","bismark"]))
print("Piga punyeto mrazi acahchishe".replace("acahchishe","achachishe"))


h="jaba"
k=h.upper()
print(k)

print(max(2,3,4,5,6,7,8,9))
print(min(3,4,5,6,7,8,9))
print(abs(789))
print(abs(-67))
print(sum([3,4,5,4,3,2,1]))

r=4.12345
print(round(r,2))

print(round(9.2345,2))

p=min(sum([34,7]),max(abs(-40),39))
print(p)

jobo=[23,45,67,89,90,89,78,6,7]

if all(o>10 for o in jobo):
    print("masomaso")
else:
    print("haigwesi")

if any((o%2==0 for o in jobo)):
    print("punyeto")
else:
    print("ziii")
for b in enumerate(jobo):
    print(b)

for b in enumerate(jobo):
    print(b)


#slicing
tupuli=23,45,67,76,55,44,33,22,33,44,55,66
print(tupuli[2:6])

def func():
    p=4+3
    return p
print(func())


jumaa=55,44,33,22,11
print(max(min(jumaa[:2]),abs(-42)))

def gugu(h,j):
     hule=h+j
     return hule*(h/j)
print(gugu(6,8))

koko=[]
def dudu(j):
    return koko.append(j)
print(dudu(8))
print(koko)

loboskeske=lambda g:2*g*g
print(loboskeske(2))



def jiko(x):
    return x**3
print(jiko(8)-4)

h=lambda j:j**3
print(h(8)-4)

print((lambda y:y**3)(8)-4)

print((lambda x,y:x*y)(4,5)-4)

kiki=lambda f:f*3
koklo=lambda f,y:f*y
print(koklo(kiki(3),4))

print((lambda x,y:x*y)((lambda x:x+3)(5),7))

def define(h):
    return h*2
retan=[11,22,33,44]
joromi=list(map(define,retan))
print(joromi)

regroup=[90,89,78,67]
print(list(map(lambda x:x*2,regroup)))


bosi=[1,333,444,555]

print([n*2 for n in bosi])

jakoyo=[p*11 for p in range(1,6)]
print([p+5 for p in jakoyo][0])


jupita=[11,22,33,44,55]
print(list(filter(lambda x:x%2==0,jupita)))

hujuma=[11,22,45,67]
print([x for x in hujuma if x%2==0])

def doo(g):
    while g>0:
        g-=1
        return g
print(doo(9))

def difain(x):
   for i in range(x):
       if i%2==0:
           yield i
print(list(difain(10)))

print(list(x for x in range(13) if x%2==0))

print(list(filter((lambda x:x%2==0),range(1))))


def bloody():
    char=""
    for z in "neno la bwana":
        char+=z
        yield char
print(list(bloody()))

def hatutashindwa(funke):
    def bruh():
        print("==========")
        funke()
        print("==========")
    return bruh()
def dodo():
    print("printy")

print(hatutashindwa(dodo))

def sentensi():
    ju=""
    for w in "jina":
        ju+=w
        yield ju
print(list(sentensi()))

print(list(x for x in range(21) if x%2==1))

def cross():
    i=5
    while i>=-5:
        yield i
        i-=1
for i in cross():
    if i>0:
        print(i,15*" ","&")
    elif i==0:
        print(i,4*" ",10*"%","E",10*"%")
    else:
        print(i,14*" ","&")

print(cross())



def dui(u):
    if u==0:
        return True
    else:
        return dontdrinkndrive(u-1)
def dontdrinkndrive(u):
    return not dui(u)
punyeto={2,3,4,5,6}
polis=set(["bulshit","sauce"])

print("io" in punyeto)
print(90 not in polis)

kwekwekwe={1,3,5,7,9,5,2,7,9,4,2}
print(kwekwekwe)
kwekwekwe.add(-1000)
kwekwekwe.remove(9)
print(kwekwekwe)


guhu={1,2,3,4,5,4,3,2,1,2,3,4,5}
while len(guhu)>0:
    guhu.pop()
    print(guhu)

squid={1,2,3,4,5,6}
ward={7,8,9,6,5,4}

print(squid|ward)
print(squid&ward)
print(squid-ward)
print(ward-squid)
print(squid^ward)


list=["a","b","c"]
tuple=("a","b","c")#immutable....rest are mutable
dictionary={"a":23,"b":34,"c":45}
set={"a","b","c"}
set=set(["a","b","c"])