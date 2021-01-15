import speedtest

st = speedtest.Speedtest()
print("Download speed: ", st.download()//10**6, "Mbps")
print("Upload speed: ", st.upload()//10**6, "Mbps")
print("Ping is: ", int(st.results.ping), "MS")

##############
#Kuin menisi cmd:ssä, mutta tämä on erilainen, koska ei voi jatkuvasti ping:ata ja arvioida sen keskiarvoa ja miten paljon tuli error
#Output::
#Download speed: ASD.F Mbps
#Upload speed: ZX.C Mbps
#Ping is: QW MS
#
#
