#Match case

x =int(input("Enter a value from 1 to 100"))
match x:
    case 0:
        print("you choose zero")
    case 100:
        print("you choose 100")
    case _ if x!=0:
        print("this is a non zero num")
    # case _:  default case
    #     print("The number is not zero")
