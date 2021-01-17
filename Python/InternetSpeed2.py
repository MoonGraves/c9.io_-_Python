import psutil
import speedtest
from tabulate import tabulate

class Network_Details(object):
  def __init__(self):
    self.parser = psutil.net_if_addrs()
    self.speed_parser = speedtest.Speedtest()
    self.interfaces = self.interface()[0]

  def interface(self):
    interfaces = []
    for interface_name, _ in self.parser.items():
      interfaces.append(str(interface_name))
    return interfaces

  #Download ja upload luvut ovat jaettu suhteeseen 1-miljoonaan suuruuteen, koska pilkkun takia 
  def __repr__(self):
    downLoad = str(f"{round(self.speed_parser.download() / 1000000, 2)} Mbps")

    upLoad = str(f"{round(self.speed_parser.upload() / 1000000, 2)} Mbps")

    interface = self.interfaces
    data = {"interface: " : [interface],
            "Download: "  : [downLoad],
            "Upload: " : [upLoad]
    }

    #Muodostettaan kuin taulukko näköinen
    table = tabulate(data, headers="keys", tablefmt="pretty")
    return table


if __name__ == "__main__":
  print("Users inteface tablet: \n")
  print(Network_Details())

############################
###Output:::
#Users inteface tablet:
#
#+-------------+-------------+-----------+
#| interface:  | Download:   | Upload:   |
#+-------------+-------------+-----------+
#|     lo      | 370.77 Mbps | 95.8 Mbps |
#+-------------+-------------+-----------+
#
#
