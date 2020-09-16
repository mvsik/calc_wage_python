# -*- coding: utf-8 -*-

"""
Takes User Input In Form:
    Hourly Wage
    Daily Wage
    Weekly Wage
    Monthly Wage
    Yearly Wage
    
Prints All Other Forms of Wage

"""

#import string


exitIfFalse = 1;

hourSet = frozenset(["hourly", "h", "hour"])
daySet = frozenset(["daily", "d", "day"])
weekSet = frozenset(["weekly", "w", "week"])
monthSet = frozenset(["monthly", "m", "month"])
yearSet = frozenset(["yearly", "y", "year"])
exitSet = frozenset(["close","exit","stop","quit","end", "q"])
editSet = frozenset(["edit", "change", "qualities", "assumptions"])
helpSet = frozenset(["help","commands",""])


def printHelp():
    print("~~~~~~~ COMMAND LIST ~~~~~~~")
    print("Commands are not case sensitive!", '\n')
    
    print("To exit program at any time:")
    print("Enter close, exit, stop, end, quit, or q","\n")
    
    print("For Type of Wage:")
    print("year,y,yearly for yearly wage")
    print("month,m,monthly for monthly wage")
    print("week,w,weekly for weekly wage")
    print("day,d,daily for daily wage", '\n')
    
    print("For Wage Ammount:")
    print("Include only one ammount in USD", '\n')
    
    print("To edit conversion assumptions:")
    print("Enter edit, change, qualities, or assumptions")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", "\n")
    
    
    

class Assumptions:
    """
    Assumptions Class
    
    Contains conversion parameters used in this program
    
    """
    
    def __init__(self):
        self.resetAssumptions()
        
    def resetAssumptions(self):
        self.daysPerWeek = 5.0
        self.daysPerMonth = 30.3275
        self.hoursPerDay = 8.0
        self.weeksPerYear = 52.0
        self.hoursPerWeek = self.hoursPerDay * self.daysPerWeek
        self.weeksPerMonth = self.daysPerMonth / 7
        self.daysPerYear = self.weeksPerYear * self.daysPerWeek
        self.monthsPerYear = self.weeksPerYear / self.weeksPerMonth
    
        
    def setAssumptions(self,first,second):
        first = int(first)
        second = int(second)
    
    
    def printAssumptions (self):
        print ("Assuming: \n", f'{self.hoursPerDay} hours per day')
        print(f'{self.hoursPerWeek:.2f} hours per week')
        print(f'{self.daysPerWeek:.2f} days per week')
        print(f'{self.daysPerMonth:.2f} days per month')
        print(f'{self.weeksPerMonth:.2f} weeks per month')
        print(f'{self.weeksPerYear:.2f} weeks per year')
        print(f'{self.monthsPerYear:.2f} months per year')

        
        
    def assignNumber (self,inputText):
        """
        Returns corresponding value for given input text
        
        See description of editAssumptions method
        
        """
        if(inputText in hourSet):
            return 0
        if(inputText in daySet):
            return 1
        if(inputText in weekSet):
            return 2
        if(inputText in monthSet):
            return 3
        if(inputText in yearSet):
            return 4
        else:
            return None
    
        
    
    def printEditHelp(self):
        print("This tool allows you to edit the conversion ratios")
        print("Enter first unit, the second unit, then the new value to change that ratio.")
        print("e.g. \n _day_ \n _month_ \n _30_ \n would edit daysPerMonth to be 30",'\n')    
        
        print("Only some ratios are supported. They are:",'\n')
        print("daysPerWeek","daysPerMonth","hoursPerDay","weeksPerYear", sep = '\n')
        
        
    def editAssumptions(self):
        """ 

        Hour : 0
        Day : 1
        Week : 2
        Month : 3
        Year : 4
    
        e.g. 0 per 2 would be hours per week
    
        """
        while (1):
            self.printEditHelp()
        
            firstInput = input("Enter first unit: ")
            firstInput = firstInput.lower().strip()
            if(firstInput in exitSet):
                return
            if(firstInput in helpSet):
                printHelp()
                continue
            
            secondInput = input("Enter second unit: ")
            secondInput = secondInput.lower().strip()
            if(secondInput in exitSet):
                return
            if(secondInput in helpSet):
                printHelp()
                continue
                
            value = input("Enter value: ")
            print('\n')
            if(value.lower().strip() in exitSet):
                return
            if(value.lower().strip() in helpSet):
                printHelp()
            try:
                value = float(value)
            except:
                print("Value was not recognized as a number, please try again",'\n')
                continue
            
            firstNumber = self.assignNumber(firstInput)
            secondNumber = self.assignNumber(secondInput)
            if(firstNumber == None or secondNumber == None):
                print("Unit name could not be recognized. You can type help to show commands.",'\n')
                continue
            
            if(firstNumber < secondNumber):
                if(firstNumber == 0):
                    if(secondNumber == 1):
                        self.hoursPerDay = value
                        print(f'Hours per Day is now {value}','\n')
                    if(secondNumber == 2):
                        self.hoursPerWeek = value
                        print(f'Hours per Week is now {value}','\n')
                        
                if(firstNumber == 1):
                    if(secondNumber == 2):
                        self.daysPerWeek = value
                        print(f'Days per Week is now {value}','\n')
                    if(secondNumber == 3):
                        self.daysPerMonth = value
                        print(f'Days per Month is now {value}','\n')
                        
                if(firstNumber == 2):
                    if(secondNumber == 4):
                        self.weeksPerYear = value
                        print(f'Weeks per Year is now {value}','\n')
                    
            elif (firstNumber > secondNumber):
                print("Units could not be resolved. They may have been in the wrong order. You can type help to show commands",'\n')
                continue
                
            else:
                print("Units could not be resolved. (Maybe you entered the same one twice?) You can type help to show commands",'\n')
                

                


    
    
    
#Main Program    
a = Assumptions()
while (exitIfFalse):
    
    Type = input ("Enter Type of Wage (e.g. Hourly, Daily, Weekly, Monthly, Yearly, etc): ")
    if (Type.lower().strip() in exitSet):
        print("Bye!")
        exitIfFalse = 0
        continue
    if (Type.lower().strip() in editSet):
        #run edit routine
        a.editAssumptions()
        continue
    if(Type.lower().strip() in helpSet):
        printHelp()
        continue
    
    Wage = input("Enter Wage (In USD): ")
    Wage = Wage.replace("$","")
    print('\n')
    if (Wage.lower().strip() in exitSet):
        print("Bye!")
        exitIfFalse = 0
        continue
    if (Wage.lower().strip() in editSet):
        #run edit routine
        a.editAssumptions()
        continue
    if(Wage.lower().strip() in helpSet):
        printHelp()
        continue
    
    if (Type.strip().lower() in hourSet):
        print(f'You entered ${Wage!s} per Hour', '\n')
        print("That would be:")
        print('$',round(float(Wage)* a.hoursPerDay)," per Day")
        print('$',round((float(Wage) * a.hoursPerWeek), 2 ),' per Week')
        print('$',round((float(Wage) * a.hoursPerWeek * a.weeksPerMonth), 2 ),' per Month')
        print('$',round((float(Wage) * a.hoursPerDay * a.daysPerYear), 2 ),' per Year', '\n')
        
        a.printAssumptions()
        continue
    
    if(Type.strip().lower() in daySet):
        print(f'You entered ${Wage!s} per Day', '\n')
        print("That would be:")
        print('$',round(float(Wage) / a.hoursPerDay , 2)," per Hour")
        print('$',round(float(Wage) * a.daysPerWeek , 2)," per Week")
        print('$',round(float(Wage) * a.daysPerMonth , 2)," per Month")
        print('$',round(float(Wage) * a.daysPerYear , 2)," per Year", '\n')
        
        a.printAssumptions()
        continue
    
    if(Type.strip().lower() in weekSet):
        print(f'You entered ${Wage!s} per Week', '\n')
        print("That would be:")
        print('$',round(float(Wage) / a.hoursPerWeek , 2)," per Hour")
        print('$',round(float(Wage) / a.daysPerWeek , 2)," per Day")
        print('$',round(float(Wage) * a.weeksPerMonth , 2)," per Month")
        print('$',round(float(Wage) * a.weeksPerYear , 2)," per Year", '\n')
        
        a.printAssumptions()
        continue
    
    if(Type.lower().strip() in monthSet):
        print(f'You entered ${Wage!s} per Month', '\n')
        print("That would be:")
        print('$',round(float(Wage) / (a.hoursPerWeek) / a.weeksPerMonth , 2)," per Hour")
        print('$',round(float(Wage) / (a.daysPerWeek) / a.weeksPerMonth , 2)," per Day")
        print('$',round(float(Wage) / a.weeksPerMonth , 2)," per Week")
        print('$',round(float(Wage) * a.monthsPerYear , 2)," per Year", '\n')
        
        a.printAssumptions()
        continue
    
    if(Type.lower().strip() in yearSet):
        print(f'You entered ${Wage!s} per Year')
        print("That would be:")
        print('$',round(float(Wage) / (a.hoursPerWeek) / a.weeksPerYear , 2)," per Hour")
        print('$',round(float(Wage) / (a.daysPerWeek) / a.weeksPerYear , 2)," per Day")
        print('$',round(float(Wage) / a.weeksPerYear , 2)," per Week")
        print('$',round(float(Wage) / a.monthsPerYear , 2)," per Month", '\n')
        
        a.printAssumptions()
        continue
    
    else:
        print("Command not recognized. Type help to see options.")
        continue  
        
        