from re import findall
import pandas as pd
import platform
from subprocess import Popen, PIPE


class readClients:
    def __init__(self, client_file, ping_count):
        self.df = pd.read_excel(client_file)
        self.client_info = self.df[["ip_address", "client", "type", 
                                    "latitude", "longitude"]]
        self.ping_count = str(ping_count)
        
    def pingClient(self, host):
        # Currently outputing ping info every time, need to fix
        ping = Popen(["/bin/ping", "-c 10", "-w 500", host], 
                      stdout=PIPE).stdout.read().decode("utf-8")
        try:
            net_info = findall(r'\d*[.,]?\d*', ping)
        except AttributeError:
            net_info = '0.000/0.000/0.000/0.000 ms'
        return ping

    def clientInformation(self):
        test = self.pingClient(self.client_info['ip_address'][0])
        return test