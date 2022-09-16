with open ("poems.txt","r")as f:
    if ("twinkle"in f.read()):
        print("Yes twinkle is present")
    else:
        print("Twinkle is not present")