
# Global scope definitions
f="abc"
print(type(f))
print(f)

# Delete prior definitions
del f

# Function scope definitions
def func():
    f = 123
    print(type(f))
    print(f)
func()

# Global Scope definitions
f = 3.14
print(type(f))
print (f)
