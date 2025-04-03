#Extract the given column from the csv files:
import csv

def given_col(col, input, output):
    
    with open (input, 'r', newline="") as infile:
        reader = csv.DictReader(infile)
        
        if col not in reader.fieldnames:
            print("Could not find: ",col)
            return
            
        with open (output, 'w', newline="") as outfile:
            writer = csv.writer(outfile)
            writer.writerow([col])
            
            for row in reader:
                writer.writerow([row[col]])
                
                
input_file = r"Question 5\sample.csv"
output_file = r"Question 5\result.csv"
column_name = "Name"
print(given_col(column_name, input_file, output_file))