from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument()
parser.add_argument()
parser.add_argument()
parser.add_argument()
parser.add_argument()
parser.add_argument()
args = parser.parse_args()


def main():
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
#       then --> 1) send message to SWEON slack channel
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
#
#
#
#
#
#

if __name__ == '__main__':
    main()
