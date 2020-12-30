def vise():  # funkcije
    return 1, 2, 3, 4


t = vise()
x, _, _, y = vise()
print(t)
print(x, y)

niz = [1, 2, 3]


def func(x, y, z):
    print(x, y, z)


print(" ")
func(*niz)

print(" ")


def func1(arg=0, *args, **kwards):
    print(arg)
    for ar in args:
        print(ar)
    for k, v in kwards.items():
        print(k, v)


func1(2)
func1(0, 2, 4, 5, 6, neko="nesto", bul=False)

print(" ")


def izvrsi(fn, ar1, ar2):
    t = fn(ar1, ar2)
    print(t)


def saberi(x, y):
    return x + y


izvrsi(saberi, 1, 2)
izvrsi(lambda x, y: x + y, 1, 2)

with open("test.txt", 'w') as file:  # rad sa fajlovima preko kontekst menagera
    file.write("neki tekst\n")
    file.write("jos teksta")

with open("test.txt", 'r') as file:
    for line in file:
        print(line)

print(" ")


def krsh():  # eksepsni
    tmp = int(input('broj veci od 10: '))
    assert (tmp > 10), "mali bvroj"
    if tmp > 100:
        raise ValueError('value ne valja')
    print(tmp)


# try: #tray/catch
#     krsh()
# except AssertionError as e:
#     print(e)
# except ValueError:
#     print("greska")
# else:  # ima else koji se izvrsi ako nema greske
#     print("nema greske")
# finally:
#     print("konacno")

print(" ")
import modul as md  # import modula

print(md.zbir(1, 2))


def test():  # import unuitar funkcije
    from modul import hello
    hello('Pera')


test()
print(" ")


class Base:  # klase
    __attr1 = 10  # konvrncija je da imena sa dve donje crte su private

    def __init__(self, atr=15):  # konstruktor  self=this turaj inicijalizaciju u njega
        self.attr2 = atr

    def get_atr1(self):  # geteri koji nam kurcu ne trebaju
        return self.__attr1

    def get_attr2(self):
        return self.attr2

    @staticmethod  # pravljenje staticke metode
    def hello():
        print('hello')


b = Base(12)
print(b.get_atr1())
b.hello()
Base.hello()
b.attr2 = 5
print(b.attr2)

print(" ")  # izvedene klase


class Child(Base):
    def __init__(self):
        super(Child, self).__init__()
        self.attr3 = 7

    def get_atr2(self):
        print("nova")


c = Child()
print(c.attr2)
print(c.attr3)
das
