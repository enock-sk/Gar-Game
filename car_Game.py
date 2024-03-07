started=False
command=""
while True:
    command=input(">").lower()
    if command=="start":
        if started:
            print("car is already started")
        else:
            started=True
        print("Car Started")
    elif command=="stop":
        if not started:
            print("car is already stopped")
        else:
            started=False
        print("Car stopped")
    elif command=="help":
        print("""
start -to start the car
stop - to stop the car
quit - to quit
        """)
    elif command=="quit":
        break
    else:
        print("we dont understand that")


