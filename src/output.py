import os
import json
import psycopg
from datetime import datetime


class fileOut:
    def __init__(self, output_directory):
        self.datetime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        self.output_directory = os.path.abspath(output_directory)
        os.makedirs(self.output_directory, exist_ok=True)

    def jsonOutput(self, network_status_dictionary):
        filename = 'network_status' + '_' + self.datetime + '.json'
        filepath = os.path.join(self.output_directory, filename)
        with open("{}".format(filepath), 'w') as f:
            json.dump(network_status_dictionary, f)

    def postgresAppend(self, network_status_dictionary):
        # Create connection tunnel to postgres database
        with psycopg.connect(
                dbname="<DBNAME>", 
                user="<USERNAME>",
                password="<PASSWORD>",
                host='<HOSTNAME>',
                port='<PORT>') as conn:

            # Open a cursor to perform database operations
            with conn.cursor() as cur:
                
                for client in network_status_dictionary:
                    # Pass data to fill a query placeholders and let Psycopg perform
                    # the correct conversion (no SQL injections!)
                    cur.execute(
                        """INSERT INTO network_connections
                        (datetime, ip_address, client, latitude, longitude,
                        packet_loss, min_ping, mean_ping, max_ping) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                        (client['datetime'], client['ip_address'],
                         client['client'], client['latitude'], client['longitude'],
                         client['packet_loss'], client['min_ping'], 
                         client['mean_ping'], client['max_ping']))

                    # Make the changes to the database persistent
                    conn.commit()

