names = ("Abid", "Qasim", "Adil", "Zaheer", "Asad")
ages = (23, 38, 36, 26, 32)
companies = ("Teradata", "Ciklum", "Ciklum", "Freelancing", "Nust")

myzip = zip(names, ages, companies)

for (a, b, c) in myzip:
    print(a, " is ", b, " years old & works at ", c)