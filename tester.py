import DiscoveryComm
import time

def test_discovery():
    mycomm = DiscoveryComm.DiscoveryComm()
    mycomm.start_network_discovery()
    while True:
        print(f"Host info: {mycomm.get_info()}")
        time.sleep(5)

if __name__ == "__main__":
    test_discovery()