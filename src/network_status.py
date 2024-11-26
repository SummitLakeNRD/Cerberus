import platform
import pandas as pd
from re import search, findall
from subprocess import Popen, PIPE


class readClients:
    def __init__(self, client_file, ping_count, timeout):
        self.df = pd.read_excel(client_file)
        # Below line identifies necessary excel column  
        # names and info for program to function
        self.client_info = self.df[["ip_address", "client", "type", 
                                    "latitude", "longitude"]]
        self.ping_count = str(ping_count)
        self.packet_loss = []
        self.min_ping = []
        self.mean_ping = []
        self.max_ping = []
        self.network_dict = {}
        
    def pingClient(self, host):
        # Pings network clients and collects relevant metrics
        ping = Popen(["/bin/ping", "-c", self.ping_count, "-w 500", host], 
                      stdout=PIPE).stdout.read().decode("utf-8")
        # Only collect the last two lines of ping info
        ping = str(ping.splitlines()[-2:]) 
        try:
            packet_loss = search("(\d+(\.\d+)?)%", ping).group()
        except AttributeError:
            packet_loss = '100% packet loss'
        try:
            ping_times = findall("\d+\.\d+", ping)
        except AttributeError:
            # Creates blank value to be handled by IndexError handling below
            ping_times = ''
        return packet_loss, ping_times

    def clientInformation(self):
        # Concatenates network client information into dictionary object type
        for i, row in self.client_info.iterrows():
            packet_loss, ping_times = self.pingClient(row['ip_address'])
            packet_loss = search("\d+", packet_loss).group()
            self.network_dict[row['ip_address']] = {}
            self.network_dict[row['ip_address']]['client'] = row['client']
            self.network_dict[row['ip_address']]['latitude'] = float(row['latitude'])
            self.network_dict[row['ip_address']]['longitude'] = float(row['longitude'])
            self.network_dict[row['ip_address']]['packet_loss'] = float(packet_loss)
            try:
                self.network_dict[row['ip_address']]['min_ping'] = float(ping_times[0])
            except IndexError:
                self.network_dict[row['ip_address']]['min_ping'] = float(-9999)
            try:
                self.network_dict[row['ip_address']]['mean_ping'] = float(ping_times[1])
            except IndexError:
                self.network_dict[row['ip_address']]['mean_ping'] = float(-9999)
            try:
                self.network_dict[row['ip_address']]['max_ping'] = float(ping_times[2])
            except IndexError:
                self.network_dict[row['ip_address']]['max_ping'] = float(-9999)

        return self.network_dict