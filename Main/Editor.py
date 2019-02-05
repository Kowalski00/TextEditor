'''
Created on 19 de mai de 2018

@author: Ramon
'''
import sys
#import pyglet
import os
#import glob
#import keyboard

def lista_dir(directory):
    local = os.path.dirname(directory)
    # abspath returns an absolute version of the pathname |-> used to be inside .dirname() but only returned the same as using directory
    #
    # directory is the full path of the program, for example: 'E:\Library\Documents\Liclipse Workspace\TextEditor\Main\Editor.py'
    # dirname returns the directory name of the directory for example : 'E:\Library\Documents\Liclipse Workspace\TextEditor\Main'
    # 
    lista = os.listdir(local)
    # returns a list containing the names of the files  in local
    lista_final = filter(lambda x: ".txt" in x, lista)
    # filter every file that's not a .txt in lista
    return lista_final

def quit_function():
    print '[*] You are leaving the editor'
    sys.exit()

def open_archive():
    print '\n'
    lista = lista_dir(__file__)
    print lista
    try:
        filename = raw_input('[*] Specify you file including the extension, please: ')
        x = open(filename, "r")
        read_file = x.read()
        print '[*]|-------------------------------------------| \n'
        print read_file
    except Exception as e:
        print("Problem: %s" % (e))
    print '\n'
        
def write_function():
    i=0   # i is a counter for the lines and to make the editor jump one line at the beginning
    lista = lista_dir(__file__) # gets a list with the files in directory to check 
    filename = raw_input('[*] Name your file(include extension): ')
    for n in lista:
        if filename == n:
            print '\n'
            ow = raw_input("[*] There is already a file with that name, do you wish to overwrite it?('yes' or 'no') ")
            if ow == 'yes':
                x = open(filename, "w")
                print "[*] To finish a line, press: ENTER"
                print "[*] To exit simply write: '[menu]' \n"
                while True:
                    if i==0:
                        print '\n'
                        i+=1
                    else:
                        line = raw_input("%3i  " % i)
                        if line.lower() == "[menu]":
                            return
                        x.write(line)
                        x.write("\n")
                        i+=1
            elif ow == 'no':
                return
            else:
                print '\n'
                print "Pick 'yes' or 'no'"
               
        else:
            x = open(filename, "w")
            print "[*] To finish a line, press: ENTER"
            print "[*] To exit simply write: '[menu]' \n"
            while True:
                if i==0:
                    print '\n'
                    i+=1
                line = raw_input("%3i  " % i)
                if line.lower() == "[menu]":
                    return
                x.write(line)
                x.write("\n")
                i+=1
    if lista == []:
        x = open(filename, "w")
        print "[*] To finish a line, press: ENTER"
        print "[*] To exit simply write: '[menu]' \n"
        while True:
            if i==0:
                print '\n'
                i+=1
            line = raw_input("%3i  " % i)
            if line.lower() == "[menu]":
                return
            x.write(line)
            x.write("\n")
            i+=1
    print '\n'

def about_function():
    print '[*] This is a Text Editor made by Kowalski, R. on Python  2.7'
    print "[*] Try to use mostly .txt files as the tests were done in this extension  \n"
    
def delete_function():
    lista = lista_dir(__file__)
    print lista, '\n'
    del_file = raw_input('[*] Which file do you want to delete? ')
    os.remove(del_file)
    print '\n'

def rename_function():
    lista = lista_dir(__file__)
    print lista, '\n'
    f_oldName = raw_input('[*] Write the name of the file to be renamed(include extension): ')
    f_newName = raw_input('[*] Write the new name for the file: ')
    if f_newName == f_oldName:
        print '[*] Warning: This is the same name as before, the operation will continue.'
    os.rename(f_oldName, f_newName)
    print '\n'

# Using a dictionary is better than putting a bunch of "elif's", uses fewer lines too      
FunctionsDict = {
    'quit':quit_function,
    'open':open_archive,
    'write':write_function,
    'rename':rename_function,
    'about':about_function,
    'delete':delete_function
    }      
       
while True:
    print '[*]|-------------------------------------------|'
    print '[*] Menu: quit, open, write, delete, rename, about \n'
    cmd = str(raw_input("[*] What do you wish for? "))
    #FunctionsDict.get(cmd, lambda: '[*] There is no such command as that \n')() # Doesn't return the line when the user types an unknown command
    FunctionsDict.get(cmd)() # 'FunctionsDict[cmd]()' works too
