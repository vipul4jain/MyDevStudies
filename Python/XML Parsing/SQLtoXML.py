from lxml.builder import E
from lxml import etree as ET
import sys

'''
Created by :- Vipul Jain

'''

class ConverttoXML():

    def __init__(self, inputfile, outfile):
        self._inputfile = inputfile
        self._outfile = outfile
    
    def Convert(self):
        fhand = open(self._inputfile, 'r')
        data = fhand.read().split('\n')

        Head = data[0].split(';')
        Head = Head[1:len(Head) - 1]
        Header=[]

        for elem in Head:
            Header.append(elem.replace(' ',''))

        xmldata=(E.root(E.Bonds))

        for line in data[2:len(data)-3]:
            col = line.split(';')
            col = col[1:len(Head)]
            page=(E.BondsData())

            for i in range(len(Header) - 1):
                head = Header[i]
                val = col[i].strip()
                page.append(E.head(val))
                body = page.find('head')
                body.tag = head
            
            xmldata.append(page)
        fhand.close()

        fhand = open(self._outfile, 'w')
        xmlstring = ET.tostring(xmldata, pretty_print=True).decode("utf-8")

        for line in xmlstring:
            fhand.write(line)

if __name__ == "__main__":
    inputfile = sys.argv[1]
    outfile   = sys.argv[2]

    sqltoxml = ConverttoXML( inputfile, outfile)
    sqltoxml.Convert()
