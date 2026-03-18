import time

from arp_scanner import scan_network
from event_manager import EventManager
from log_sender import send_log

NETWORK = "192.168.1.0/24"

SCAN_INTERVAL = 30   # seconds


def main():

    manager = EventManager("LAB-01")

    print("LAN Monitoring Agent Started")

    while True:

        devices = scan_network(NETWORK)

        events = manager.process_scan(devices)

        for event in events:

            print(event)

            send_log(event)

        time.sleep(SCAN_INTERVAL)


if __name__ == "__main__":
    main()
