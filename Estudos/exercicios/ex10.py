real = float(input("Quanto dinheiro tem na carteira? "))
dolar = real / 5.80
print("Com R${} vocE pode comprar US${:.2f }, ".format(real,dolar))