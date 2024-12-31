from argparse import ArgumentParser
from src.network_status import readClients
from src.output import fileOut


parser = ArgumentParser()
parser.add_argument('client_file', type=str, 
                    help = 'provide path to xlsx file with network info')
parser.add_argument('ping_count', type=int, default=10, 
                    help = 'number of round-trip data packets to send')
parser.add_argument('timeout', type=int, default=1,
                    help = 's (linux) or ms (windows) for ping timeout')
parser.add_argument('--output_directory', type=str, default='./output/',
                    help = 'directory to output json files to')
args = parser.parse_args()


rc = readClients(args.client_file, args.ping_count, args.timeout)
f = fileOut(args.output_directory)


def main():
    # The following function gathers client information from network pings
    network_status_dict = rc.clientInformation()

    # The following function sends out messages via slack/email to a defined 
    # user list when network clients have been non-functional for a certain
    # amount of time
    # watchdogNotification()
    # tutorial: https://www.datacamp.com/tutorial/how-to-send-slack-messages-with-python 

    # The following function writes the network ping metrics to a json output
    # or to a PostgreSQL database (comment out if you don't want one)
    f.jsonOutput(network_status_dict)
    f.postgresAppend(network_status_dict)


if __name__ == '__main__':
    main()
