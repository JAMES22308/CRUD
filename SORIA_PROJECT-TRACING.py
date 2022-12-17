#Author: Michael James Soria
import json
import pyttsx3

rate = -5000
jarvis = pyttsx3.init()
jarvis.setProperty('rate', rate)


def Add_Entry():
    name = input("Enter Name: ")
    contact = input("Enter contact no.: ")
    address = input("Enter address: ")
    date = input("Enter date: ")
   

    dictionary = {
        "name: " : name,
        "contact: " : contact,
        "address: " : address,
        "date: " : date
    }

    with open("visitor.json", "r") as getdata:
        data = json.load(getdata)  #convert json to python        
        data[name] = dictionary 
                
        with open("visitor.json", "w") as save:
            json.dump(data, save) #convert python to json
            jarvis.say("Data Successfully Added")
            print("Data Successfully Added 😊")
            jarvis.runAndWait()



def Show_Entry():
    with open ("visitor.json", "r") as view:
        data = json.load(view)

        if(len(data) <= 0):
            jarvis.say("no existing data")
            print("No data")
            jarvis.runAndWait()  
        else:
            for i, m in data.items():   #used to return the list with all dictionary keys with values.
                for x, n in m.items():
                    print(x, n)
            print("Data showed 😊\n") 
            jarvis.say("Data showed")
            jarvis.runAndWait()        



def Delete_Entry():
    Show_Entry()
    name = input("Enter Name : ")
    with open("visitor.json", "r") as getdata:
        data = json.load(getdata)
        
        if name in data:
            data.pop(name)   #removes the specified item from the dictionary
            

            with open ("visitor.json", "w") as delete:
                data1 = json.dump(data, delete)
                jarvis.say("Data Successfully Deleted ")
                print("Data Successfully Deleted 👍")
                jarvis.runAndWait()    




def delete_Entry_by_date():

    Show_Entry()    
    date = input("Enter Date :")  

    with open("visitor.json", "r") as getdata:
        data = json.load(getdata)

        mainKey = ""

        for key, value in data.items():
           for i,x  in value.items():
               if(date == x):
                    mainKey = key
        
        if(mainKey == ""):
            jarvis.say("Invalid input, no data deleted")
            print("Invalid input, no data deleted 😔\n")
        else:
            data.pop(mainKey)
            jarvis.say("Data Successfully Deleted")
            print("Data Successfully Deleted 👍")
       
        with open ("visitor.json", "w") as delete:
            data2 = json.dump(data, delete)           
            jarvis.runAndWait() 




def Find_entry():
   
    name = input("Enter Name :")  

    with open("visitor.json", "r") as getdata:
        data = json.load(getdata)

        mainKey = ""

        for key, value in data.items():
           for i,x  in value.items():
               if(name == x):
                    mainKey = key
        
        if(mainKey == ""):
            jarvis.say("Invalid input, no data found")
            print("Invalid input, no data found 😔\n")
        else:
            for i, x in data[mainKey].items():
                print(i, x)   
            jarvis.say("Data Successfully Found")
            print("Data Successfully Found 😊👍 ")       
       
        with open ("visitor.json", "w") as find:
            data3 = json.dump(data, find)
            jarvis.runAndWait() 




def Find_entry_by_date():
   
    date = input("Enter Date :")  

    with open("visitor.json", "r") as getdata:
        data = json.load(getdata)

        mainKey = ""

        for key, value in data.items():
           for i,x  in value.items():
               if(date == x):
                    mainKey = key
        
        if(mainKey == ""):
            jarvis.say("Invalid input, no data found")
            print("Invalid input, no data found  😔\n")
        else:
            for i, x in data[mainKey].items():
                print(i, x)
            jarvis.say("Data Successfully Found")
            print("Data Successfully Found 😊👍 ")
      
        with open ("visitor.json", "w") as find:
            data3 = json.dump(data, find)
            
            jarvis.runAndWait() 




def main():
    print("[1] Add Entry")
    print("[2] Delete Entry")
    print("[3] Delete Entry by Date")
    print("[4] Find Entry")
    print("[5] Find Entry by Date")
    print("[6] Show Entries")
    print("[0] Exit")
    print(" ")
    enter = int(input("choose: "))
    print(" ")
   
    if enter == 1:
        Add_Entry()
        print(" ")
        main()

    elif enter == 2:
        Delete_Entry()
        print(" ")
        main()

    elif enter==3:
        delete_Entry_by_date()
        print(" ")
        main()

    elif enter == 4:
        Find_entry()
        print(" ")
        main()

    elif enter == 5:
        Find_entry_by_date()
        print(" ")
        main()

    elif enter == 6:
        Show_Entry()
        print(" ")
        main()

    elif enter == 0:
        jarvis.say("Thankyou for trusting me")
        print("exit.")
        jarvis.runAndWait()

    else:
        jarvis.say("Try again with a specific number")
        print("Try again with a specific number \n")
        jarvis.runAndWait()
        main()
        print("\n")
        
  
main()



    
    
    

