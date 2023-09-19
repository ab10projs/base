a= int(input("a: "))
counter =0
while (counter<=a):
    print(counter)
    counter+= 1
    if counter==5:
        print("before break")
        #break
        print("break")
        break
        print("this was after continue which was not printed")

    print("outside loop11")