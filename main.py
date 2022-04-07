from dbhelper import DBHelper

def main():
    db=DBHelper()
    while True:
        print("******WELCOME*******")
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display all users")
        print("PRESS 3 to delete user")
        print("PRESS 4 to exit program")
        print()
        try:
            choice=int(input())
            if (choice==1):
                userid=int(input('Enter userID\t'))
                username=input('Enter username\t')
                phone = int(input('Enter phone number\t'))
                db.insertdb(userid,username,phone)
            elif (choice==2):
                db.fetchall()
            elif(choice==3):
                userid=int(input('Enter the userID to delete entry from database\t'))
                db.deleteuser(userid)
            elif(choice==4):
                break
            else:
                print("invalid input! try again")
        except Exception as e:
            print(e)
            print("Invalid details, try again")

if __name__=="__main__":
    main()
