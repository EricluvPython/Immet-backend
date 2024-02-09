# Infinity Co. Prototype

## Introduction

This is Eric's (jingxia3) 15-390 course project. I have implemented a rudimentary peer-to-peer cloud computing framework along with GUI applications.

My vision is to provide accesible computation to all scientific researchers through the unity of idle computation resources.

## How to run the demo

To run the host app (when you want to rent out your computation power), simply do ```python3 hostGUI.py```.

To run the client app (when you want to submit a computation job), simply do ```python3 clientGUI.py```.

## Files

This section describes all the files in this project.

### Demo scripts

```clientGUI.py``` contains code that runs the client GUI. In there, the login screen is for demo only (does not actually verify or register the user), and in the main homepage you are able to select files to upload, specify the number of nodes required, and run a task using mpiexec. The returnned result could be viewed and downloaded from "review my jobs" tab. While the task is running, the virtual currency will decrease depending on the number of nodes.

```hostGUI.py``` contains code that runs the host GUI. In there, the login screen is for demo only (does not actually verify or register the user), and in the main homepage you are able to connect to and disconnect from the decentralized cloud (also for demo only). After the "connect" button is pressed, the host is connected to the cloud. After 5 seconds, a task runs on the host. After 6 seconds, the task stops, and the user is able to disconnect from the cloud.

```taskadd.py``` contains code that performs a distributed addition of 1M integers. It uses ```mpi4py``` to allow distributed computation and saves result in ```sum.txt```.

```taskmult.py``` contains code that performs a distributed multiplication of 1M integers. It uses ```mpi4py``` to allow distributed computation and saves result in ```product.txt```.


### Testing scripts

```DiscoveryComm.py``` implements a gossip-based discovery network. It contains all functionalities that allow machines connected under the same internet to discover each other, including their IP, capacity, machine name, neighboring machines, etc. This script also contains functions that transfer files among machines.

```AppleOS.py``` and ```WindowsOS.py``` were used to test the functions implemented in ```DiscoveryComm.py```.

```CommandMPI.py``` was used to experiment with running distributed jobs.


### Folders

```./assets/``` contains assets used in GUI.

```./client_files/``` and ```./host_files/``` were used when testing file transfer with ```DiscoveryComm.py```.

```./results/``` stores the output after task submitted in ```clientGUI.py``` finishes running.

## Disclaimer

The file ```taskadd.py``` was taken and modified from the recitation slides from the distributed systems course.

All the other files are my own, original creation.

## License

MIT License

Copyright (c) 2023 Jingxiang Gao

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Footnotes

The functionalities in ```DiscoveryComm.py``` were not implemented in the GUI applications because of some technical difficulties in setting up the SSH and MPI environments across machines with different OS. The frontends are for demonstration purposes only, and they do not necessarily represent the backend story I envisioned.

Due to limitatinos in time and resources, I was unable to fully implement my design for the demo frontend.

Special thanks to professor Hammoud for his committed encouragement and support! Also to my friend Zhijie who helped me understand the mechanism of MPI. Also to Hend and Kranthi for preparing the cluster for my testing.