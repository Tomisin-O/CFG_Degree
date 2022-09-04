chocolates = {

	'white': 1.50,

	'milk': 1.20,

	'dark': 1.80,

	'vegan': 2.00,

}
customer_choice = input('Choose your chocolate:')

for i in chocolates:
	if i == customer_choice:
		# print('true')
		print(chocolates[i])

# for i in chocolates:
# 	if i == customer_choice:
# 		# print('true')
# 		print(chocolates[i])