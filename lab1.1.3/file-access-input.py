file = open ("devices.txt", "a")
while True:
    Newitem = input("Enter device name: ")
    if Newitem == "exit":
        print("All done!")
    break

file.write(Newitem + "\n")
file.close()
