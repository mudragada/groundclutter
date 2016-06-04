__author__ = 'v-mudrak-8l'


fileDesc = open("/Users/v-mudrak-8l/Desktop/category.page.js")

for i, line in enumerate(fileDesc):
    if i == 70:
        print line[433588:433600]

fileDesc.close()