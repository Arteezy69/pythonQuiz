import os
import datetime

basicSalary=float('50000')
supervisorySalary=float('30000')
ordinarySalary=float('20000')

hra=float('.15')
da=float('.10')
ea=float('.05')
ta=float('.12')
totalAllow=float('.42')
totalDeduct=float('.08')

ss=float('0.07')
levi=float('0.01')



while True:
    print("Name of Employee:")
    lastname = input("   Enter last name:")
    firstname = input("   Enter firstname:")
    middlename = input("   Enter middle name:")
    
    print ("    \nJob categories:")
    print("     [1] Managerial")
    print("     [2] Supervisory")
    print("     [3] Ordinary Personnel:\n")

    jobCategory = int(input("Enter Job Category:"))
    
    def computeAllowance(x,y):
        return x*y
        
    def computeDeductions(x,y):
        return x*y  
    
    def totalAllowance(x,y):
        return x*y
        
    def computeManagerialGross(x,y):
        return (basicSalary+(basicSalary*totalAllow))
        
    def computeManagerialNet(x,y):
        gross=(basicSalary+(basicSalary*totalAllow))
        return gross-(basicSalary*(totalDeduct))
    
    def computeSupervisoryGross(x,y):
        return (supervisorySalary+(supervisorySalary*totalAllow))
        
    def computeSupervisoryNet(x,y):
        gross=(supervisorySalary+(supervisorySalary*totalAllow))
        return gross-(supervisorySalary*(totalDeduct))
    
    def computeOrdinaryGross(x,y):
        return (ordinarySalary+(ordinarySalary*totalAllow))
        
    def computeOrdinaryNet(x,y):
        gross=(ordinarySalary+(ordinarySalary*totalAllow))
        return gross-(ordinarySalary*(totalDeduct))
    
    def notification():
        currentDate=datetime.datetime.now()
        date=currentDate.date()
        yr=date.strftime("%m/%Y")
        print("Notification Message:")
        print("This is your salary for the month/year:" ,yr )


    if(jobCategory==1):
        print("Name of Employee: "+firstname +" "+middlename +" "+lastname)
        print("Job Category: MANAGERIAL")
        print("Basic Salary:",int(basicSalary))
        print("\nAllowances:")
        print("   HRA:",computeAllowance(basicSalary,hra))
        print("   DA:",computeAllowance(basicSalary,da))
        print("   EA:",computeAllowance(basicSalary,ea))
        print("   TA:",computeAllowance(basicSalary,ta))
        print("   Total Allowance:",totalAllowance(basicSalary,totalAllow))
        
        print("\nDeductions:")
        print("   SS:",computeDeductions(basicSalary,ss))
        print("   LEVI:",computeDeductions(basicSalary,levi))
        print("   \nTotal Deductions",basicSalary*(ss+levi))
        
        print("\nGross Salary:",computeManagerialGross(basicSalary,totalAllow))
        print("Net Salary:",computeManagerialNet(basicSalary,totalDeduct))
        notification()
        while True:
            tryagain=input("Do you want to try again? [y/n]:")
            if tryagain=="y":
                os.system('cls')
                break;
            elif tryagain=="n":
                exit();
            else: 
                print("Invalid")
            
    

    
    
    if(jobCategory==2):
        print("Name of Employee: "+firstname +" "+middlename +" "+lastname)
        print("Job Category: SUPERVISORY")
        print("Basic Salary:",int(supervisorySalary))
        print("\nAllowances:")
        print("   HRA:",computeAllowance(supervisorySalary,hra))
        print("   DA:",computeAllowance(supervisorySalary,da))
        print("   EA:",computeAllowance(supervisorySalary,ea))
        print("   TA:",computeAllowance(supervisorySalary,ta))
        print("   Total Allowance:",totalAllowance(supervisorySalary,totalAllow))
        
        print("\nDeductions:")
        print("   SS:",computeDeductions(supervisorySalary,ss))
        print("   LEVI:",computeDeductions(supervisorySalary,levi))
        print("   Total Deductions",supervisorySalary*(ss+levi))
        
        print("\nGross Salary:",computeSupervisoryGross(supervisorySalary,totalAllow))
        print("Net Salary:",computeSupervisoryNet(supervisorySalary,totalDeduct))
        print("\nNotification Message:")
        print("This is your salary for the month/year:5/2022")
        while True:
            tryagain=input("Do you want to try again? [y/n]:")
            if tryagain=="y":
                os.system('cls')
                break
            elif tryagain=="n":
                exit()
            else: print("Invalid")
           
    
    
    
    if(jobCategory==3):
        print("Name of Employee: "+firstname +" "+middlename +" "+lastname)
        print("Job Category: ORDINARY")
        print("Basic Salary:",int(ordinarySalary))
        print("\nAllowances:")
        print("   HRA:",computeAllowance(ordinarySalary,hra))
        print("   DA:",computeAllowance(ordinarySalary,da))
        print("   EA:",computeAllowance(ordinarySalary,ea))
        print("   TA:",computeAllowance(ordinarySalary,ta))
        print("   Total Allowance:",totalAllowance(ordinarySalary,totalAllow))
        
        print("\nDeductions:")
        print("   SS:",computeDeductions(ordinarySalary,ss))
        print("   LEVI:",computeDeductions(ordinarySalary,levi))
        print("   Total Deductions",ordinarySalary*(ss+levi))
        
        print("\nGross Salary:",computeOrdinaryGross(ordinarySalary,totalAllow))
        print("Net Salary:",computeOrdinaryNet(ordinarySalary,totalDeduct))
        
        
        print("\nNotification Message:")
        print("This is your salary for the month/year:5/2022")
        
        while True:
            tryagain=input("Do you want to try again? [y/n]:")
            if tryagain=="y":
                os.system('cls')
                break
            elif tryagain=="n":
                exit()
            else: 
                print("Invalid")
                
    
   
        