import numpy as np
from numpy import *

#This program imports data using the numpy function genfromtxt('file.csv') which reads and converts .csv files into a single numpy array. It then randomizes the data set before dividing the data into Training, Cross Validtion and Testing data sets. Thus the numpy function ```numpy.random.shuffle(arr)``` was used to shuffle the data by rows while leaving the contents of each row unshifted.

#The divided datasets are then stored into their respective .dat files, which was made possible through the use of the function savetxt('file.dat')

def divide(csv):
    
    try:
        #Load dataset
        data = np.genfromtxt(csv,delimiter=",")

        #Randomize dataset
        np.random.shuffle(data)

        #sets the ratio of [training data : validation data : testing data] 
        #It is currently set to 80:10:10
        perc1= int(0.6*len(data))
        perc2= int(0.8*len(data))

        #Divides dataset into training, validation and testing datasets
        train = data2[:perc1]
        val = data2[perc1:perc2]
        test = data2[perc2:]

        #writes the arrays into their respective files
        savetxt('train.dat', train)
        savetxt('cv.dat', val)
        savetxt('test.dat', test)

        return "SUCCESS"
   
    except:
        return "ALERT! Dataset does not exist."
    
def main():
    
    file = input("Please enter the name of the dataset. (.csv excluded)")
    file = file + ".csv"
    message = divide(file)
    print(message)
    
if __name__== "__main__":
    main()
