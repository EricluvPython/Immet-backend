import DiscoveryComm
import time

def test_discovery():
    mycomm = DiscoveryComm.DiscoveryComm(100)
    mycomm.start_network_discovery()
    while True:
        print(f"Client info: {mycomm.get_info()}\n")
        time.sleep(10)

def test_filetransfer():
    mycomm = DiscoveryComm.DiscoveryComm(100)
    apple_ip = "10.27.236.109"
    win_ip = "169.254.15.133"
    mycomm.receive_file_transfer(win_ip, "./client_files/hello.txt")


if __name__ == "__main__":
    test_discovery()
    #test_filetransfer()