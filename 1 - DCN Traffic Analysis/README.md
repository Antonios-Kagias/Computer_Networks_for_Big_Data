The Python program will open the 'trace.pcap' file (uploaded as zip). Path can be changed within the code if necessary.

This project is about an analysis of network traffic in data centres based on trace in PCAP format and extraction of traffic characteristics in the form of distributions. It contains the following:

1. Reading the trace. Extracting traffic characteristics from the trace in the form of distributions. The following features are extracted at the flow level:
- Flow size (bytes)
- Flow duration (sec)

2. Grouping packets into flows. It is based on the following header fields:
- Sender IP address
- Receiver IP address
- Sender's port number
- Receiver's port number
- Protocol (TCP or UDP)

3. Extracting the packet size distribution from all flows.

4. Categorizing traffic into (a) TCP, (b) UDP, (c) ICMP and (d) ARP and calculating the respective percentages of each category in relation to the total traffic volume.


The following libraries are required:
- dpkt
- datetime
- socket
- numpy
- matplotlib.pyplot
- statsmodels.api
