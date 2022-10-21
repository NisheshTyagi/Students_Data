
while True:
    Students = ["Nishesh","Anshika","Naincy","Geeta","Rajneesh"]
    exitcon = ["close","exit","Quit","quit","Exit","Close"]
    maxrn = len(Students)
    Marks = [100,2,100,100,100]
    uinnput = input("Enter Roll no of students : ")
    if uinnput in exitcon:
        break
    if uinnput.isdigit():
        if uinnput > "0" and uinnput < "6":
            rn = int(uinnput) - 1
            print(Students[rn]," : " , Marks[rn])
        else:
            print("Please enter a number between 1 and ",maxrn)
    else:
        print("Please enter a number between 1 and ",maxrn)
