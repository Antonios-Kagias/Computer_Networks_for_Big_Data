#!/bin/bash
sudo ovs-ofctl add-flow s6 dl_src=00:00:00:00:00:06,dl_dst=00:00:00:00:00:07,actions=output:4
sudo ovs-ofctl add-flow s6 dl_src=00:00:00:00:00:07,dl_dst=00:00:00:00:00:06,actions=output:3
sudo ovs-ofctl add-flow s8 dl_src=00:00:00:00:00:06,dl_dst=00:00:00:00:00:07,actions=output:4
sudo ovs-ofctl add-flow s8 dl_src=00:00:00:00:00:07,dl_dst=00:00:00:00:00:06,actions=output:1
sudo ovs-ofctl add-flow s9 dl_src=00:00:00:00:00:06,dl_dst=00:00:00:00:00:07,actions=output:3
sudo ovs-ofctl add-flow s9 dl_src=00:00:00:00:00:07,dl_dst=00:00:00:00:00:06,actions=output:1
sudo ovs-ofctl add-flow s11 dl_src=00:00:00:00:00:06,dl_dst=00:00:00:00:00:07,actions=output:2
sudo ovs-ofctl add-flow s11 dl_src=00:00:00:00:00:07,dl_dst=00:00:00:00:00:06,actions=output:1
sudo ovs-ofctl add-flow s10 dl_src=00:00:00:00:00:06,dl_dst=00:00:00:00:00:07,actions=output:1
sudo ovs-ofctl add-flow s10 dl_src=00:00:00:00:00:07,dl_dst=00:00:00:00:00:06,actions=output:3
sudo ovs-ofctl add-flow s7 dl_src=00:00:00:00:00:06,dl_dst=00:00:00:00:00:07,actions=output:2
sudo ovs-ofctl add-flow s7 dl_src=00:00:00:00:00:07,dl_dst=00:00:00:00:00:06,actions=output:4
