import os
import xml.etree.ElementTree as et

base_path = os.path.dirname(os.path.realpath(__file__))
print(base_path)
xml_file = os.path.join(base_path, "input.xml")
print(xml_file)


def parse_xml():
    try:
        tree = et.parse(xml_file)
    except FileNotFoundError as e:
        print(e, file = sys.stderr)
        raise
    finally:
        root = tree.getroot()

# for child in root:
# print(child.tag, "==", child.attrib)
# xml_data = {}

        for child in root:
            childtag = {}
            childtag = child.attrib
            print(childtag['id'])
            tagname = childtag['id']
            print(tagname)
            filename = base_path + '\\' + tagname + '.txt'
            print(filename)
            f = open(filename, "w+")
            for element in child:
                # print(element.tag, ":", element.text + "\n")
                f.write("ExecCustomProc Y" + "\n" )
                f.write(element.tag + ":" + element.text + "\n")
        f.close()


#xml_data[element.tag] = element.text
#print("insert into Kustom..TableName Values ( \"" + xml_data["author"] + "\"," + xml_data["price"] + ")")
#f = open(child, "w+")
#print(xml_data)


if __name__ == "__main__":
    parse_xml()
