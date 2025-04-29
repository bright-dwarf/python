greeting = input("Greeting: ").strip().lower()

if greeting.startswith("hello"):
    print("$100")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$0")
