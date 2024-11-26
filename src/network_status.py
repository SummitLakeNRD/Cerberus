from ast import Try
from re import search, findall
import pandas as pd
import platform
from subprocess import Popen, PIPE


class readClients:
    def __init__(self, client_file, ping_count):
        self.df = pd.read_excel(client_file)
        self.client_info = self.df[["ip_address", "client", "type", 
                                    "latitude", "longitude"]]
        self.ping_count = str(ping_count)
        self.packet_loss = []
        self.min_ping = []
        self.mean_ping = []
        self.max_ping = []
        self.network_dict = {}
        
    def pingClient(self, host):
        # pings network clients and collects relevant metrics
        ping = Popen(["/bin/ping", "-c", self.ping_count, "-w 500", host], 
                      stdout=PIPE).stdout.read().decode("utf-8")
        ping = str(ping.splitlines()[-2:]) 
        # only collect the last two lines of ping info
        try:
            packet_loss = search("(\d+(\.\d+)?)%", ping).group()
        except AttributeError:
            packet_loss = '100% packet loss'
        try:
            ping_times = findall("\d+\.\d+", ping)
        except AttributeError:
            ping_times = ''
        return packet_loss, ping_times

    def clientInformation(self):
        for i, row in self.client_info.iterrows():
            packet_loss, ping_times = self.pingClient(row['ip_address'])
            packet_loss = search("\d+", packet_loss).group()
            try:
                min_ping = float(ping_times[0])
            except IndexError:
                min_ping = float(-9999)
            try:
                mean_ping = float(ping_times[1])
            except IndexError:
                mean_ping = float(-9999)
            try:
                max_ping = float(ping_times[2])
            except IndexError:
                max_ping = float(-9999)
            
        return packet_loss, min_ping, mean_ping, max_ping