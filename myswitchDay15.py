x=input("enter the value of x")

match x:
    case 0:
        print("you enter zero value")
    case 1:
        print("case is 1")
    case 2:
        print("you enter value of x is 2")
    
    case _ if x!=9:
        print("value of x is not equal to zero")
    case _:
        print("by default value")