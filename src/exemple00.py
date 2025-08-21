CONSTANTE_BONUS = 1000
nome_usuario = input("Olá, por gentileza digite seu nome: ")
salario_usuario = float(input("Insira o valor do seu salário: "))
bonus_usuario = float(input("Qual foi o percentual de bonus recebido? "))
valor_do_bonus = CONSTANTE_BONUS + salario_usuario*bonus_usuario
print(f"Olá {nome_usuario}! O seu valor bônus foi de {valor_do_bonus}")