#!/bin/bash
sudo ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:0b,actions=output:3
sudo ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:0b,dl_dst=00:00:00:00:00:04,actions=output:2
sudo ovs-ofctl add-flow s5 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:0b,actions=output:4
sudo ovs-ofctl add-flow s5 dl_src=00:00:00:00:00:0b,dl_dst=00:00:00:00:00:04,actions=output:1
sudo ovs-ofctl add-flow s7 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:0b,actions=output:4
sudo ovs-ofctl add-flow s7 dl_src=00:00:00:00:00:0b,dl_dst=00:00:00:00:00:04,actions=output:1
sudo ovs-ofctl add-flow s10 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:0b,actions=output:3
sudo ovs-ofctl add-flow s10 dl_src=00:00:00:00:00:0b,dl_dst=00:00:00:00:00:04,actions=output:1
sudo ovs-ofctl add-flow s11 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:0b,actions=output:3
sudo ovs-ofctl add-flow s11 dl_src=00:00:00:00:00:0b,dl_dst=00:00:00:00:00:04,actions=output:2
