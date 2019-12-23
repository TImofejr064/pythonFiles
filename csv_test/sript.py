import csv



with open('new_csv_file.csv', 'w') as new_file:

	fieldnames = ['field_name', 'field_lastname', 'field_email']

	csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='-')

	csv_writer.writeheader()

	csv_writer.writerow({'field_name' : 'Timur', 'field_lastname' : 'Bogdalov', 'field_email' : 'useremail@gmail.com'})
	csv_writer.writerow({'field_name' : 'Timur', 'field_lastname' : 'Bogdadlov', 'field_email' : 'useremail@gmail.com'})