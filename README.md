## Spruce is a simple utility for Alpine Email.

Spruce will:

* present two options on launch:
  1. (C)HOOSE an email account to open (any number of email accounts can easily be selected)
  2. (I)MPORT contacts from Google Contacts or Outlook csv file
* automatically launch Alpine with password file support (e.g. --with-password)

CONTENTS:
[Changelog](#changelog)

[Dependencies](#dependencies)

[Running adm](#running)

[Notes](#notes)

## Changelog:
0.6.5 -- bug fixes


<br><br>
## Dependencies:

Python 3.6 or newer


<br><br>
## Running:

1. Download spruce.py, make it executable, and place it with user-executable files (e.g., /usr/local/bin/).

2. Run it from any terminal

<br><br>
## Notes:
I love Alpine Email, and it has several advantages over Mutt, including that it adapts to small windows better (great for using in a window manager) and it has a very effective interface. It also has good password storage support with SSH, and a slew of customizations far too many to discuss here. If you use it, you already know.

However, Alpine lacks support for multiple accounts, and is often compiled in distros without password-saving functioniality. It also has a specific layout for text-based contacts storage and no ability to import contacts from a csv.

Spruce is an effort to work around these three limitations:

1. Using Alpine's ability to supercede its default pinerc config file using a pinercex file, Spruce allows the user to select from any number of pinercex files on launch, resulting a simple way to choose from a list of email accounts quickly. Allpine must still be restarted to change accounts, but it's faster than hand-copying files in the terminal.

2. Spruce contains the code from my contact import utility Goose, which allows contacts to be imported into an Alpine (or Mutt) formatted file from a Google Contacts or Outlook csv file, and used immediately. There is no two-way sync at this time. Mutt and Alpine only store names and emails anyway, so keeping a master contact file elsewhere is necessary in any event.

3. Among the distros that have Alpine in their repos (hats off to those that do), they seem to compile it without "passfile" support. Of course, Alpine can be launched with -password to rectify this, and Spruce includes this flag by default, saving typing or the use of an alias.

I would suggest inspecting the code in the script before running it. It's pretty clear where it expects files to be located.

