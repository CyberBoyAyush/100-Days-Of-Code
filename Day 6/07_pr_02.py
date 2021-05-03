sub1 = int(input("Enter 1 Subject Marks\n"))
sub2 = int(input("Enter 2 Subject Marks\n"))
sub3 = int(input("Enter 3 Subject Marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("Your Are Fail because you have less than 33 % in one of subject")
elif(sub1+sub2+sub3)/3 <40:
    print("You Are Fail Due To Less % Than 40")
else:
    print("Congo!, You Are Passed")