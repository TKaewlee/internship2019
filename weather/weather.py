
# coding: utf-8

# # WEATHER 2019
# [reference]  
# tutorial on XML processing with lxml.etree https://lxml.de/tutorial.html     
# Python XML with ElementTree: Beginner's Guide https://www.datacamp.com/community/tutorials/python-xml-elementtree   
# 
# Python Dictionary https://www.programiz.com/python-programming/dictionary  
# How to use JSON with Python https://developer.rhino3d.com/guides/rhinopython/python-xml-json/  
# JSON Formatter https://jsonformatter.curiousconcept.com/  
# 
# 

# In[203]:


import xml.etree.cElementTree as et
import json

##Convert Function 
def XML_to_JSON(filename):
    # read .xml file
    filexml = filename + ".xml"
    parsedXML = et.parse(filexml)
    
    # temporary dictionary
    temp = dict()
    
    # access node from root
    for node in parsedXML.getroot():
        temp[node.tag] = node.attrib
        
        # access child from node
        for child in node.iter() :
            if node.tag != child.tag: 
                if child.attrib:
                    temp[node.tag][child.tag] = child.attrib
                elif child.text:
                    temp[node.tag][child.tag] = child.text
                    
    filejson = "./" + filename + ".json"
    with open(filejson, 'w') as write_file:
        json.dump(temp, write_file)
    print("Finished convert XML to JSON")
        
print('Please put your filename: ')
filename = input()
XML_to_JSON(filename)

