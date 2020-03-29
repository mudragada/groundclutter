from string import Template

def main():
    ## String formatting
    str1 = "You are watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)
    ## Using a template string
    templ = Template("You are watching ${title} by ${author}")
    str2 = templ.substitute(title="Advanced Python", author="Joe Marini")
    print(str2)

    ## Use a dictionary
    data = { "title": "Advanced Python", "author": "Joe Marini"}
    str = templ.substitute(data)
    print(str)

if __name__ == '__main__':
    main()
