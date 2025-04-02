salário = float(input("Qual o salário do funcionário? R$"))
novo = salário + (salário * 15 / 100)
print("Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa areceber R${:.2f}".format(salário, novo))