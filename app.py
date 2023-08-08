def teste_palindromo(em_teste):
    em_teste = em_teste.lower() #coloca tudo em minúsculas
    em_teste = em_teste.replace(" ","") #remove espaços em branco
    em_teste_invertido = em_teste[::-1] #inverte a string

    return em_teste==em_teste_invertido #retorna V ou F para verificação se é palíndromo





print("Esse programa identifica se uma palavra ou frase é um palíndromo")
print("----------------------------------")
print("Vamos começar agora!")
print("----------------------------------")
novamente = "1"
while (novamente=="1"):
    testar = input("Digite uma palavra ou frase: ")
    if teste_palindromo(testar):
        print(f"{testar} é um palíndromo")
    else:
        print(f"{testar} não é um palíndromo")
    novamente = input("Deseja testar outra palavra? (1 para sim, qualquer tecla para não:) ")
else:
    print("Fim")