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
        filepath = os.path.join(self.output_directory, filename)
        with open("{}".format(filepath), 'w') as f:
            json.dump(network_status_dictionary, f)
