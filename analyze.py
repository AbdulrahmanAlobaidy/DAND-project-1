import csv
import logging


logging.basicConfig(level=logging.DEBUG)


#open local_data csv file
fi = open('comparison.csv', 'r')

#start reading the csv data from fi
csvReader = csv.reader(fi)

#read field names
fieldnames = next(csvReader, None)

logging.debug(fieldnames)


#create a list to store the rows from the csv file
rows = list()

#variable to indicate whether the varibales are set with a starting value or not, False for not
started = False

#initialize the variables and set them to None, this is not the starting value
min_g = max_g = min_l = max_l = None

min_g_year = max_g_year = min_l_year = max_l_year = min_diff_year = max_diff_year = None

diff = min_diff = max_diff = None

tmp = None

total_diff = 0

#store rows in the rows list
for row in csvReader:

	#deconstruct the row into three variables
	year, g, l = row

	g = float(g)
	l = float(l)

	#calculate the difference for this year
	diff = abs(g - l)

	#add it to the total difference
	total_diff = total_diff + diff

	#if the variables are still None, then set them with starting values
	if not started:
		min_g = max_g = g
		min_l = max_l = l
		min_diff = max_diff = diff
		started = True


	#from here to the end of the loop block we calculate the variables and register their respective years

	tmp = min_g

	min_g = min(min_g, g)

	if min_g != tmp:
		min_g_year = year

	tmp = max_g

	max_g = max(max_g, g)

	if max_g != tmp:
		max_g_year = year

	tmp = min_l

	min_l = min(min_l, l)

	if min_l != tmp:
		min_l_year = year


	tmp = max_l

	max_l = max(max_l, l)

	if max_l != tmp:
		max_l_year = year


	tmp = min_diff

	min_diff = min(min_diff, diff)

	if min_diff != tmp:
		min_diff_year = year


	tmp = max_diff_year

	max_diff = max(max_diff, diff)

	if max_diff != tmp:
		max_diff_year = year

	rows.append(row)


#number of rows or years
n = len(rows)

#calculate the average difference
avg_diff = total_diff / n

#print the desired information
print('min_g', round(min_g, 2))
print('max_g', round(max_g, 2))
print('min_l', round(min_l, 2))
print('max_l', round(max_l, 2))
print('min_diff', round(min_diff, 2))
print('max_diff', round(max_diff, 2))

print('min_g_year', min_g_year)
print('max_g_year', max_g_year)
print('min_l_year', min_l_year)
print('max_l_year', max_l_year)
print('min_diff_year', min_diff_year)
print('max_diff_year', max_diff_year)

print('avg_diff', round(avg_diff, 2))


#close files' streams
fi.close()


print("DONE")