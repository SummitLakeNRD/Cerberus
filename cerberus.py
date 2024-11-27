from argparse import ArgumentParser
from src.network_status import readClients
from src.output import fileOut


parser = ArgumentParser()
parser.add_argument('client_file', type=str, 
                    help = 'provide path to xlsx file with network info')
parser.add_argument('ping_count', type=int, default=10, 
                    help = 'number of round-trip data packets to send')
parser.add_argument('timeout', type=int, default=500,
                    help = 'time in ms for ping timeout')
parser.add_argument('--output_directory', type=str, default='./output/',
                    help = 'directory to output json files to')
#parser.add_argument()
#parser.add_argument()
args = parser.parse_args()


rc = readClients(args.client_file, args.ping_count, args.timeout)
f = fileOut(args.output_directory)


def main():
    network_status_dict = rc.clientInformation()
    #print(network_dict)

    # watchdogNotification()

    # databaseAppend()

    # This will be a temporary function used to write connection metrics 
    # to json files until the postgreSQL database is ready to use
    f.output(network_status_dict)

############# PROGRAM OVERVIEW ##################
# Program will automatically run once every fifteen minutes per service file
# directions. It will need to:
# 1) read in csv containing list of network clients w/ IP addresses & other info
# 2) send 10 ping packets to each network client and record info:
#   - packet drop rate
#   - avg ping
#   - min ping
#   - max ping
# 3) Check for disconnection of network clients
#   if:
#       client has been disconnected for 4 hours (?)
#       create cached list (tuple or text file?) with 16 rows for 4 hours (only disconnected clients)
#       then --> 1) send message to SWEON slack channel https://www.datacamp.com/tutorial/how-to-send-slack-messages-with-python
#                2) email keane, james, & others (?)
#                - equipment type, location, other info
#   else:
#       continue
# 4) write the following info to postgreSQL database:
#   - datetime
#   - ip address
#   - equipment name (?)
#   - packet drop rate (0-1)
#   - avg ping
#   - min ping
#   - max ping
#################################################


if __name__ == '__main__':
    main()
