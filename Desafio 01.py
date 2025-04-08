# ≠======Digitar as horas e minutos=======≠#
hora = int(input("Digite a primeira hora: "))
minu = int(input("Digite o primeiro minuto: "))
hora2 = int(input("Digite a segunda hora: "))
minu2 = int(input("Digite o segundo minuto: "))
# ===============Calculos1==================$
Horas = (hora + hora2)
Minutos = (minu + minu2)
# if de calculos para compensar minutos em horas,e colocar horas em um sistema em 12 em 12 horas
if Minutos >= 60:
    Horas += Minutos // 60
    Minutos = Minutos % 60
    Horas = Horas % 12
    Minutos = Minutos
#if para colocar as horas ,se horas for maior que o resto de 12 que e 0,tudo
# que passar de 12 ele vai fazer oi sistema de 12 em 12 novamente.
if Horas % 12 == 0:

    H = Horas % 12

    print(f"{H:02d}:{Minutos:02d}")

else:
    print(f"{Horas:02d}:{Minutos:02d}")




