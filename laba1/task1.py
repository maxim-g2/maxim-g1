def Summa_Jewels():
    J = input("Введите jewels")
    S = input("Введите stones")
    jewels = set(J)
    print (sum(1
               for stone in S
               if stone in jewels
               ))

Summa_Jewels()