f = open("country.txt", "rt")
pop=0
country=0
for i in f:
    i = i.rstrip()
    j = i.split(',')
    lang = j[-1]
    contr = j[0]
    popu = int(j[1])
    if lang == 'English':
        pop=pop+popu
        country=country+1
print('There are {} countries who speak English with total population of {}.'.format(country,pop))