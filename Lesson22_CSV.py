# 1st example
import csv # importing the csv module

with open('example.csv') as csvfile: # so we don't have to close the file in the end
    readCSV = csv.reader(csvfile, delimiter=',') # we can use any delimiter
    # printing the data in the csvfile
    for row in readCSV:
        # printing all the columns
        print(row)
        # printing the first column
        print(row[0])
        # printing the first and the second columns
        print(row[0],row[1],row[2],)

# 2ed example
with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # creating empty lists to store the data in
    dates = []
    colors = []
    for row in readCSV:
        color = row[3] # the 4th element in each line of the original list is colour
        date = row[0] # the 1st element in each line of the original list is date
        # adding the elements into the lists we created above
        dates.append(date)
        colors.append(color)
    # printing the lists we just created
    print(dates)
    print(colors)

# 3ed example: simple application of matching idexs of two lists
    whatColor = input('What color do you wish to know the date of?:') # user's input
    coldex = colors.index(whatColor) # finding the index of the input given above
    theDate = dates[coldex] # using that index to find the matching index in 2ed list
    print('The date of',whatColor,'is:',theDate) # printing the answer