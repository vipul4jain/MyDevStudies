from lxml.builder import E
from lxml import etree as ET
import sys
import logging
from datetime import date, datetime

'''
Created by :- Vipul Jain
Input Data :- 
;Bonds_ShortName;Bonds_Name              ; Cpty_Issuer  ; Currency  ; IssueDate ; SettlementDate ; MaturityDate ; NPI;IssuerStatus;
;--------------;-----------------;----------------------;-----;----------------;---------------;-------------;-------------;----;
;AJBOND2        ;AJBOND2   ; ITC    ; USD   ; Jun 22 2016 12:00 AM;   Jun 22 2016 12:00 AM;    Jun 22 2021 12:00AM;N;NULL;
;ITC10%2016     ;ITC10%2016; ITC    ; INR   ; Jul 22 2016 12:00 AM;   Jul 22 2016 12:00 AM;    Jul 22 2021 12:00AM;N;DEFAULTER;
--
--
--
OUTPUT :- 
<root>
  <Bonds/>
  <BondsData>
    <Bonds_ShortName>AJBOND2</Bonds_ShortName>
    <Bonds_Name>AJBOND2</Bonds_Name>
    <Cpty_Issuer>ITC</Cpty_Issuer>
    <Currency>USD</Currency>
    <IssueDate>Jun 22 2016 12:00 AM</IssueDate>
    <SettlementDate>Jun 22 2016 12:00 AM</SettlementDate>
    <MaturityDate>Jun 22 2021 12:00AM</MaturityDate>
    <NPI>N</NPI>
  </BondsData>
  <BondsData>
    <Bonds_ShortName>ITC10%2016</Bonds_ShortName>
    <Bonds_Name>ITC10%2016</Bonds_Name>
    <Cpty_Issuer>ITC</Cpty_Issuer>
    <Currency>INR</Currency>
    <IssueDate>Jul 22 2016 12:00 AM</IssueDate>
    <SettlementDate>Jul 22 2016 12:00 AM</SettlementDate>
    <MaturityDate>Jul 22 2021 12:00AM</MaturityDate>
    <NPI>N</NPI>
  </BondsData>
</root>
-------------
Description:- 
    Input is the sql file with 1st line header, 2nd line ignore, data from 3rd line, ignore last 3 line
    Output is XML, each header will be the tag 
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

        logging.info(f'Headers: {Header}')
        logging.info(f'DATA : {data[2:len(data)]}')

        xmldata=(E.root(E.Bonds))

        for line in data[2:len(data)-3]:
            col = line.split(';')
            col = col[1:len(Head)]

            print(col)
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

    now = datetime.now()
    datestr = now.strftime("%Y%M%d")

    logging.basicConfig(filename=datestr+'.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info('This will get logged to a file')
    logging.info(f'first Args :{sys.argv[1]}')

    sqltoxml = ConverttoXML( inputfile, outfile)
    sqltoxml.Convert()
