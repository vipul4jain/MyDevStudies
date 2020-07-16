from xml.dom import minidom
import xml.etree.ElementTree as et



top = et.Element('KPLUSFEED')

comment = et.Comment('Deal Message')
top.append(comment)

child = et.SubElement(top, 'TableName')
child.text = 'This child contains text.'

child_with_tail = et.SubElement(top, 'child_with_tail')
child_with_tail.text = 'This child has regular text.'
child_with_tail.tail = 'And "tail" text.'

child_with_entity_ref = et.SubElement(top, 'child_with_entity_ref')
child_with_entity_ref.text = 'This & that'

#print (et.tostring(top).decode("utf-8"))
rough_string=et.tostring(top, 'utf-8')
reparsed = minidom.parseString(rough_string)
print(reparsed.toprettyxml(indent="  "))
 