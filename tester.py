import DiscoveryComm
import time

def test_discovery():
    mycomm = DiscoveryComm.DiscoveryComm()
    mycomm.start_network_discovery()
    while True:
        print(f"Host info: {mycomm.get_info()}")
        time.sleep(5)

def test_filetransfer():
    mycomm = DiscoveryComm.DiscoveryComm(100)
    apple_ip = "10.27.236.109"
    win_ip = "169.254.15.133"
    mycomm.initiate_file_transfer(apple_ip, "./host_files/hello.txt")

if __name__ == "__main__":
    test_discovery()