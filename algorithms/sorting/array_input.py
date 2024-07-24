def arrayloader():
    try:
        array = []
        while True:
            array.append(int(input("Enter an element: ")))
    except:
        print(f"Your array is: {array}")
        return array