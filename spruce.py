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
soft_tag  = "a handy tool for Alpine email"

# Software version 
soft_vers = "beta 0.5.2"

user_home = os.environ['HOME']

re = re.compile(r'[\w\.-]+@[\w\.-]+')
account_list = []
master_list  = []
email_list   = []
key = 1

def user_nag_func():
    user_nag=input("Continue? y/n ")
    if user_nag == 'Y' or user_nag == 'y':
        stay_main=0
        stay_c=0
        stay_i=0
        main_menu=''
    else:
        exit()

def print_main_func():
    os.system('clear')
    print("")
    print("Welcome to Spruce " + str(soft_vers) + ", " + str(soft_tag) + ".")
    print("\n\t(C)HOOSE AN ACCOUNT")
    print("\n\t(I)MPORT CONTACTS")
    print("\n\t(Q)UIT")
    
stay_main=1
while stay_main == 1:
    print_main_func()
    main_menu = input("")

    if main_menu == "Q" or main_menu == 'q':
        exit()
    
    if main_menu == "C" or main_menu == 'c':
        stay_c = 1
        while stay_c == 1:
            for pinercex in os.listdir(os.path.join(user_home, ".alpine/")):
                if pinercex.startswith('pinercex'):
                    account_list.append(pinercex)
                    account_list.sort()

            for item in account_list:
                with open(os.path.join("/home/andrew/.alpine", item)) as document:
                    for line in document:
                        email = re.search(line)
                        if email:
                            email.group()
                            if email.group() not in email_list:
                                email_list.append("[")
                                email_list.append(key)
                                email_list.append("] ")
                                email_list.append(email.group())
                                email_list.append("\n")
                                key += 1
                                master_list.append(item)
                                master_list.append(email.group())
            print_main_func()
            print("\nHere are the accounts in your .alpine folder: \n")
            print(''.join(map(str, email_list)))
            usr_num = input("\nPlease enter a number: ")
            if usr_num == 'C' or usr_num == 'c':
                break
            if usr_num == 'I' or usr_num == 'i':
                break
            if usr_num == 'Q' or usr_num == 'q':
                exit()
            try:
                x = (email_list.index(int(usr_num))) + 2
                account = email_list[x]
                
                y = (master_list.index(account)) - 1
                file_name = master_list[y]
            
                shutil.copy2(os.path.join(user_home, ".alpine", file_name), os.path.join(user_home, ".pinercex"))
                subprocess.run(['alpine', '-passfile', os.path.join(user_home, '.pine-passfile')])
                exit()
            except ValueError:
                print(usr_num + " is not an option\n")
                time.sleep(1)
    
    if main_menu == "I" or main_menu == 'i':
        stay_i=1
        while stay_i == 1:

            # START SPRUCE COMPATIBLE CODE HERE
            # User filenames - CHANGE THIS HERE! subsequent code will follow these names
            userfile_alp = 'addressbook'
            userfile_mutt = 'aliases'
            
            # User file locations
            alpine_original = os.path.join(user_home, '.alpine', userfile_alp) 
            mutt_original   = os.path.join(user_home, '.mutt', userfile_mutt) 
            
            # Temp file locations
            alpine_temp = os.path.join('/tmp', userfile_alp)
            mutt_temp   = os.path.join('/tmp', userfile_mutt)
            
            # Check for current files
            print_main_func()
            mutt_or_alp = input("\nImport to (A)lpine, (M)utt, (B)oth, or (Q)uit? ")
            if mutt_or_alp == 'Q' or mutt_or_alp == 'q':
                os.system('clear')
                exit()
            if mutt_or_alp == 'A' or mutt_or_alp == 'a':
                if os.path.isfile(alpine_original):
                    pass
                else:
                    print("\nNo current Alpine addressbook found.  Default is " + os.path.join(alpine_original))
            if mutt_or_alp == 'M' or mutt_or_alp == 'm':
                if os.path.isfile(mutt_original):
                    pass
                else:
                    print("\nNo current Mutt aliases found.  Default is " + os.path.join(mutt_original))
            if mutt_or_alp == 'B' or mutt_or_alp == 'b':
                if os.path.isfile(alpine_original) is False:
                    print("\nNo current Alpine addressbook found.  Default is " + os.path.join(alpine_original))
                if os.path.isfile(mutt_original) is False:
                    print("\nNo current Mutt aliases found.  Default is " + os.path.join(mutt_original))
                else:
                    pass
            if mutt_or_alp not in {"A", "a", "M", "m", "B", "b"}:
                print("\n" + mutt_or_alp + " is not an option")
                time.sleep(1)
                continue
        
        
            # Google export check
            if os.path.isfile(os.path.join(user_home, "Downloads", "google.csv")):
                google_export = (os.path.join(user_home, "Downloads", "google.csv"))
                print("\nImport from " + os.path.join(user_home, "Downloads", "google.csv"))
                user_nag = input("\ny/n: ")
                if user_nag == 'Y' or user_nag == 'y':
                    pass
                else:
                    exit()
            elif os.path.isfile(os.path.join(user_home, "Downloads", "contacts.csv")):
                google_export = (os.path.join(user_home, "Downloads", "contacts.csv"))
                print("\nImport from" + os.path.join(user_home, "Downloads", "contacts.csv"))
                user_nag = input("\ny/n: ")
                if user_nag == 'Y' or user_nag == 'y':
                    pass
                else:
                    exit()
            else:
                print("Can't find csv to import - google.csv or contacts.csv should be in your Dowloads folder.")
                exit()
            
            # Lists
            global nick_list
            nick_list = []
            
            # This is for exception handling
            def extract_names_func():
                global first_name
                global last_name
                global nick_name
                global email_addr
                global email_addr1
                global email_addr2
                global email_addr3
                global company_name
                # First but no last
                if first_name != '' and last_name == '':
                    if company_name:
                        nick_name = company_name[0:15].lower().replace(" ", "_").replace(".", "")
                        first_name = first_name.split("@")[0]
                        last_name = ("(" + email_addr.split("@")[1].split(".")[0] + ")")
                    else:
                        nick_name  = (first_name).strip().lower().replace(".","").replace(" ","_")
                        first_name = (email_addr).split("@")[0]
                        last_name  = ("(" + (email_addr.split("@")[1]).split(".")[0] + ")") 
                # Last but no first
                elif first_name == '' and last_name != '':
                    nick_name  = (last_name).strip().lower().replace("'","")
                    first_name = "_" 
                # Neither
                elif first_name == '' and last_name == '':
                    if company_name:
                        nick_name = company_name[0:15].lower().replace(" ", "_").replace(".", "")
                        first_name = email_addr.split("@")[0].replace(".", "")
                        last_name  = ("(" + (email_addr.split("@")[1]).split(".")[0] + ")")
                    else:
                        nick_name  = email_addr.split("@")[0].replace(".", "") 
                        first_name = email_addr.split("@")[0].replace(".", "")
                        last_name  = ("(" + (email_addr.split("@")[1]).split(".")[0] + ")")
                # Both names present
                else:
                    first_name = first_name.replace(".", "")
                    nick_name  = (first_name.strip().lower().replace(".","").replace(" ","_") + "_" + last_name.strip()).lower().replace("'","")
            
            
            # Backup existing files
            if os.path.isfile(alpine_original):
                shutil.copy2(alpine_original, "/tmp")
                os.rename(os.path.join("/tmp", userfile_alp), os.path.join("/tmp", userfile_alp) + "_" + str(time.monotonic()))
            if os.path.isfile(mutt_original):
                shutil.copy2(mutt_original, "/tmp")
                os.rename(os.path.join("/tmp", userfile_mutt), os.path.join("/tmp", userfile_mutt) + "_" + str(time.monotonic()))
            
            with open(google_export) as contacts_csv:
                with open(alpine_temp, "a") as alpine_out, open(mutt_temp, "a") as mutt_out:
                    reader = csv.reader(contacts_csv, delimiter=',')
                    firstline = True
                    for r, row in enumerate(reader):
                        for c, column in enumerate(row):
                            if "Given Name" in column and "Yomi" not in column or "First Name" in column:
                                first_name_index = (c)
                            if "Family Name" in column and "Yomi" not in column or "Last Name" in column:
                                last_name_index = (c)
                            if "E-mail 1 - Value" in column and "Yomi" not in column or "E-mail Address" in column:
                                email_loc1_index = (c)
                            if "E-mail 2 - Value" in column and "Yomi" not in column or "E-mail 2 Address" in column:
                                email_loc2_index = (c)
                            if "E-mail 3 - Value" in column and "Yomi" not in column or "E-mail 3 Address" in column:
                                email_loc3_index = (c)
                            if "Organization 1 - Name" in column and "Yomi" not in column or "Company" in column:
                                company_name_index = (c)
            #                    print(first_name_index, last_name_index, email_loc1_index, email_loc2_index, email_loc3_index, company_name_index)
                                for row in reader: 
                                    if firstline:
                                        firstline = False
                                        continue
                                    first_name   = row[first_name_index]
                                    last_name    = row[last_name_index]
                                    nick_name    = []
                                    email_addr   = []
                                    email_addr1  = row[email_loc1_index]
                                    email_addr2  = row[email_loc2_index]
                                    email_addr3  = row[email_loc3_index]
                                    company_name = row[company_name_index]                   
            #                        print(first_name, last_name, email_addr1, email_addr2, email_addr3, company_name)
                               
                                    if email_addr1:
                                        if email_addr2:
                                            email_addr = email_addr1.strip()
                                            if email_addr1:
                                                extract_names_func()
                                                nick_list.append(nick_name + "_1")
                                                print(nick_name + "_1", '\t', first_name, last_name, '\t', email_addr)
                                                print(nick_name + "_1", '\t', first_name, last_name, '\t', email_addr, file=alpine_out)
                                                print("alias", nick_name + "_1", first_name, last_name, "<" + email_addr + ">", file=mutt_out)
                                            try:
                                                email_addr = email_addr2.split(':::')[0].strip()
                                                if email_addr:
                                                    extract_names_func()
                                                    nick_list.append(nick_name + "_2")
                                                    print(nick_name + "_2", '\t', first_name, last_name, '\t', email_addr)
                                                    print(nick_name + "_2", '\t', first_name, last_name, '\t', email_addr, file=alpine_out)
                                                    print("alias", nick_name + "_2", first_name, last_name, "<" + email_addr + ">", file=mutt_out)
                                            except:
                                                pass
                                            try:
                                                email_addr = email_addr2.split(':::')[1].strip()
                                                if email_addr:
                                                    extract_names_func()
                                                    nick_list.append(nick_name + "_3")
                                                    print(nick_name + "_3", '\t', first_name, last_name, '\t', email_addr)
                                                    print(nick_name + "_3", '\t', first_name, last_name, '\t', email_addr, file=alpine_out)
                                                    print("alias", nick_name + "_3", first_name, last_name, "<" + email_addr + ">", file=mutt_out)
                                            except:
                                                pass
                                            try:
                                                email_addr = email_addr2.split(':::')[2].strip()
                                                if email_addr:
                                                    extract_names_func()
                                                    nick_list.append(nick_name + "_4")
                                                    print(nick_name + "_4", '\t', first_name, last_name, '\t', email_addr)
                                                    print(nick_name + "_4", '\t', first_name, last_name, '\t', email_addr, file=alpine_out)
                                                    print("alias", nick_name + "_4", first_name, last_name, "<" + email_addr + ">", file=mutt_out)
                                            except:
                                                pass
                                            try:
                                                email_addr = email_addr3.split(':::')[0].strip()
                                                if email_addr:
                                                    extract_names_func()
                                                    if (nick_name + "_2") not in nick_list:
                                                        print(nick_name + "_2", '\t', first_name, last_name, '\t', email_addr)
                                                        print(nick_name + "_2", '\t', first_name, last_name, '\t', email_addr, file=alpine_out)
                                                        print("alias", nick_name + "_2", first_name, last_name, "<" + email_addr + ">", file=mutt_out)
                                                    if (nick_name + "_2") in nick_list and (nick_name + "_3") not in nick_list:
                                                        print(nick_name + "_3", '\t', first_name, last_name, '\t', email_addr)
                                                        print(nick_name + "_3", '\t', first_name, last_name, '\t', email_addr, file=alpine_out)
                                                        print("alias", nick_name + "_3", first_name, last_name, "<" + email_addr + ">", file=mutt_out)
                                                    if (nick_name + "_3") in nick_list and (nick_name + "_4") not in nick_list:
                                                        print(nick_name + "_4", '\t', first_name, last_name, '\t', email_addr)
                                                        print(nick_name + "_4", '\t', first_name, last_name, '\t', email_addr, file=alpine_out)
                                                        print("alias", nick_name + "_4", first_name, last_name, "<" + email_addr + ">", file=mutt_out)
                                            except:
                                                pass
                                            try:
                                                email_addr = email_addr3.split(':::')[1].strip()
                                                if email_addr:
                                                    extract_names_func()
                                                    if (nick_name + "_3") not in nick_list:
                                                        print(nick_name + "_3", '\t', first_name, last_name, '\t', email_addr)
                                                        print(nick_name + "_3", '\t', first_name, last_name, '\t', email_addr, file=alpine_out)
                                                        print("alias", nick_name + "_3", first_name, last_name, "<" + email_addr + ">", file=mutt_out)
                                                    if (nick_name + "_3") in nick_list and (nick_name + "_4") not in nick_list:
                                                        print(nick_name + "_4", '\t', first_name, last_name, '\t', email_addr)
                                                        print(nick_name + "_4", '\t', first_name, last_name, '\t', email_addr, file=alpine_out)
                                                        print("alias", nick_name + "_4", first_name, last_name, "<" + email_addr + ">", file=mutt_out)
                                                    if (nick_name + "_4") in nick_list and (nick_name + "_5") not in nick_list:
                                                        print(nick_name + "_5", '\t', first_name, last_name, '\t', email_addr)
                                                        print(nick_name + "_5", '\t', first_name, last_name, '\t', email_addr, file=alpine_out)
                                                        print("alias", nick_name + "_5", first_name, last_name, "<" + email_addr + ">", file=mutt_out)
                                                    if (nick_name + "_5") in nick_list and (nick_name + "_6") not in nick_list:
                                                        print(nick_name + "_6", '\t', first_name, last_name, '\t', email_addr)
                                                        print(nick_name + "_6", '\t', first_name, last_name, '\t', email_addr, file=alpine_out)
                                                        print("alias", nick_name + "_6", first_name, last_name, "<" + email_addr + ">", file=mutt_out)
                                            except:
                                                pass
                                            try:
                                                email_addr = email_addr3.split(':::')[2].strip()
                                                if email_addr:
                                                    extract_names_func()
                                                    if (nick_name + "_4") not in nick_list:
                                                        print(nick_name + "_4", '\t', first_name, last_name, '\t', email_addr)
                                                        print(nick_name + "_4", '\t', first_name, last_name, '\t', email_addr, file=alpine_out)
                                                        print("alias", nick_name + "_4", first_name, last_name, "<" + email_addr + ">", file=mutt_out)
                                                    if (nick_name + "_4") in nick_list and (nick_name + "_5") not in nick_list:
                                                        print(nick_name + "_5", '\t', first_name, last_name, '\t', email_addr)
                                                        print(nick_name + "_5", '\t', first_name, last_name, '\t', email_addr, file=alpine_out)
                                                        print("alias", nick_name + "_5", first_name, last_name, "<" + email_addr + ">", file=mutt_out)
                                                    if (nick_name + "_5") in nick_list and (nick_name + "_6") not in nick_list:
                                                        print(nick_name + "_6", '\t', first_name, last_name, '\t', email_addr)
                                                        print(nick_name + "_6", '\t', first_name, last_name, '\t', email_addr, file=alpine_out)
                                                        print("alias", nick_name + "_6", first_name, last_name, "<" + email_addr + ">", file=mutt_out)
                                                    if (nick_name + "_6") in nick_list and (nick_name + "_7") not in nick_list:
                                                        print(nick_name + "_7", '\t', first_name, last_name, '\t', email_addr)
                                                        print(nick_name + "_7", '\t', first_name, last_name, '\t', email_addr, file=alpine_out)
                                                        print("alias", nick_name + "_7", first_name, last_name, "<" + email_addr + ">", file=mutt_out)
                                            except:
                                                pass
                                        else:
                                            email_addr = email_addr1
                                            extract_names_func()
                                            print(nick_name.ljust(25), (first_name + " " + last_name).ljust(30), email_addr)
                                            print(nick_name, '\t', first_name, last_name, '\t', email_addr, file=alpine_out)
                                            print("alias", nick_name, first_name, last_name, "<" + email_addr + ">", file=mutt_out)
            
            
            # Finally, put the new files in the user locations
            while mutt_or_alp:
                if mutt_or_alp == 'Q' or mutt_or_alp == 'q':
                    print("\nExiting...\n")
                    exit()
                elif mutt_or_alp == 'A' or mutt_or_alp == 'a':
                    shutil.copy2(alpine_temp, alpine_original)
                    print("\nAlpine contacts updated!\n")
                    user_nag_func()
                    mutt_or_alp = ''
                elif mutt_or_alp == 'M' or mutt_or_alp == 'm':
                    shutil.copy2(mutt_temp, mutt_original)
                    print("\nMutt contacts updated\n")
                    user_nag_func()
                    mutt_or_alp = ''
                elif mutt_or_alp == 'B' or mutt_or_alp == 'b':
                    shutil.copy2(alpine_temp, alpine_original)
                    shutil.copy2(mutt_temp, mutt_original)
                    print("\nAlpine and Mutt contacts updated!\n")
                    user_nag_func()
                    mutt_or_alp = ''
                else:
                    mutt_or_alp = input("\nImport to (A)lpine, (M)utt, (B)oth, or (Q)uit? ")
            break
        ## END SPRUCE CODE HERE
            
    if main_menu not in {"C", "c", "I", "i"}:
        print(main_menu + " is not an option ")
        time.sleep(1)
        continue
        #exit()
