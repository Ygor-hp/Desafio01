hora =int(input("digite a hora: "))
minuto=int(input("digite os minutos: "))
hora2=int(input("digite a segunda hora:"))
minuto2=int(input("digite os minutos da segunda hora: "))
h=24-(hora+hora2)
m=minuto+minuto2-60
t=m%60
h1=h%25
if h1 == 13:
 t1=h1-1
 print(f"{t1}:{t}")
elif h1 == 7:
    t2=h1-1
    print(f"{t2}:{t}")
else:
    print(f"{h1}:{t}")




