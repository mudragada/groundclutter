__author__ = 'Krishna Mudragada'

from xml.etree import ElementTree
from xml.dom import minidom
doc = ElementTree.parse("productCatalog.xml").getroot()
for itemDescType in doc.findall("item-descriptor"):
    itemDescName = itemDescType.get("name")
    print(" Attributes :")
    #print(itemDescType.attrib)
    itemExpireTimeout = itemDescType.find("item-expire-timeout")
    
    print("**** %s ****" % (itemDescName))
    if itemExpireTimeout is None:
        itemExpireTimeout = itemDescType.get("item-expire-timeout")
    else:
        itemExpireTimeout = ""
    tables = itemDescType.findall("table")
    for table in tables:
        tableName = table.get("name")    
        print ("%s\t%s\t%s" % ( table.attrib.get("name"),table.attrib.get("type"), table.get("item-cache-size")))
    
        
    
##doc = minidom.parse("claimableRepository.xml")

##itemDescriptors = doc.getElementsByTagName("item-descriptor")

# for itd in itemDescriptors:
#     itemDescriptorName = itd.getAttribute("name")
#     tables = itd.getElementsByTagName("table")
#     print("**** %s ****" % (itemDescriptorName))
#     tableNames = ','.join([str(table.getAttribute("name")) for table in tables])
#     for table in tables:
#         tableName = table.getAttribute("name")
#         properties = table.getElementsByTagName("property")
#         for property in properties:
#             propertyName = property.getAttribute("name")
#             columnName = property.getAttribute("column-name")
#             print("%s\t%s\t%s " % (propertyName, tableName, columnName ))
