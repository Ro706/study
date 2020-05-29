#study progarm
#NO CODE IS RUN HERE,IT IS TELLING US WHAT WE WILL DO LATER
#HERE WE WILL DEFINE OUR FUNCTIONS
#THIS PRINT THE MAIN MENU AND PROMPTS FOR A CHOICE

def menu():
   #print what options you have
   print "welcome to calculator.py"
   print "your options are:"
   print ""
   print "1)gravity"
   print "2)force"
   print "3)current"
   print "4)Quit calculator.py"
   print ""
   return input("choose your option:")
#THIS MULTIPLIES THREE NUMBER THEN DIVIDED BY r ** 2 GIVEN
def gravity(G,m1,m2,r):
    print G,"*",m1,"*",m2,"/",r**2,"=",G*m1*m2/r**2

#THIS MULTIPLIES TWO NUMBERS GIVEN
def force(m,g):
    print m,"*",g,"=",m*g

#THIS DIVIDES TWO NUMBERS GIVEN
def current(q,t):
    print q,"/",t,"=",q/t


#NOW THE PROGRAM REALLY STARTS,AS CODE IS RUN
loop = 1
choice = 0
while loop == 1:
  choice = menu()
  if choice == 1:
      gravity(input("G:"),input("m1:"),input("m2:"),input("r"))
  elif choice == 2:
      force(input("m:"),input("g:"))
  elif choice == 3:
      current(input("q:"),input("t:"))
  elif choice == 4:
      loop = 0
print "thank u for using study.py!"

#NOW THE PROGRAM REALLY FINISHES
