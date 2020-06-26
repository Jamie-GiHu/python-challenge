import csv

# Store the file path for budget_data.csv
file = 'c:/Users/foong/Google Drive/PREWORK_JT/python-challenge/python-challenge JT submission/python-challenge/PyBank/Resources/budget_data.csv'

# Open the file in "read" mode and store the contents 
with open(file, 'r', newline='', ) as input_file:

    csvreader = csv.reader(input_file, delimiter = ',')

    # Read header in first row and skip reader
    header = next(csvreader)
    
    # Create dictionary as 'd'
    d = {}

    for row in csvreader:

        months = row[0]
        PL = row[1]
        d[months] = float(PL)
    
    # Total months can be found by calculating number of rows in dictionary
    total_month = len(d)
    
    # Net total amount of "Profit/Losses" over the entire period by adding all values in dictionary
    total_PL = sum(d.values())
    
    # Average of the changes in "Profit/Losses" over the entire period by converting dictionary to list
    total_previous_year_PL = sum(list(d.values())[0:len(d)-1])
    total_current_year_PL = sum(list(d.values())[1:len(d)])
    average_change = (total_current_year_PL - total_previous_year_PL)/(total_month -1)

    # Year on year changes to be added into a list
    total_change = list()
    i = 0 # Previous year position starting at first value in dictionary
    p = 1 # Current year position starting at second value in dictionary

    for row in d:       
        if p < total_month:
        
            total_change.append(list(d.values())[p] - list(d.values())[i])
            
            i += 1
            p += 1  
        pass # To avoid error message

    # Greatest increase in profits (amount) over the entire period by finding max value of list
    greatest_increase_amount = max(total_change)

    # Find the index position of the greatest increase in profits in the list
    greatest_increase_index = total_change.index(greatest_increase_amount) + 1 #add 1 to align with the month of the change

    # Search dictionary keys to find month based on matched list position
    greatest_increase_month = list(d.keys())[greatest_increase_index]

    # Greatest decrease in profits (amount) over the entire period by finding min value of list
    greatest_decrease_amount = min(total_change)

    # Find the index position of the greatest decrease in profits in the list
    greatest_decrease_index = total_change.index(greatest_decrease_amount) + 1

    # Search dictionary keys to find month based on matched list position
    greatest_decrease_month = list(d.keys())[greatest_decrease_index]

 # Print out the financial analysis results
    print(f"Financial Analysis")
    print(f"-" * 30)  
    print(f"Total Months: {total_month}")
    print(f"Total: ${int(total_PL)}")
    print(f"Average Change: ${round((average_change),2)}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${int(greatest_increase_amount)})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${int(greatest_decrease_amount)})")

# Set variable for output file
output_file = 'c:/Users/foong/Google Drive/PREWORK_JT/python-challenge/python-challenge JT submission/python-challenge/PyBank/analysis/financial_analysis.txt'

#  Open the output file
with open(output_file, "w") as writer:

    # Write in financial analysis results
    writer.write(f"Financial Analysis")
    writer.write("\n")
    writer.write(f"-" * 30)
    writer.write("\n")  
    writer.write(f"Total Months: {total_month}")
    writer.write("\n")
    writer.write(f"Total: ${int(total_PL)}")
    writer.write("\n")
    writer.write(f"Average Change: ${round((average_change),2)}")
    writer.write("\n")
    writer.write(f"Greatest Increase in Profits: {greatest_increase_month} (${int(greatest_increase_amount)})")
    writer.write("\n")
    writer.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${int(greatest_decrease_amount)})")
    writer.write("\n")