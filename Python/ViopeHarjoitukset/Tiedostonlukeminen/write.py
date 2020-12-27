nimi = input("Minkäniminen tiedosto luodaan?:") 
teksti = open(nimi,"w")
 
sisalto = input("Mitä kirjoitetaan tiedostoon?:")
 
teksti.write(sisalto)
teksti.close()
print("Luotiin tiedosto", nimi ,"ja siihen tallennettiin teksti:",sisalto)
 
