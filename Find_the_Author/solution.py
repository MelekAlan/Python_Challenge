with open("text1.txt", "r") as file1 :
    print(len([i for i in file1.read().split(".") if i != " "]))
