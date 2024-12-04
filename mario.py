
#coluna


Text = input("Escolha o material da COLUNA?")
n = int(input("Qual o tamanho da COLUNA?"))

while n > 0:
    print(Text) 
    n -= 1


#linha


Text = input("Escolha o material da LINHA")
n = int(input("Qual o tamanho da linha?"))

print(Text * n) 



#bloco

Text = input("Escolha o material da BLOCO?")
n = int(input("Qual o tamanho da BLOCO?"))
m = n
while n > 0:
    print(Text * m) 
    n -= 1
