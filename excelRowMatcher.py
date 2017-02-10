import csv

def get_dict_from_CSV(string):
    """A function to parse a comma separated value file into a dictionary
       Returns:
           A dicionary with
               keys: first row of csv
               values: columns associated with rows 
    """
    return_dict = {}
    ##return_dict = {'Date': [], 'Volume' : [], 'High' : [], 'Adj Close': [], 'Volume' : [], 'Low': [], 'Close' : [], 'Open' : []   }
    with open(string, mode ='r') as csvfile:
        reader = csv.DictReader(csvfile) #returns a sequence of dictionaries
        for row in reader:
            for key, value in row.items():
                if key in return_dict:
                    #print ('already here')
                    return_dict[key].append(value)
                else:
                    return_dict[key]= []
                    #print ("now it exists")
    return return_dict

def get_rows_from_CSV(string):
    """
        A function to parse a comma separated value file into a list of lists
        Returns:
            a list with
                each index represents a row in the CSV
    """
    ret = []
    with open(string, 'rb') as csvfile:
        fileReader = csv.reader(csvfile, delimiter=' ',quotechar='|')
        for row in fileReader:
            print" ".join(row)
            ret.append(row)
    return ret

def match_rows(arrayFromCSV):
    """
    A function to match rows of a CSV
    
    """
    ret_dict = {}
    x = 0
    while x < len(arrayFromCSV):
        y = 0
        while y < len(arrayFromCSV):
            if x == y:
                y = y + 1
                continue
            if (arrayFromCSV[x] == arrayFromCSV[y]):
                print (arrayFromCSV[x])
                print ("occurs at rows " + str(x) + " and " + str(y))
            y = y + 1
        x = x + 1
    print ("if nothing was output, then there were no matching rows.")
