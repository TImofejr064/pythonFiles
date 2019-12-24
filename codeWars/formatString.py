def namelist(names):

	namess = ''
	
	if len(names) == 1:
		ab = names[0]
		namess += ab['name']
		return namess

	for i in range(0, len(names)):
		ab = names[i]
		namess += ab['name']
		if len(names) == 2 and i == 0:
			namess += ' & '
		elif len(names) == 2 and i == 1:
			break
		elif i == 0:
			namess += ', '
		elif i == len(names) - 2:
			namess += ' & '
		elif i == len(names) - 1:
			break
		else : 
			namess += ', '
	return namess

print(namelist([ {'name' : 'Bart'}, {'name' : 'Lisa'} ]))