studentMarks = [30, 40, 50, 35, 45, 50]

def averageCalculation(markList):
    average = sum(markList)/len(markList)
    return average 
result = averageCalculation(studentMarks)
print("Average is: ",round(result, 2) )