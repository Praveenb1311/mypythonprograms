
companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]


# define a sort key
def sort_key(company):
    return company[2]



# sort the companies by revenue
companies.sort(key=sort_key, reverse=True)

# show the sorted companies
print(companies)


a = "string"
value = a.find('i')
print(a.find('g'))
print(value)

print('t' in a)

s = ('This is my first program and program first consists of my first value and its benifits').split()
print(s)
p = max(set(s),key = s.count)

print(p)