# Mess Feedback System

def add_feedback():
    f = open("feedback.txt", "a")
    ans = 'y'
    while ans == 'y' or ans == 'Y':
        reg = input("Enter registration number: ")
        name = input("Enter student name: ")
        mess = input("Enter mess name: ")
        
        print("1. Breakfast")
        print("2. Lunch")
        print("3. High Tea")
        print("4. Dinner")
        meal_choice = int(input("Enter meal choice (1 to 4): "))
        
        if meal_choice == 1:
            meal = "Breakfast"
        elif meal_choice == 2:
            meal = "Lunch"
        elif meal_choice == 3:
            meal = "High Tea"
        elif meal_choice == 4:
            meal = "Dinner"
        else:
            meal = "Unknown"
            
        rate = int(input("Enter rating (1 to 5): "))
        while rate < 1 or rate > 5:
            print("Rating should be between 1 and 5")
            rate = int(input("Enter rating (1 to 5): "))
            
        comm = input("Enter comment: ")

        
        f.write(reg + "," + name + "," + mess + "," + meal + "," + str(rate) + "," + comm + "\n")
        print("Feedback added successfully!")
        
        ans = input("Want to add more? (y/n): ")
    f.close()


def display_feedback():
    try:
        f = open("feedback.txt", "r")
        line = f.readline()
        if line == "":
            print("No feedback found!")
        else:
            print("\n--- ALL FEEDBACK RECORDS ---")
            while line != "":
                rec = line.strip().split(",")
                print("Reg No  :", rec[0])
                print("Name    :", rec[1])
                print("Mess    :", rec[2])
                print("Meal    :", rec[3])
                print("Rating  :", rec[4])
                print("Comment :", rec[5])
                print("-" * 25)
                line = f.readline()
        f.close()
    except:
        print("No feedback found!")


def search_feedback():
    try:
        f = open("feedback.txt", "r")
        reg = input("Enter registration number to search: ")
        found = 0
        line = f.readline()
        while line != "":
            rec = line.strip().split(",")
            if rec[0] == reg:
                print("\n--- Feedback Found ---")
                print("Reg No  :", rec[0])
                print("Name    :", rec[1])
                print("Mess    :", rec[2])
                print("Meal    :", rec[3])
                print("Rating  :", rec[4])
                print("Comment :", rec[5])
                found = 1
            line = f.readline()
        f.close()
        if found == 0:
            print("No feedback found for this registration number.")
    except:
        print("No feedback found!")


def mess_avg():
    try:
        f = open("feedback.txt", "r")
        m_name = input("Enter mess name: ")
        total = 0
        count = 0
        line = f.readline()
        while line != "":
            rec = line.strip().split(",")
            if rec[2].lower() == m_name.lower():
                total = total + int(rec[4])
                count = count + 1
            line = f.readline()
        f.close()
        
        if count == 0:
            print("No feedback found for this mess.")
        else:
            avg = total / count
            print("Total Feedbacks:", count)
            print("Average Rating of", m_name, "is", round(avg, 2))
            if avg >= 4:
                print("Mess is very good!")
            elif avg >= 3:
                print("Mess is average.")
            else:
                print("Mess needs improvement.")
    except:
        print("No feedback found!")


def meal_avg():
    try:
        f = open("feedback.txt", "r")
        meal_name = input("Enter meal name (Breakfast/Lunch/High Tea/Dinner): ")
        total = 0
        count = 0
        line = f.readline()
        while line != "":
            rec = line.strip().split(",")
            if rec[3].lower() == meal_name.lower():
                total = total + int(rec[4])
                count = count + 1
            line = f.readline()
        f.close()
        
        if count == 0:
            print("No feedback found for this meal.")
        else:
            avg = total / count
            print("Average rating for", meal_name, "is", round(avg, 2))
    except:
        print("No feedback found!")


def delete_feedback():
    try:
        f = open("feedback.txt", "r")
        reg = input("Enter registration number to delete: ")
        lines = f.readlines()
        f.close()
        
        found = 0
        f = open("feedback.txt", "w")
        for line in lines:
            rec = line.strip().split(",")
            if rec[0] == reg:
                found = 1
            else:
                f.write(line)
        f.close()
        
        if found == 1:
            print("Feedback deleted successfully!")
        else:
            print("Registration number not found.")
    except:
        print("No feedback found!")


while True:
    print("\n==============================")
    print("    MESS FEEDBACK SYSTEM      ")
    print("==============================")
    print("1. Add Feedback")
    print("2. Display All Feedback")
    print("3. Search Feedback")
    print("4. Average Rating of a Mess")
    print("5. Average Rating of a Meal")
    print("6. Delete Feedback")
    print("7. Exit")
    
    ch = int(input("Enter your choice (1-7): "))
    
    if ch == 1:
        add_feedback()
    elif ch == 2:
        display_feedback()
    elif ch == 3:
        search_feedback()
    elif ch == 4:
        mess_avg()
    elif ch == 5:
        meal_avg()
    elif ch == 6:
        delete_feedback()
    elif ch == 7:
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 7.")
