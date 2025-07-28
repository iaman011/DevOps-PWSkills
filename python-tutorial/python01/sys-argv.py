import sys
#print all arguments
print ("Arguments:", sys.argv)

# Access individual arguments
if len(sys.argv) >1:
    print("First argument:", sys.argv[1])

else:
    print("No arguments provided")


# pass the parameters while running the python scripts

# PS C:\Users\iaman\OneDrive\Desktop\New folder> python sys-argv.py hello world
# Arguments: ['sys-argv.py', 'hello', 'world']
# First argument: hello