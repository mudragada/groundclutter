############################################################################
# basic Function
def basicFunc():
    print ("I am a basic function")
    return "End of Basic Function"
#Function Calls

basicFunc()
#Function as an Object, prints returnValue
print (basicFunc())
############################################################################
# Function with arguments

def funcArgs(arg1, arg2):
    print ("I am a Function with Args")

    print("arg1, arg2: ",arg1, arg2);
    print("type(arg1), type(arg2): ", type(arg1), type(arg2));
    print("arg1, arg2 with separator: ", arg1, arg2, sep=', ')
    print ("arg1 + arg2", arg1 + arg2, sep=': ')
    print("Type of arg1 + arg2", type(arg1 + arg2), sep = ": ")
    return 2*arg1 + 2*arg2
funcArgs(10, 20)
print(funcArgs("Krishna", "Mudragada"))

############################################################################
# Function with default arguments

def funcDefault(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# Execute the function but doesn't return anything
funcDefault(10)

# Execute the function with an override argument
print(funcDefault(10,5))

############################################################################
# Function with variable arguments

def funcVarArgs(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(funcVarArgs(1, 2, 3, 4, 5))
############################################################################
