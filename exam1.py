employees = ""
Add_new_employee = 1
print_all_employees = 2
Delete_by_age_range = 31
update_salary_by_name = 4
End_the_program = 5

choice=int(input("enter your choice from(1 to 5):"))
if 1 < choice > 5:
        print ("invalid range.try again")
elif choice== Add_new_employee:
        print("enter employee data:")  
        print(input("enter the name:"),"has age",input("enter the age:"),"and salary is",int(input("enter the salary:"))) 
        employees.append(Add_new_employee)

elif choice== print_all_employees:
        print(employees)
elif choice==Delete_by_age_range:
        print(int(input("enter age range").startwith[::].remove()))    
elif choice==update_salary_by_name:
            print(int(input("enter salary updated").insert()))  

while choice==5:
        break           


    


