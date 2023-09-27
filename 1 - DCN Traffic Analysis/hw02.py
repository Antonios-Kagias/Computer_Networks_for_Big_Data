# -*- coding: utf-8 -*-
"""
Use DPKT to read in a pcap file. Some code was used from
https://dpkt.readthedocs.io/en/latest/_modules/examples/print_packets.html

The following code:
- Extracts flows using TCP, UDP protocols
- Plots the CDF of the above flows' sizes and durations
- Plots the CDF of all packets' sizes
- Categorises traffic into TCP, UDP, ICMP and ARP
- Calculates the number of packets for each one of the above
- Plots a bar graph for these packets
- Calculates the respective percentages of each category in relation to the total traffic volume

DPKT library download required
"""

#!/usr/bin/env python
#!pip install dpkt

# Libraries required
import dpkt
import datetime
import socket
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


# Function to add value labels to bar graph
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')


def inet_to_str(inet):
    """Convert inet object to a string

        Args:
            inet (inet struct): inet network address
        Returns:
            str: Printable/readable IP address
    """
    # First try ipv4 and then ipv6
    try:
        return socket.inet_ntop(socket.AF_INET, inet)
    except ValueError:
        return socket.inet_ntop(socket.AF_INET6, inet)


def print_packets(pcap):
    """Print out information about each packet in a pcap

       Args:
           pcap: dpkt pcap reader object (dpkt.pcap.Reader)
    """
    
    # Dictionary to store TCP and UDP flows
    tcp_udp_flows = {}

    # Array to store flow sizes
    sizes = []
    # Array to store flow durations
    durations = []
    # Array to store packet sizes
    packets = []

    # Store number of ARP packets
    arp_packets = 0
    # Store number of TCP packets
    tcp_packets = 0
    # Store number of UDP packets
    udp_packets = 0
    # Store number of ICMP packets
    icmp_packets = 0


    # For each packet in the pcap process the contents
    for timestamp, buf in pcap:

        # Unpack the Ethernet frame (mac src/dst, ethertype)
        eth = dpkt.ethernet.Ethernet(buf)

        # Make sure the Ethernet data contains an IP packet
        if not isinstance(eth.data, dpkt.ip.IP):
            # Count how many ARP packets there are
            if hasattr(eth, "arp"):
                arp_packets += 1
            continue

        # Now unpack the data within the Ethernet frame (the IP packet)
        # Pulling out src, dst, length, fragment info, TTL, and Protocol
        ip = eth.data

        # Add flow to dictionary if the protocol used is TCP or UDP
        if (ip.p == dpkt.ip.IP_PROTO_TCP):
            TCP = ip.data
            proto = 'TCP'
            srcport = TCP.sport
            dstport = TCP.dport
            # Group packet into tcp_udp_flows based on source IP, destination IP, source port, destination port and protocol
            flow_key = (inet_to_str(ip.src), inet_to_str(ip.dst), srcport, dstport, proto)
            if flow_key not in tcp_udp_flows:
                tcp_udp_flows[flow_key] = []
            # Append the packet to the corresponding flow list
            # Keep packet size and timestamp to calculate duration of the flow later
            tcp_udp_flows[flow_key].append((ip.len, datetime.datetime.utcfromtimestamp(timestamp)))
        elif (ip.p == dpkt.ip.IP_PROTO_UDP):
            UDP = ip.data
            proto = 'UDP'
            srcport = UDP.sport
            dstport = UDP.dport
            # Group packet into tcp_udp_flows based on source IP, destination IP, source port, destination port and protocol
            flow_key = (inet_to_str(ip.src), inet_to_str(ip.dst), srcport, dstport, proto)
            if flow_key not in tcp_udp_flows:
                tcp_udp_flows[flow_key] = []
            # Append the packet to the corresponding flow list
            # Keep packet size and timestamp to calculate duration of the flow later
            tcp_udp_flows[flow_key].append((ip.len, datetime.datetime.utcfromtimestamp(timestamp)))
        
        
        # Store ALL packets' size for plotting later
        packets.append(ip.len)

        
        # Count how many TCP, UDP and ICMP packets there are
        if (ip.p == dpkt.ip.IP_PROTO_TCP):
            tcp_packets += 1
        elif (ip.p == dpkt.ip.IP_PROTO_UDP):
            udp_packets += 1
        elif (ip.p == dpkt.ip.IP_PROTO_ICMP):
            icmp_packets += 1
        
        
    # For each flow, calculate size and duration
    for key, value in tcp_udp_flows.items():
        # Remember, we appended to tcp_udp_flows size and timestamp together
        flow_size = sum(i[0] for i in value)
        start_time = min(i[1] for i in value)
        end_time = max(i[1] for i in value)
        flow_duration = end_time - start_time
        # Convert to seconds
        flow_duration = flow_duration.total_seconds()
        # Add to arrays for plotting
        sizes.append(flow_size)
        durations.append(flow_duration)

    # Convert to numpy array
    sizes = np.array(sizes)
    durations = np.array(durations)

    # Calculate number of all packets
    all_packets = arp_packets + tcp_packets + udp_packets + icmp_packets

    # Calculate percentages
    arp_packets_perc = round((arp_packets/all_packets)*100, 2)
    tcp_packets_perc = round((tcp_packets/all_packets)*100, 2)
    udp_packets_perc = round((udp_packets/all_packets)*100, 2)
    icmp_packets_perc = round((icmp_packets/all_packets)*100, 2)

    # Print results
    print(f"The number of ARP packets is {arp_packets} and corresponds to {arp_packets_perc}% of the traffic")
    print(f"The number of TCP packets is {tcp_packets} and corresponds to {tcp_packets_perc}% of the traffic")
    print(f"The number of UDP packets is {udp_packets} and corresponds to {udp_packets_perc}% of the traffic")
    print(f"The number of ICMP packets is {icmp_packets} and corresponds to {icmp_packets_perc}% of the traffic")
    print(f"The number of all packets is {all_packets}\n")

    
    # Graph for TCP-UDP flows' sizes distribution
    # Get data from the appropriate array
    sizes_sorted = np.sort(sizes)
    # Get the CDF of the data array as a step function
    ecdf = sm.distributions.ECDF(sizes_sorted)
    # Smooth the lines
    x = np.linspace(min(sizes_sorted), max(sizes_sorted))
    y = ecdf(x)
    plt.step(x, y, label="CDF")
    plt.legend()
    plt.title("CDF of TCP-UDP flows' sizes")
    plt.show()
    print("\n")

    # Graph for flows' durations distribution
    # Get data from the appropriate array
    durations_sorted = np.sort(durations)
    # Get the CDF of the data array as a step function
    ecdf = sm.distributions.ECDF(durations_sorted)
    # Smooth the lines
    x = np.linspace(min(durations_sorted), max(durations_sorted))
    y = ecdf(x)
    plt.step(x, y, label="CDF")
    plt.legend()
    plt.title("CDF of TCP-UDP flows' durations")
    plt.show()
    print("\n")

    # Graph for packets' sizes distribution
    # Get data from the appropriate array
    packets_sorted = np.sort(packets)
    # Get the CDF of the data array as a step function
    ecdf = sm.distributions.ECDF(packets_sorted)
    # Smooth the lines
    x = np.linspace(min(packets_sorted), max(packets_sorted))
    y = ecdf(x)
    plt.step(x, y, label="CDF")
    plt.legend()
    plt.title("CDF of packets' sizes")
    plt.show()
    print("\n")

    # Graph for number of packets per each protocol
    protocols = ("ARP", "TCP", "UDP", "ICMP")
    protocol_values = (arp_packets, tcp_packets, udp_packets, icmp_packets)
    fig = plt.figure(figsize = (10, 5))
    plt.bar(protocols, protocol_values, color ='teal', width = 0.4)
    # Call the function to add value labels
    addlabels(protocols, protocol_values)
    plt.xlabel("Protocols")
    plt.ylabel("No. of packets")
    plt.title("Packets per each protocol")
    plt.show()
    print("\n")


def test():
    """Open the pcap file"""
    with open('trace.pcap', 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        print_packets(pcap)



if __name__ == '__main__':
    test()
