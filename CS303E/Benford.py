#File: Benford.py
#Description: Checks population statistics from a file to demonstrate Benford conjecture
#Student Name: Matthew Gmitro

def main():
    pop_num = []
    inFile = open ("Census 2009.txt", "r")
    count = 0
    for line in inFile:
        if (count == 0):
            count += 1
            continue
        else:
            count += 1
            line = line.strip()
            word_list = line.split()
            pop_num.append (word_list[-1])

    #create dictionary
    first = {}
    for i in range(1,10):
        first[str(i)] = 0

    #create dictionary values
    for item in pop_num:
        first[item[0]] = first[item[0]] + 1

    #summing counts
    countlist = list(first.values())
    sum = 0
    for item in countlist:
        sum = sum + item

    #print table
    print("Digit \t Count \t %")
    keylist = list(first.keys())
    keylist.sort()
    for i in range(len(keylist)):
        idx = str(keylist[i])
        num = int(first[idx]) / sum
        num = num * 100
        num = round(num, 1)
        print(str(keylist[i]) + "\t" + str(first[idx]) + "\t" + str(num))

    inFile.close()


main()
