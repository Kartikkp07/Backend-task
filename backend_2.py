###########################################################################################################################################################################################
#importing libraries
import csv
from passlib.hash import sha256_crypt #for hashing passwords
import getpass
#pip install pillow to access PIL
from PIL import Image
import os


###########################################################################################################################################################################################
#storing pre registered names,emails and passwords
names=[]
ph_nos=[]
list_of_sex=[]
list_of_address=[]
passwords=[]
prereg_emails=[]
try:

    with open("User_details.csv", 'r') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=",")
        header=next(csv_reader)
    
        for line in csv_reader:
            prereg_emails=prereg_emails+[line[3]]
            names=names+[line[0]]
            list_of_address=list_of_address+[line[4]]
            list_of_sex=list_of_sex+[line[2]]
            ph_nos=ph_nos+[line[1]]
            passwords=passwords+[line[5]]
except:
    with open("User_details.csv", 'w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=",")
        csv_writer.writerow(["Name","Phone Number","Sex","Email ID","Address","Passwords"])
    with open("User_details.csv", 'r') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=",")
        header=next(csv_reader)
    
        for line in csv_reader:
            prereg_emails=prereg_emails+[line[3]]
            names=names+[line[0]]
            list_of_address=list_of_address+[line[4]]
            list_of_sex=list_of_sex+[line[2]]
            ph_nos=ph_nos+[line[1]]
            passwords=passwords+[line[5]]


###########################################################################################################################################################################################
def login(email,password):
    if (len(prereg_emails)==0):
        print("\n\n\033[1mNo accounts registered yet,please register first\033[0m\n\n")
        access("reg")
    elif (len(prereg_emails)!=0):
    
        if (email in prereg_emails) and (sha256_crypt.verify(password,passwords[prereg_emails.index(email)])):
            print("\n------------YOUR DETAILS ARE AS FOLLOWS-------------\n")
            print("\n\033[1mName:\033[0m\t",names[prereg_emails.index(email)])
            print("\n\033[1mPhone Number:\033[0m\t",ph_nos[prereg_emails.index(email)])
            print("\n\033[1mSex:\033[0m\t",list_of_sex[prereg_emails.index(email)])
            print("\n\033[1mAddress:\033[0m\t",list_of_address[prereg_emails.index(email)])
            print("\n\033[1mEmail id:\033[0m\t",email)
            
            while True:
                srch=input("\nwould you like to search for users(y/n)\n")
                if srch=="y":
                    srch_user()
                elif srch=="n":
                    break
                else:
                    print("\nplease enter 'y' or 'n' only\n")
                
        else:
            print("\n----Invalid login credentials ,please try again----\n")
            access(option)
    
###########################################################################################################################################################################################
def register(name,password,ph_no,email,sex,address):
    with open("User_details.csv", 'a') as csv_file:
        csvWriter = csv.writer(csv_file, delimiter = ',')
        csvWriter.writerow([name,ph_no,sex,email,address,sha256_crypt.hash(password)])
    print("\n\n\nregistered\n\n\n")

###########################################################################################################################################################################################
def store_dp(username):
    os.chdir("/Users/kkp/Desktop/profile_pictures")
    dp_choice=int(input("Choose from the following options(1/2) to set your profile picture:\n\t1.Use default image\n\t2.Enter path of image to be used\n\t"))
    if (dp_choice==1):
        img_name=username+".jpg"
        f=open("/Users/kkp/Desktop/profile_pictures/default_dp.jpg","rb")
        user_img=open(img_name,"wb")
        for line in f:
            user_img.write(line)
        
    
    elif (dp_choice==2):
        try:
            img_path=input("\nEnter path of image you want to set as profile picture\n")
            img_name=username+".jpg"
            f=open(img_path,"rb")
            user_img=open(img_name,"wb")
            for line in f:
                user_img.write(line)
        
            
        except:
            print("\n----------There exists no image for given path ,please try again----------\n")
            store_dp(username)
    else:
        print("\nEnter a valid choice\n")
        store_dp(username)
        
        
###########################################################################################################################################################################################
def srch_user():
    n=input("\n  Enter name of user whos details you want to search:  \n")
    print("\t------------------------------------------------------\t")
    if n not in names:
        print("\n User entered doesn't exist\n")
    else:
    
        for j in range(len(names)):
            if names[j]==n:
                print("\n\033[1mName:\033[0m\t",names[j])
                print("\n\033[1mPhone Number:\033[0m\t",ph_nos[j])
                print("\n\033[1mAddress:\033[0m\t",list_of_address[j])
                print("\t------------------------------------------------------\t")
                    
###########################################################################################################################################################################################
def access(option):
    if (option=="login"):
        email=input("\nEnter email \n")
        password=getpass.getpass(prompt="enter password")
        login(email,password)
    else:
        print("\nEnter required details to register\n")
        name=input("\nEnter name \n")
        ph_no=int(input("enter 10 digit phone number"))
        while True:
        
            email=input("\nEnter email id \n")
            #checking if email already exists
            if email in prereg_emails:
                print("\n------------This email has already been registered, please use a different email id ------------------\n")
            else:
                break
            
        sex=input("\nEnter sex (Male/Female/Others)\n")
        address=input("\nEnter address \n")
        password=getpass.getpass(prompt="please enter password")
        confirm_pass=getpass.getpass(prompt="confirm password")
        if confirm_pass==password:
            store_dp(name)
            os.chdir("/Users/kkp/Desktop")
            register(name,password,ph_no,email,sex,address)
        else:
            print("\n--------Passwords didn't match,try again------\n")
            access(option)
    
###########################################################################################################################################################################################
def begin():
    global option
    print("welcome to backend task 2")
    option=input("Login or Register by creating a new account(login,reg):\n")
    if (option!="login" and option!="reg"):
        print("\n\nPlease enter a valid option")
        begin()
        
begin()
access(option)
