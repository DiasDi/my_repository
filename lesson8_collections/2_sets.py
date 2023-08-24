countries_list = ['Brazil', 'India', 'China']
countries = set(countries_list)

print(type(countries_list))
print(type(countries))

empty_set = set()
emply_set = {}

print(countries_list)
print(countries)

alph = {'a', 'b', 'c', 'd'}
alph_2 = {'d', 'e', 'f', 'a'}
del alph[0]
print(type(alph))
print(alph)
print('a' in alph)

print(alph | alph_2) #unique
print(alph & alph_2) #not unique