try:
    f = open('filename', "a")
    f.write("LionKing")
except:
    print("Something went wrong")
finally:
    f.close()
