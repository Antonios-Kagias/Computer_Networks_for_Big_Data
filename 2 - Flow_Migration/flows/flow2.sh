#!/bin/bash
sudo ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:06,actions=output:3
sudo ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:06,dl_dst=00:00:00:00:00:02,actions=output:2
sudo ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:06,actions=output:4
sudo ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:06,dl_dst=00:00:00:00:00:02,actions=output:2
sudo ovs-ofctl add-flow s6 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:06,actions=output:3
sudo ovs-ofctl add-flow s6 dl_src=00:00:00:00:00:06,dl_dst=00:00:00:00:00:02,actions=output:1
