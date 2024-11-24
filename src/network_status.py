import pandas as pd
import platform
from subprocess import call


class readClients:
    def __init__(self, client_file, ping_count):
        self.df = pd.read_excel(client_file)
        self.client_info = self.df[["ip_address", "client", "type", 
                                    "latitude", "longitude"]]
        self.ping_count = str(ping_count)
        
    def pingClient(self, host):
        # Currently outputing ping info every time, need to fix
        param = '-n' if platform.system().lower()=='windows' else '-c'
        command = ['ping', param, self.ping_count, host]
        return call(command)

    def clientInformation(self):
        test = []
        ping = self.pingClient(self.client_info['ip_address'][0])
        test.append(ping)
        return test