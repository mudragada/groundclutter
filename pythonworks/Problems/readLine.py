__author__ = 'Krishna Mudragada'


fileDesc = open("~/Desktop/category.page.js")

for i, line in enumerate(fileDesc):
    if i == 70:
        print line[433588:433600]

fileDesc.close()