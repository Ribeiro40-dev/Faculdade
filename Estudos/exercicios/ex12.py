preço = float(input("Qual opreço do produto? R$"))
novo = preço - (preço * 5 / 100)
print("O produto que custava R${}, com desconto de 5% vai custar R${}".format(preço, novo))