## Spruce is a simple utility for Alpine Email.

Spruce will present two options on launch: 
  1. (C)HOOSE an email account to open (any number of email accounts can easily be selected)
  2. (I)MPORT contacts from Google Contacts or Outlook csv file

CONTENTS:
[Changelog](#changelog)

[Dependencies](#dependencies)

[Running spruce](#running)

[Notes](#notes)

<br><br>
## Changelog: 
0.6.6 -- remove broken password file argument  
0.6.5 -- bug fixes

<br><br>
## Dependencies: 
Python 3.6 or newer

<br><br>
## Running:

1. Download spruce.py, make it executable, and place it with your user-executable scripts (e.g., /usr/local/bin/)

2. Run it from your favorite terminal

<br><br>
# Notes:
Alpine Email is great. The spruce.py script is an effort to smooth out two limitations: (1) lack of support for multiple accounts, and (2) no ability to import contacts from Gxxgle/Micrxsxft.

1. Using Alpine's ability to supercede its default pinerc config file using a pinercex file, Spruce allows the user to select from any number of pinercex files on launch, resulting a simple way to choose from a list of email accounts quickly. Alpine must still be restarted to change accounts, but it's faster than hand-copying files in the terminal.

2. Spruce contains the code from my contact import utility goose.py, which allows contacts to be imported into an Alpine formatted file from a Google Contacts or Outlook csv file, and used immediately. There is no two-way sync at this time. Alpine only stores names and emails anyway, so keeping a master contact file elsewhere is necessary in any event.

I would suggest inspecting the code in the script before running it. It's pretty clear where it expects files to be located.

