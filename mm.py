import csv
import logging


# moveMean takes a list as a parameter and returns a list [year, global moving average, local moving average]
def moveMean(l):
	return [ l['year'], round(l['G'] / l['count'], 2) , round(l['L'] / l['count'], 2) ]



logging.basicConfig(level=None)


# the number of years to take as a whole block, that is to count the moving average of a block-amount of years
block = 25


#open local_data csv file
fi = open('local_data.csv', 'r')
#create movingMean csv file
fo = open('_movingMean-' + str(block) + '-block.csv', 'w', newline='')

#start reading the csv data from fi
csvReader = csv.reader(fi)

#read field names
fieldnames = next(csvReader, None)

logging.debug(fieldnames)


#create a list to store the rows from the csv file
rows = list()

#store rows in the rows list
for row in csvReader:
	rows.append(row)




#number of rows
n = len(rows)

#variable to keep track of the years in a block
count = 0

#variable to keep track of the position where the for loop has reached in the rows list
pos = 0

#dictionary to keep information about the time block

tmp = {
	'year': 0, #start year of the block
	'G': 0, #sum of the global_avg
	'L': 0, #sum of the local_avg
	'count': 0, #how many years that are in a block, you may say why have this, isn't a block number constant?, it's because the last block may contain more years that are after it that are few and don't qualify as a block of their own
}


#create the csv writer to write to the csv output file
csvWriter = csv.writer(fo)

#write the headers to the csv output file
csvWriter.writerow(['Year', 'GLOBAL_AVG', 'LOCAL_AVG'])


#loop through the rows list and gather information about each block then call the movingMean function to get the moving mean of that block
for row in rows:

	#increase the position by one
	pos = pos + 1

	#deconstruct the row into three variables
	year, g, l = row


	#set the start year of the block only if we are at the beginning of the block i.e. count = 0
	if count == 0:
		tmp['year'] = year
	
	#add the global and local averages to the block information
	tmp['G'] = tmp['G'] + float(g)
	tmp['L'] = tmp['L'] + float(l)


	#increase the count by one
	count = count + 1



	#if ( the years in a block are completer AND the remaining years qualify for at least one block ) OR the position is at last i.e. n == pos, then process the information in this block
	if ( count % block == 0 and n - pos >= block ) or n == pos:

		#put the number of rows in this block
		tmp['count'] = count

		logging.debug(tmp)

		#calculate the moving mean of the block
		mm = moveMean(tmp)

		#write the block information to the csv output file
		csvWriter.writerow(mm)

		logging.debug(mm)

		#reset the tmp and the count
		tmp = {
			'year': 0,
			'G': 0,
			'L': 0,
			'count': 0
		}

		count = 0


#close files' streams
fi.close()
fo.close()

print("DONE")