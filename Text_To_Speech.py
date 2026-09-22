import os

while True:
    user = input("What do you want to say : ")
    if user == "exit":
        os.system(f"say Good Bye Sweetie")
        break
    command = f"say {user}"
    print(f"User: {user}")
    os.system(command);
    