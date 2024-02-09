import socket
import json
import threading
import time
import platform
import subprocess


class DiscoveryComm:
    def __init__(self, discovery_port=15390, file_port=15122, interval=5):
        self.discovery_port = discovery_port  # port to monitor
        self.file_port = file_port # port to transfer files
        self.discovery_interval = interval  # interval for broadcasting
        self.name = socket.gethostname()  # my name
        if platform.system() == "Windows":
            self.ip = socket.gethostbyname(self.name)  # my ip
        else:
            try:
                self.ip = self.get_ip()
            except:
                print("Unrecognized OS!")
        init_info = {
            "ip": self.ip,
            "name": self.name
        }
        self.neighbors = [init_info]  # members already identified by me
        # initialize socket
        # if not hasattr(socket, 'SO_REUSEPORT'):
        #     socketopn = socket.SO_REUSEADDR
        # else:
        #     socketopn = socket.SO_REUSEPORT
        
        self.discovery_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        # self.discovery_socket.setsockopt(socket.SOL_SOCKET, socketopn, 1)
        self.discovery_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        # self.receiver_socket.setsockopt(socket.SOL_SOCKET, socketopn, 1)
        self.receiver_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.receiver_socket.bind(('', self.discovery_port))

        self.file_sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.file_receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    
    # returns the summary about this node
    def get_info(self):
        host_info = {
            "ip": self.ip,
            "name": self.name,
            "neighbors": self.neighbors
        }
        return host_info

    def get_send_info(self):
        send_info = {
            "ip": self.ip,
            "neighbors": self.neighbors
        }
        return send_info
    
    # updates own status from received info
    def update_status(self, info):
        updated_neighbors = []
        seen_ips = []
        for node in (self.neighbors + info["neighbors"]):
            if node["ip"] not in seen_ips:
                updated_neighbors.append(node)
                seen_ips.append(node["ip"])
        self.neighbors = updated_neighbors

    # send discovery message to nearby machines
    def send_discovery_message(self):
        while True:
            host_list = self.get_send_info()
            self.discovery_socket.sendto(json.dumps(host_list).encode('utf-8'), ('<broadcast>', self.discovery_port))
            #print(f"Sent discovery message: {host_list}")
            time.sleep(self.discovery_interval)

    # receive discovery message from nearby machines
    def receive_discovery_messages(self):
        while True:
            data, addr = self.receiver_socket.recvfrom(1024)
            if data:
                received_info = json.loads(data.decode('utf-8'))
                if received_info["ip"] != self.ip:
                    print(f"Received discovery message: {received_info}")
                    self.update_status(received_info)

    # start discovering nearby machines in the network and update the list accordingly
    def start_network_discovery(self):
        send_thread = threading.Thread(target=self.send_discovery_message)
        receive_thread = threading.Thread(target=self.receive_discovery_messages)

        send_thread.start()
        receive_thread.start()
    
    # send file to detination host
    def send_file(self, dest_ip, file_path):
        with open(file_path, 'rb') as file:
            file_data = file.read()
        
        try:
            self.file_sender_socket.connect((dest_ip, self.file_port))
            self.file_sender_socket.send(file_data)
        except Exception as e:
            print(f"Error sending file to {dest_ip}: {e}")

    # receive file from source host
    def receive_file(self, source_ip, save_path):
        try:
            self.file_receiver_socket.bind(('', self.file_port))
            self.file_receiver_socket.listen()
            conn, addr = self.file_receiver_socket.accept()
            with conn:
                file_data = conn.recv(4096)
                with open(save_path, 'wb') as file:
                    file.write(file_data)
        except Exception as e:
            print(f"Error receiving file from {source_ip}: {e}")

    # start a thread to transfer file
    def initiate_file_transfer(self, dest_ip, file_path):
        send_thread = threading.Thread(target=self.send_file, args=(dest_ip, file_path))
        send_thread.start()

    # start a thread to receive file
    def receive_file_transfer(self, source_ip, save_path):
        receive_thread = threading.Thread(target=self.receive_file, args=(source_ip, save_path))
        receive_thread.start()