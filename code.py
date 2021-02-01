# DNA barcodes

import random

#function compares the indexes of two strings to determine the hamming distance
def hamming1(string1, string2):
    global d #to be used in def hamming
    d = 0
    i = 0
    while i<len(string1):
        if string1[i] != string2[i]: 
            d+=1
            i+=1
        else:     
            i+=1
    return(d)

#creates a file and inputs the requested amount/lengths of barcodes
def create_file(sequence5):
    f = open("dnafile.txt", 'w')
    a = 1
    i = 0
    while i < n:
        f.write("barcode" + " " + str(a)+ ":" + sequence5[i] + "\n")
        i +=1
        a+=1
    f.close()

#function determines hamming distance for all strings in the dna sequence list
def hamming(sequence4):
    finalsequence = []
    size = len(sequence4)
    i = 0
    while i<(size-1):
        hamming1(sequence4[i], sequence4[i+1]) #compares all strings of the list using def hamming1
        if d >= 3: #d = hamming distance
            finalsequence.append(sequence4[i])
            i+=1
        else:
            i+=1
    create_file(finalsequence)

#function excludes the restricted barcodes from the dna sequence list
def restrictions(sequence3):
    sequence4 = []
    for i in sequence3:
        if i != "ACCGGT" and i != "GGCGCGCC" and i != "GGATCC" and i != "CCTGCAGG":
            sequence4.append(i)
    hamming(sequence4)

#function excludes barcodes with 3 or more of the same nucleotides repeated consecutively
def repeated(sequence2):
    sequence3 = []
    for i in sequence2:
        if i.count("G")<3 and i.count("C") <3 and i.count("A")<3 and i.count("T")<3:
           sequence3.append(i)
    restrictions(sequence3)

#function makes sure all barcodes have GC-content from 40 to 60 percent
def GC_content(sequence):
    sequence2 = []
    for i in sequence:
        total = len(i)
        c = i.count("C")
        g = i.count("G")
        if ((g+c)/total) * 100 >= 40 and ((g+c)/total) * 100 <= 60:
            sequence2.append(i)
    repeated(sequence2)

#recieves the requested size and amount of barcodes and organizes it into a list of strings(barcodes)
def strings(n, size):
    DNA = ["A", "T", "G", "C"]
    dnalist = ""
    for i in range(n*5): #comes up with a list of a single, large string of barcodes (using amount of from size in range of n*5
        for element in range(0, size): 
            dnalist+=random.choice(DNA)
    sequence = []
    for i in range(0, len(dnalist), size):
        sequence.append(dnalist[i:i+size]) #splits up the string according to size
    GC_content(sequence)

#asks the user for input     
def main():
    global n
    n = int(input("How many sequences of DNA barcodes?:"))
    size = int(input("What is the length of each DNA barcode?:"))
    strings(n, size)


main()



    
    
    
