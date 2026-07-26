while True:
    try:
        nilai = int(input("please enter your grade: "))

        if nilai >= 90:
            print(f"your grade {nilai} thats an A good job!")
        elif nilai >= 80:
            print(f" your grade {nilai} thats a B")
        elif nilai >= 70:
            print(f" your grade {nilai}  thats a C")
        elif nilai >= 60:
            print(f"your grade {nilai} thats a D")
        else:
            print(f"your grade {nilai} is a F please do the additional work to mark up your score and hand it out to my table!!")
        break
    except ValueError:
        print("please enter a number")     


