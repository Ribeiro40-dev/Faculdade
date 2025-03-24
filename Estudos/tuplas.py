lanche = ('hambúrgue', 'suco', 'pizza', 'pudim')
'''print(lanche)
print (lanche[2])
print(lanche[-3])
print(lanche[2:])'''

#for cont in range(0, len(lanche)):
 #   print(f'Eu vou comer {lanche[cont]}')


#for c in lanche:
#   print(f'Eu vou comer {c}')


for pos, c in enumerate(lanche):
   print(f'Eu vou comer {c} na posição {pos}')
 

print('Estou satisfeito! ')