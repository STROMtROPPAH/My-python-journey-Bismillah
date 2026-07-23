#add fuction + len
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add('Twitter')

print(len(it_companies))


#adding multiple using update
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies_after_deletion = {'Amazon', 'Microsoft', 'O.corp', 'Oracle', 'IBM', 'Surya.corp,G & corp', 'Apple'}
it_companies.update(['O.corp', 'Surya.corp', 'G & corp'])
it_companies.remove('Facebook')


print(it_companies)

#diffrernce fuction
print(f"oringinal companies: ", it_companies.difference(it_companies_after_deletion))
print(f"companies after deletion: ", it_companies_after_deletion.difference(it_companies))

