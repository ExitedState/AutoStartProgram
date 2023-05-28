import socket
import requests
import logging

logging.basicConfig(level=logging.INFO)

def check_internet_connectivity(timeout=0.5):
    # Check if we can ping a known stable server
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("1.0.0.1", 53))
        logging.info("Internet connectivity detected via DNS query to Cloudflare's DNS server.")
        return True
    except socket.error:
        pass
    # Send a simple HTTP request to a web server
    try:
        response = requests.head("http://www.google.com", timeout=timeout)
        logging.info(f"HTTP response code: {response.status_code}")
        if 200 <= response.status_code < 400:
            logging.info("Internet connectivity detected via HTTP request.")
            return True
    except (requests.ConnectionError, requests.Timeout, requests.HTTPError):
        pass

    logging.warning(
        "No internet connectivity detected. Please connect to the internet and try again.")
    return False
