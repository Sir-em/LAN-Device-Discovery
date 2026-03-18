from scapy.all import ARP, Ether, srp

def scan_network(network):
    """
    Performs an ARP scan on the specified network.

    Args:
        network (str): Example '192.168.1.0/24'

    Returns:
        list of dicts: [{'ip':..., 'mac':...}]
    """

    devices = []

    arp_request = ARP(pdst=network)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = broadcast / arp_request

    result = srp(packet, timeout=2, verbose=0)[0]

    for sent, received in result:

        device = {
            "ip": received.psrc,
            "mac": received.hwsrc
        }

        devices.append(device)

    return devices
