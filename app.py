# Importing Libraries
from prettytable import PrettyTable
pt = PrettyTable()
import json

# Initialising Variables
name_list = []
num_list = []
email_list = []
m = 0

# Header Function
def cringe():
    print()
    print("-----------------------------------------")
    print()
    print("B.Tech - Comp Sci (Hons) Python Project")
    print("Name: Asmit Singh")
    print("Section: K22FG")
    print("Roll No: 62")
    print("Reg. No: 12200276")
    print("-----------------------------------------")
    print()
    print("Database Application in Python")
    main()

# Function to Add Data
def add_data():
    print()
    noe = int(input("Enter the number of entries to be inserted: "))
    for i in range(noe):    
        def name_input():
            inp1 = str(input("Enter the name of the student: "))
            if len(inp1)==0:
                print("Enter a valid name--->")
                print()
                name_input()
            else:
                name_list.append(inp1)
        name_input()
        
        def num_input():
            inp2 = str(input("Enter the mobile number of the student: "))
            if len(inp2)<10:
                print("Enter a valid number--->")
                print()
                num_input()
            else:
                num_list.append(inp2)
        num_input()
        
        def email_input():
            inp3 = str(input("Enter the email address of the student: "))
            veri = inp3.find("@")
            if veri==-1:
                print("Enter a valid email address---> ")
                print()
                email_input()
            else:
                email_list.append(inp3)
        email_input()
    json_save()
    main()

# Function to Display Data

def disp_data():
    print()
    print("Displaying all entries in the repository: ")
    pt = PrettyTable(["Name", "Phone Number", "E-mail Address"])
    for i in range(len(name_list)):
        pt.add_row([name_list[i],num_list[i],email_list[i]])
    print(pt)
    main()

# Function to Search Entries

def look_data():
    print()
    print("Search Using: ")
    print("1. Name ")
    print("2. Phone Number ")
    print("3. Email Address ")

    def search_by_name():
        print()
        name = str(input("Enter the name of the student ---> "))
        f_name = name_list.index(name)
        print("The linked phone number is: ", num_list[f_name])
        print("The linked email address is: ", email_list[f_name])
    
    def search_by_number():
        print()
        num = str(input("Enter the phone number of the student ---> "))
        f_num = num_list.index(num)
        print("The linked name is: ", name_list[f_num])
        print("The linked email address is: ", email_list[f_num])

    def search_by_email():
        print()
        email = str(input("Enter the email address of the student ---> "))
        f_email = email_list.index(email)
        print("The linked name is: ", name_list[f_email])
        print("The linked phone number is: ", num_list[f_email])
    
    def find_choice():
        print()
        fi = int(input("Enter your choice: "))
        if fi==1:
            search_by_name()
        elif fi==2:
            search_by_number()
        elif fi==3:
            search_by_email()
        else:
            print("Enter a valid number as choice: ")
            find_choice()
    find_choice()
    main()

# Function to Export Data as Dictionary in a JSON File

def json_save():
    dic = dict(zip(name_list,num_list))
    json_object = json.dumps(dic)
    with open("savefile.json","a") as outfile:
        outfile.write(json_object)
    
    dic2 = dict(zip(name_list,email_list))
    json_object2 = json.dumps(dic2)
    with open("savefile.json","a") as outfile:
        outfile.write(json_object2)

# Main Function
def main():
    print()
    print("What do you want to do:")
    print("1. Add")
    print("2. Display")
    print("3. Search")
    print("4. Exit")
    def m_inp():
        m = int(input("Enter your choice: "))
        if m==1:
            add_data()
        elif m==2:
            disp_data()
        elif m ==3:
            look_data()
        elif m==4:
            exit()
        else:
            print("Enter a valid number as choice:")
            m_inp()
    m_inp()
cringe()
