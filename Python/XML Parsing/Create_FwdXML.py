from lxml.builder import E
from lxml import etree as ET

Act="INSERT"
page = (
    E.KPLUSFEED(
           E.HEADER
           ( {'Primary': 'ForwardDeals'},
               E.TableName('ForwardDeals', type("S")),
			   E.Action(Act, type("C")),
               E.DateFormat('DD/MM/YYYY hh:mm:ss', type("S")),
               E.TradeKast('Y', type("S")),
               E.ExecCustomProc('Y', type("S")),
               E.SetDefaultValues('Y', type("S"))
           ),
           E.PRIMARY
           (
               E.ForwardDeals
               (
                   E.DealStatus('V Valid',type("S")),
                   E.TradeDate('12/12/2019',type("D"))
               ),
               E.Cpty
               (
                   E.CptyShortName("CITI")
               )
           )
        )
)

print (ET.tostring(page, pretty_print=True).decode("utf-8"))