import sys
print(sys.version)

while True:
    user_input = input("Q: ").strip().lower()

    if user_input in ["exit", "quit", "goodbye", "bye"]:
        print("A: Goodbye")
        sys.exit(0)
    else:
        print("A:")