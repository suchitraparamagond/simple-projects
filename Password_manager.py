import random
import string

password={}

try:
    with open("password.txt","r") as file:
        for line in file:
            website,pwd=line.strip().split(":")
            password[website]=pwd

except:
    pass

def generate_password():
    chars=string.ascii_letters+string.digits+"!@#&$%"
    password="".join(random.choice(chars) for _ in range(8))
    return password
while True:
    print("\n----PERSONAL PASSWORD MANAGER----")
    print("1.Save Password")
    print("2.View Password")
    print("3.Generate Password")
    print("4.Exit")

    choice=input("enter your choice:")

    if choice=="1":
        site=input("enter website:")
        pwd=input("enter your Password:")


        password[site]=pwd

        with open("password.txt","a") as file:
            file.write(f"{site}:{pwd}\n")

        print("saved!")

    elif choice=="2":
        if not password:
            print("no data")
        else:
            for site,pwd in password.items():
                print(site,":",pwd)

    elif choice=="3":
        print("Generated password", generate_password())

    elif choice=="4":
        print("ok bye..")
        break

    else:
        print("invalid input")