def identity():

    nationality = ""
    age = 0
    first_name = ""
    second_name = ""
    third_name = False
    height = 0
    weight = 0
    born_place = ""
    languages = []
    sex = ""


    while sex == "":
        sex = input("What's your sex? ")

    while  first_name  == "":
        first_name = input("What's your first_name? ")

    while second_name == "":
        second_name = input("Enter your second name ")

    if third_name == True:
        third_name = input("Enter your third name ")

    while age == 0:
        try:
            age = int(input("How old are you? "))
        except:
            print("ERROR: something went wrong, try again")

    while height == 0:
        try:
            height = float(input("What size are you? "))
        except:
            print("ERROR: something went wrong, try again")
    
    while weight == 0:
        try:
            weight = float(input("How much do you weigh? "))
        except:
            print("ERROR: something went wrong, try again")
    
    while nationality == "":
        nationality = input('What is your nationality? ')

    while born_place == "":
        born_place = input('Where did you born? ')
    
    languages = input("What languages did you spoke? ")

    print("Sex :", sex)
    if third_name == False:    
        print("Name :", first_name, second_name)
    else:
        print("Name :", first_name, second_name, third_name)
    print(str(age), "years old")
    print("Height :", str(height), "weight :", str(weight))
    print("Born in", born_place, "nationality :", nationality)
    print("Languages :", languages)


identity()
    
            
    
