t = [-4, -4, -3, -2, -2, -1, 0, 1, 2, 4, 6, 6, 7, 8, 8, 7, 6, 5, 4, 4, 3, 3, 2, -2]
#primul element din lista reprezinta temperatura la ora 1 dimineata.
print(round(sum(t)/24, 2))
print("Max t = ", max(t), "Min t = ", min(t))
n= max(t)
tmica = [index for index, value in enumerate(t) if value == n]
ore = [x+1 for x in tmica]
print("Temperatura cea mai inalta a fost la ora/orele ", ", ".join(map(str, ore)))
m = min(t)
tmare = [index for index, value in enumerate(t) if value == m]
orele = [x+1 for x in tmare]
print("Temperatura cea mai joasă a fost la ora/orele ", ", ".join(map(str, orele)))
#punctele e si f absolut nu le-am inteles, deoarece cum au aparut si zile, adica asta presupune sa se formeze 7 liste, fiecare sa aiba denumirea zilei si sa aiba temeperaturile sale? conditia spune clar ca avem o lista care reprezinta
#temepraturile timp de 24 de ore.