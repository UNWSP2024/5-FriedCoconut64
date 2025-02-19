def kilometer_conversion(kilometers):
    miles = 0.0
    miles = kilometers*0.6214

    return miles



if __name__ == '__main__':
    print("Kilometer Converter")
    kilometers = float(input("How many kilometers would you like to convert?:"))
miles = kilometer_conversion(kilometers)

print(kilometers,"kilometers is equal to",miles, "miles")

#Program #1, Donovan Thompson 02/19/25
