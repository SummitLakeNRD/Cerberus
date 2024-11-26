import os
import json
from datetime import datetime


class fileOut:
    def __init__(self, output_directory):
        self.datetime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        self.output_directory = os.path.abspath(output_directory)
        os.makedirs(self.output_directory, exist_ok=True)

    def output(self, network_status_dictionary):
        filename = 'network_status' + '_' + self.datetime + '.json'
        with open("{}".format(filename), 'w') as f:
            json.dump(network_status_dictionary, f)
