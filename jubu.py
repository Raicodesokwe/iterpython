from itertools import takewhile,accumulate,chain,permutations,product

print(list(accumulate(range(8))))
print(list(takewhile(lambda x:x<=6,range(8))))


print(list(chain(["mawe","punyeto"],[1,2])))

def rudia():
    tu=[0]
    for g in range(9):
        tu.append(g+tu[g])
    return tu
print(rudia())
nums=2,3,4,5,6,7
print(list(takewhile(lambda x:x%2==0,range(2))))
biticha=("kwa","do","tu")
print(list(product(("a","b","c","d"),range(2))))
print(list(permutations(biticha,3)))

d=(2,3)
print(len(list(product(d,range(3))))-1)


class Distone:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

diablo=Distone("mawe",2,"M")
Simbithi=Distone("Quasar",3,"F")
wepukhulu=Distone("Blackhole",4,"N.B")

print(diablo.name)
print(Simbithi.age)


class wuhan:
    def __init__(self,mawe,stone):
        self.mawe=mawe
        self.stone=stone
juanita=wuhan("sulei","mawe")
print(juanita.stone)

class tambua:
    def __init__(endelea,jaba,taxin):
        endelea.jaba=jaba
        endelea.taxin=taxin
    def fucktion(endelea):
        print("alutaaaa!!!")
godana=tambua("kangeta","medium")
print(godana.taxin)
godana.fucktion()


class sirikali:
    miaka=4
    def __init__(self,colour,shape):
        self.colour=colour
        self.shape=shape
    def newFunc(self):
        print("pokot!!!")

mungai=sirikali("red","round")
print(mungai.shape)
mungai.newFunc()
print(sirikali.miaka)
print(mungai.miaka)

class darasa:
    def __init__(self,name,size):
        self.name=name
        self.size=size
class mbesha(darasa):
    def kirasi(self):
        print("ouuuuuuu!!!!")
libidough=mbesha("Murai",56)
print(libidough.name+' likes a '+str(libidough.size)+" inch booory")
libidough.kirasi()

class classy:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def maweism(self):
        print("wololooo")
class Wille(classy):

    def maweism(self):
        print("bombofuck!!!!")

juniper=Wille("Murai",90)
juniper.maweism()

class A:
    def supa(self):
        print("konyweee")
class B(A):
    def supa(self):
        print("kinyes")
class C(B):
    def supa(self):
        print("konyaG")
        super().supa()

C().supa()


class gugulet:
    def __init__(self,m):
        self.m=m
    def __mul__(self, other):
        return self.m/other.m
wan=gugulet(9)
tu=gugulet(4)
print(wan*tu)

class juis:
    def __init__(self,ki):
        self.ki=ki
    def __truediv__(self, other):
        spacetime="*" * len(other.ki)
        return "\n".join([self.ki,spacetime,other.ki])
one=juis("hello")
two=juis("bruhman")
print(one/two)

class klassee:
     def __init__(self,con):
         self.con=con

     def __gt__(self, other):
         for i in range(len(other.con)+1):
             sababisha= other.con[:i]+">"+self.con+">"+other.con[i:]
             print(sababisha)
kunye=klassee("fudhi")
fudhi=klassee("kunye")

kunye>fudhi
