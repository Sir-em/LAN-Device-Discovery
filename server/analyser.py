AUTHORIZED_MACS = [
    "A4:5E:60:22:11:FF",
    "88:31:AA:CC:DD:22"
]


def analyze_log(log):

    mac = log["mac"]

    if mac not in AUTHORIZED_MACS:

        print("ALERT: Unauthorized device detected:", mac)
