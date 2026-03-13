import subprocess

def is_alive(ip):
    """
    Checks if a device is reachable using ICMP ping.

    Args:
        ip (str)

    Returns:
        bool
    """

    try:

        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return result.returncode == 0

    except Exception:
        return False