marks = []

n = int(input("Ho many students?  "))


for i in range(n):
    mark = float(input(f"Enter the marks for the students {i+1}" ))
    marks.append(mark)

total = sum(marks)
avg = total/len(marks)
highest = max(marks)
lowest= min(marks)


print("-------\n Results ---------")
print("Mark list", marks)
print("Total Marks: ", marks)
print("Average:", avg)
print("Highest:", highest)
print("lowest", lowest)

# grade calculation 

if avg >=80:
    print("Geade: A")
elif avg >=70:
    print("Grade: B")
elif avg >= 60:
    print("Grade: C")
elif avg >=50:
    print("Grace: D")
else:
    print("Grade: failed")