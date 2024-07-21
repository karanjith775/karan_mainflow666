#creating a set of cements
cements={'OPC','PPC','RHC','QSC'}

#adding an element in the set
cements.add('LHC')

#removing an element from the set
cements.remove('RHC')

#checking if an element exists in the set
has_PPC='PPC' is cements
print(f"Has cement:{has_PPC}")

#iterating through the set
for cement in cements:
    print(cement)
    
#original set
print(cements)
