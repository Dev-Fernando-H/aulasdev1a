N1 = float(input("Digite um NUMERO!"))
Op = input ("Digite uma OPERAÇÃO!")
N2 = float(input("Digite outro NUMERO!"))
Rs = ""
if Op == "+":
    Rs = N1 + N2
    Rs = f"{Rs:_.2f}"
    print (f"O resultado dessa soma é" , Rs . replace(".",",").replace("_","."))
elif Op == "-":
    Rs = N1 - N2
    Rs = f"{Rs:_.2f}"
    print (f"O resultado dessa subtração é" , Rs . replace(".",",").replace("_","."))
elif Op == "*":
    Rs = N1 * N2
    Rs = f"{Rs:_.2f}"
    print (f"O resultado dessa multiplicação é," , Rs . replace(".",",").replace("_","."))
elif Op == "/":
    
    Rs = N1 / N2
    
    #definir a equação da função primeiro
    
    Rs = f"{Rs:_.2f}"
    
    #definir o "." como "_"
    
    print (f"O resultado dessa divisão é," , Rs . replace(".",",").replace("_","."))

'''
    mostrar o resultado trocando todos os pontos de Ex: 1.50 (um e meio em ingles) 
    pelo formato brasileiro (1,50) e troca novamente o "_" por "." para ficar 1.500 ao em vez de 1_500
'''
