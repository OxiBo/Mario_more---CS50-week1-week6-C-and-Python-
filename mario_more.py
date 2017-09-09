#print Mario piramid_less comfortable

def main():

    import cs50

    #get positive integer from a user (the height) greater than 0 lesser than 23
    while (True):
        print("height:", end="")
        height=cs50.get_int()
        if height>0 and height<23:
            break


    width=height-1 #creat a variable to remember amount of spaces to print in each row
    h=1 #create a variable to remember the amount of # to print in each row
    w=1 #create a variable to remember the amount of # to print in second half of double half-pyramid

    #iterate over each row
    for i in range(height):
        #print spaces in each row
        print(" "*width, end="")

        #print # in each row
        print("#"*h, end="")

        h+=1 #increment amount of # to print in the next row
        width-=1 #decrement amout of spaces to print in the next row

        print("  ", end="") #print 2 spaces between halfs of the half-pyramid

        #print second half of the half-pyramid
        print("#"*w, end="")

        w+=1 #increment amount of # in each row of the second half

        print () #print a new line



if __name__ == "__main__":
    main()








