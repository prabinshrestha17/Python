# Write a function to find the smallest number in a list


myNumbers = [20, 30, 56, 90, 88, 45]


def smallestNumber(myNumbers):
    smallest = min(myNumbers)
    return smallest
output = smallestNumber(myNumbers)
print(output)






# WAP to list the nme of the countries

countries = ["Nepal", "North Korea", "Iserial", "America"]
def countCountries(countries):
    for i in range(len(countries)):
        print(countries[i])

output = countCountries(countries)
print(output)