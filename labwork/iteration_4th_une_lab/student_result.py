#Accept marks of 5 subjects., total marks, percentage, grade, number of subject failed 
#----------------------------------
#Accept/input  the 5 students marks
failed = 0
sub1 = int(input("Enter the 1st subject marks:")) 
#validation
if (sub1<0):
    print("Marks should not be negative")
elif(sub1 < 40):
     failed += 1
sub2 = int(input("Enter the 2nnd subject marks:")) 
#validation
if (sub2<0):
    print("Marks should not be negative")
elif(sub2 < 40):
     failed += 1    
sub3 = int(input("Enter the 3th subject marks:")) 
#validation
if (sub3<0):
    print("Marks should not be negative")
elif(sub3 < 40):
     failed += 1    
sub4 = int(input("Enter the 4th subject marks:")) 
#validation
if (sub4<0):
    print("Marks should not be negative")
elif(sub4 < 40):
     failed += 1
sub5 = int(input("Enter the 5th subject marks:")) 
#validation
if (sub5<0):
    print("Marks should not be negative")
elif(sub5 < 40):
     failed += 1    
total_marks = 0
total_marks = sub1+sub2+sub3+sub4+sub5
print("Total Marks:",total_marks)
percentage = (total_marks/500)*100
print("Percentage",percentage,"%")
if(percentage >=90):
        print("Grade: A+")
elif(percentage>=75 and percentage<90):
        print("Grade: A")    
elif(percentage>=60 and percentage<75):
        print("Grade: B")
elif(percentage>=40 and percentage<60):
        print("Grade:C")
else:
        print("Fail")     
print("Number of Subjects Failed:", failed)            
