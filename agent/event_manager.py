import time

class EventManager:

    def __init__(self, unit_id):

        self.unit_id = unit_id

        # previous scan device map
        self.previous_devices = {}

    def process_scan(self, devices):

        events = []

        current_ips = set()

        for device in devices:

            ip = device["ip"]
            mac = device["mac"]

            current_ips.add(ip)

            # new device detected
            if ip not in self.previous_devices:

                events.append(
                    self.create_event(ip, mac, "DEVICE_JOINED")
                )

            # mac address change
            elif self.previous_devices[ip] != mac:

                events.append(
                    self.create_event(ip, mac, "MAC_CHANGE")
                )

            self.previous_devices[ip] = mac

        # detect devices leaving network
        for ip in list(self.previous_devices.keys()):

            if ip not in current_ips:

                events.append(
                    self.create_event(
                        ip,
                        self.previous_devices[ip],
                        "DEVICE_LEFT"
                    )
                )

                del self.previous_devices[ip]

        return events

    def create_event(self, ip, mac, event_type):

        return {
            "unit_id": self.unit_id,
            "device_ip": ip,
            "mac": mac,
            "event": event_type,
            "timestamp": time.time()
        }