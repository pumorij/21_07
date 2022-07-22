
l=['m','n']
n=3

new_l=['{}{}'.format(x,y) for y in range(1,n+1) for x in l]
print(new_l)