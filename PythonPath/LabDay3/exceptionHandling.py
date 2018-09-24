try:

    f = open('filename', "r")
    f.write("LionKing")

except:

    print("Something went wrong")

finally:

    f.close()
