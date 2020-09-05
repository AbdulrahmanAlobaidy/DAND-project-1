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

#initialize the variables and set them to None, this is not the starting value, g -> global, l -> local, diff -> difference
min_g = max_g = min_l = max_l = None

prev_l = prev_g = None

prev_year = None

g_g_diff = l_l_diff = min_g_g_diff = max_g_g_diff = min_l_l_diff = max_l_l_diff = None



min_g_year = max_g_year = min_l_year = max_l_year = min_diff_year = max_diff_year = min_g_g_year = max_g_g_year = min_l_l_year = max_l_l_year = None

diff = min_diff = max_diff = None

tmp = None

total_diff = total_g_g_diff = total_l_l_diff = 0

total_g = total_l = 0

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
		min_g_g_diff = min_l_l_diff = 999999
		max_g_g_diff = max_l_l_diff = -999999
		started = True
	else:
		g_g_diff = g - prev_g
		l_l_diff = l - prev_l

		total_g_g_diff = total_g_g_diff + g_g_diff
		total_l_l_diff = total_l_l_diff + l_l_diff

		tmp = min_g_g_diff

		min_g_g_diff = min(min_g_g_diff, g_g_diff)

		if min_g_g_diff != tmp:
			min_g_g_year = year

		tmp = max_g_g_diff

		max_g_g_diff = max(max_g_g_diff, g_g_diff)

		if max_g_g_diff != tmp:
			max_g_g_year = year


		tmp = min_l_l_diff

		min_l_l_diff = min(min_l_l_diff, l_l_diff)

		if min_l_l_diff != tmp:
			min_l_l_year = year

		tmp = max_l_l_diff

		max_l_l_diff = max(max_l_l_diff, l_l_diff)

		if max_l_l_diff != tmp:
			max_l_l_year = year

	#from here to the end of the loop block we calculate the variables and register their respective years

	total_g = total_g + g
	total_l = total_l + l

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


	prev_g = g
	prev_l = l

	prev_year = year

	rows.append(row)






#number of rows or years
n = len(rows)

#calculate averages
avg_g = total_g / n
avg_l = total_l / n

#calculate the average difference
avg_diff = total_diff / n

#calculate the average differences between years for both global and local, n - 1 not n is because the difference requires two points
avg_g_g_diff = total_g_g_diff / (n - 1)
avg_l_l_diff = total_l_l_diff / (n - 1)

#print the desired information
print('min_g', round(min_g, 2))
print('max_g', round(max_g, 2))
print('min_l', round(min_l, 2))
print('max_l', round(max_l, 2))
print('min_diff', round(min_diff, 2))
print('max_diff', round(max_diff, 2))
print('min_g_g_diff', round(min_g_g_diff, 2))
print('max_g_g_diff', round(max_g_g_diff, 2))
print('min_l_l_diff', round(min_l_l_diff, 2))
print('max_l_l_diff', round(max_l_l_diff, 2))


print('min_g_year', min_g_year)
print('max_g_year', max_g_year)
print('min_l_year', min_l_year)
print('max_l_year', max_l_year)
print('min_diff_year', min_diff_year)
print('max_diff_year', max_diff_year)
print('min_g_g_year', min_g_g_year)
print('max_g_g_year', max_g_g_year)
print('min_l_l_year', min_l_l_year)
print('max_l_l_year', max_l_l_year)

print('avg_g', round(avg_g, 2))
print('avg_l', round(avg_l, 2))
print('avg_diff', round(avg_diff, 2))
print('avg_g_g_diff', round(avg_g_g_diff, 2))
print('avg_l_l_diff', round(avg_l_l_diff, 2))

#close files' streams
fi.close()


print("DONE")