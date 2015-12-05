__author__ = 'Krishna Mudragada'


from xml.dom import minidom

doc = minidom.parse("claimableRepository.xml")

itemDescriptors = doc.getElementsByTagName("item-descriptor")

for itd in itemDescriptors:
    itemDescriptorName = itd.getAttribute("name")
    tables = itd.getElementsByTagName("table")
    print("**** %s ****" % (itemDescriptorName))
    tableNames = ','.join([str(table.getAttribute("name")) for table in tables])
    for table in tables:
        tableName = table.getAttribute("name")
        properties = table.getElementsByTagName("property")
        for property in properties:
            propertyName = property.getAttribute("name")
            columnName = property.getAttribute("column-name")
            print("%s\t%s\t%s " % (propertyName, tableName, columnName ))


