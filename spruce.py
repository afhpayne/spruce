#!/usr/bin/env python3
# Andrew Payne, contact(*t)duckbrainsoftware(d*t)com

import csv
import os
import re
import readline
import shutil
import subprocess
import time

# Software information
soft_name = "spruce.py"
soft_tag  = "a handy tool for Alpine email."

# Software version 
soft_vers = "beta 0.6.2"

# Variables
user_home = os.environ['HOME']

# Email search string
re = re.compile(r'[\w\.-]+@[\w\.-]+')

# Lists
account_list = []
master_list  = []
email_list   = []

def print_main_func():
    os.system('clear')
    print("")
    print("Welcome to Spruce " + str(soft_vers) + ", " + str(soft_tag) + ".")

def print_sub_all_func():
    print("\n" + " "*4 + "(C)HOOSE AN ACCOUNT")
    print("\n" + " "*4 + "(I)MPORT CONTACTS")
    print("\n" + " "*4 + "(Q)UIT")

def print_sub_c_func():
    print("\n" + " "*4 + "(C)HOOSE AN ACCOUNT")
    print("\n" + " "*4 + "Here are the accounts in your .alpine folder:")
    print("")

def print_sub_i_func():
    print("\n" + " "*4 + "(C)HOOSE AN ACCOUNT")
    print("\n" + " "*4 + "(I)MPORT CONTACTS")
    print("")

def choose_account_func():
    for pinefile in os.listdir(os.path.join(user_home, ".alpine/")):
        if pinefile.startswith('pinercex'):
            account_list.append(pinefile)
    for pinercex in account_list:
        with open(os.path.join(user_home, ".alpine", pinercex)) as pinedoc:
            for line in pinedoc:
                email = re.search(line)
                if email is not None and [email.group(), pinercex] not in email_list:
                    email_list.append([email.group(), pinercex])
                    email_list.sort()
    email_dict = {}
    key = 1
    # Make a dictionary of tuples where [0] is the email and [1] is the pinercex file
    for email in email_list:
        email_dict.update({key:email})
        key += 1
        
    for key,email in email_dict.items():
        print(" "*8 + "[" + str(key) + "] " + email[0] + "\n")
    pick_num = 0
    while pick_num == 0:
        account_pick = input(" "*4 + "(Q)uit or enter a number: ")
        if account_pick == "q" or account_pick == "Q":
            pick_num = 1
            exit(0)
        elif account_pick.isnumeric() is False:
            continue
        else:
            pick_num = 1
            # Call a dictionary of tuples where [0] is the email and [1] is the pinercex file
            for key,email in email_dict.items():
                if key == int(account_pick):
                    shutil.copy2(os.path.join(user_home, ".alpine", email[1]), os.path.join(user_home, ".pinercex"))
                    subprocess.run(['alpine', '-passfile', os.path.join(user_home, '.pine-passfile')])
                    exit(0)

# Let's get started
os.system("clear")

print_main_func()
print_sub_all_func()

main_menu_loop = 0
while main_menu_loop == 0:
    main_menu = input("")
    if main_menu == "Q" or main_menu == 'q':
        exit(0)
    elif main_menu == "C" or main_menu == 'c':
        print_main_func()
        print_sub_c_func()
        choose_account_func()
        main_menu_loop = 1
    elif main_menu == "I" or main_menu == 'i':
        print_main_func()
        print_sub_i_func()
        print('subprocess.run(["goose.py", "--alpine"])')
        main_menu_loop = 1
        exit(0)
    else:
        print(main_menu + " is not an option ")
exit(0)
