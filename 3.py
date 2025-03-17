#place de cinema
wallet = 0
age = input("quelle age avez vous")
if int(age) <=18 :
    print("ça vous fera 7€")
    wallet = +7
else:
    print("sa vous fera 12€")
    wallet = +12
pop_corn = input("souhaitez-vous du pop corn ?")
if pop_corn == 'oui':
    wallet += 5
    print("ça vous feras " + str(wallet)+"€")
elif pop_corn == 'non' :
    print("ça vous feras "+ str(wallet))
