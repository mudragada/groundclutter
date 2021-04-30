"""
Objective
---------
In this challenge, we're going to learn about the difference between a class and an instance; because this is an Object Oriented concept, it's only enabled in certain languages. Check out the Tutorial tab for learning materials and an instructional video!

Task
Write a Person class with an instance variable,"age", and a constructor that takes an integer,"initialAge", as a parameter. The constructor must assign to after confirming the argument passed as is not negative; if a negative argument is passed as , the constructor should set to

and print Age is not valid, setting age to 0.. In addition, you must write the following instance methods:

    yearPasses() should increase the

instance variable by
.
amIOld() should perform the following conditional actions:

    If

, print You are young..
If
and

        , print You are a teenager..
        Otherwise, print You are old..

To help you learn by example and complete this challenge, much of the code is provided for you, but you'll be writing everything in the future. The code that creates each instance of your Person class is in the main method. Don't worry if you don't understand it all quite yet!

Note: Do not remove or alter the stub code in the editor.

Input Format

Input is handled for you by the stub code in the editor.

The first line contains an integer,
(the number of test cases), and the subsequent lines each contain an integer denoting the

of a Person instance.

Constraints

Output Format

Complete the method definitions provided in the editor so they meet the specifications outlined above; the code to test your work is already in the editor. If your methods are implemented correctly, each test case will print
or lines (depending on whether or not a valid was passed to the constructor).

"""
class Person():
    age = 0
    def __init__(self,initialAge):
        if(initialAge > 0):
            self.age = initialAge
        else:
            print("Age is not valid, setting age to 0.")
            self.age = 0

    def yearPasses(self):
        self.age += 1
    def amIOld(self):
        if(self.age < 13):
            print("You are young.")
        elif(self.age >= 13 and self.age < 18):
            print("You are a teenager.")
        else:
            print("You are old.")

def main():
    t = 100
    for i in range(0, t):
        p = Person(i)
        p.amIOld()
        for j in range(0, 3):
            p.yearPasses()
        p.amIOld()
        print("")

if __name__ == '__main__':
    main()
