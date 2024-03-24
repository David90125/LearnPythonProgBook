print("Chapter 3 second run through\n")

'''   # if elif pg 85-86
income=15000
if income < 10000:
    tax_coefficient = 0.0
elif income < 30000:
    tax_coefficient = 0.2
elif income < 100000:
    tax_coefficient = 0.35
else:
    tax_coefficient = 0.45
                                                                 # What gets printed.  Notice spacing on first one
print(f'You will pay: ${income * tax_coefficient} in taxes')     # You will pay: $3000.0 in taxes
print( 'You will pay: ${income * tax_coefficient} in taxes')     # You will pay: ${income * tax_coefficient} in taxes
print( 'You will pay: $', income * tax_coefficient, 'in taxes')  # You will pay: $ 3000.0 in taxes
'''

'''  #  The Ternary Operator  Pg 87-88
order_total = 247
discount = 25 if order_total > 100 else 0
print(order_total, discount)
'''
'''
#  Looping pg 88-
#  for() loop pg 88-95
for number in range(5):
    print(number, " Using range(5)")

for number in [1,2,3,4,5]:
    print(number, " Using list [1,2,3,4,5]")

for number in (1,2,3,4,5):
    print(number, " Using tuples (1,2,3,4,5)")

l=[1,2,3,4]
for number in l:
    print(number, "Using a predefined  list[1,2,3,4]" )
t=(1,2,3,4)
for number in t:
    print(number, "Using a predefined tuple(1,2,3,4)" )

surnames = ['Rivest', 'Shamir', 'Adleman']
for position in range(len(surnames)):
    print(position, surnames[position])

for position in range(len(surnames)):
    print(surnames[position][0], end='')  # Notice end= is used to get rid of the automatic <cr><lf>
print("\n")

for surname in surnames:
    print(surname, surname[0], surname[5])

for position, surname in enumerate(surnames):
    print(position, surname)


print(enumerate(surnames))

values = ["a", "b", "c"]
for count, value in enumerate(values, start=1):
     print(count, value)


values = ["a", "b", "c"]
for count, value in enumerate(values, start=5):
     print(count, value)


# pg 94  Multiple sequences implicitly
people=['Nick', 'Rick','Roger','Syd']
ages=[23, 24, 23, 21]
instruments=['Drums','Keyboards','Bass','Guitar']
for data in zip(people, ages, instruments):
    person, age, instrument = data
    print(person, age, instrument)
'''

'''
# while() loop pg 95-
n=69
remainders=[]
while n > 0:
    remainder = n%2
    remainders.append(remainder)
    n//=2
remainders.reverse()
print(remainders)

n=69
remainders=[]
while n > 0:
    n, remainder = divmod(n,2)
    remainders.append(remainder)
remainders.reverse()
print(remainders)

n=69
print(bin(n))
print(hex(n))
'''
'''
customers = [
    dict(id='aaa', total=200, coupon_code='F20'),
    dict(id=2, total=150, coupon_code='P30'),
    dict(id='ccc', total=100, coupon_code='P50'),
    dict(id=4, total=110, coupon_code='F15'),
] 

for customer in customers:
    code = customer['coupon_code']
    if code == 'F20':
        customer['discount'] = 20.0
    elif code == 'F15':
        customer['discount'] = 15.0
    elif code == 'P30':
        customer['discount'] = customer['total'] * 0.3
    elif code == 'P50':
        customer['discount'] = customer['total'] * 0.5
    else:
        customer['discount'] = 0.0
for customer in customers:
    print(customer['id'], customer['total'], customer['discount'])
print(" ")

discounts = {  # I experimented by rearranging the order of this dictionary and it still worked
    'F20': (0.0, 20.0),'F15': (0.0, 15.0),
    'P50': (0.5, 0.0),'P30': (0.3, 0.0),
}

for customer in customers:
    code = customer['coupon_code']
    percent, fixed = discounts.get(code, (0.0, 0.0))
    customer['discount'] = percent * customer['total'] + fixed

for customer in customers:
    print(customer['id'], customer['total'], customer['discount'])
'''

# pg 111
from itertools import count
for n in count(5,3):
    if n > 20:
        break
    print(n, end=', ')   # instead of newline, comma and space






print("\n\nEnd of exercise")
