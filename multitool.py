import requests
import os
import json

logo = """

\033[0;35m █████ █████ █████  █████ ███████████   █████████      ███████████                   ████ 
░░███ ░░███ ░░███  ░░███ ░█░░░░░░███   ███░░░░░███    ░█░░░███░░░█                  ░░███ 
 ░░███ ███   ░███   ░███ ░     ███░   ░███    ░███    ░   ░███  ░   ██████   ██████  ░███ 
  ░░█████    ░███   ░███      ███     ░███████████        ░███     ███░░███ ███░░███ ░███ 
   ░░███     ░███   ░███     ███      ░███░░░░░███        ░███    ░███ ░███░███ ░███ ░███ 
    ░███     ░███   ░███   ████     █ ░███    ░███        ░███    ░███ ░███░███ ░███ ░███ 
    █████    ░░████████   ███████████ █████   █████       █████   ░░██████ ░░██████  █████
   ░░░░░      ░░░░░░░░   ░░░░░░░░░░░ ░░░░░   ░░░░░       ░░░░░     ░░░░░░   ░░░░░░  ░░░░░ 
                                                                                        
"""



while True:
    os.system("title Yuza Tool")
    os.system("cls")
    print(logo)
    print("[1] Ip Lookup")
    print("[2] Webhook Sender")
    print("[3] Show HWID")
    print("")
    x = input("Option: ")

    if x == "1":
         os.system("cls")
         print("\033[0;35mIP LOOKUP\n")
         ip = input("Enter IP: ")
         os.system("cls")
         r = requests.get(f"http://ip-api.com/json/{ip}")
         data = r.json()
         print("RESULTS\n")
         print(f"\033[0;35mCountry: \033[0;35m{data["Country"]}")
         print(f"\033[0;35mCity: \033[0;35m{data["City"]}")
         print(f"\033[0;35mRegion: \033[0;35m{data["regionName"]}")
         print(f"\033[0;35mTimeZone: \033[0;35m{data["timezone"]}")
         print(f"\033[0;35mRegion: \033[0;35m{data["regionName"]}")
         print("")
         pause = input("Press enter to return...")


    if x == "2":
         os.system("cls")
         print("\033[0;35mWEBHOOK SENDER\n")
         url = input("Webhook URL: \033[0;35m")
         message = input("Message: \033[0;35m")
         name = input("Webhook Name: \033[0;35m")


         data = {
              "content": message,
              "username": name
         }

         try: 
             r = requests.post(url, json=data)
             print("Webhook Sent!")
         except:
              print("ERROR SENDING WEBHOOK")

         print()
         pause = input("Press enter to return...")

         if x == "3":
              os.system("cls")
              print("\033[0;35mHardware ID\n")

              print("\033[0;35mCPU Serial\033[0;35m")
              print(os.system("wimic cpu get ProcessorID"))

              print("\033[0;35mDisk Serial\033[0;35m")
              print(os.system("wmic diskdrive get SerialNumber"))

              print("\033[0;35mMotherboard Serial\033[0;35m")
              print(os.system("wmic baseboard get SerialNumber"))
              print()
              pause = input("Press enter to return...")


         else:
              os.system("cls")
              print("\033[0;35mInvalid Option\n")
              pause = input("Press enter to return...")