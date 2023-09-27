- The 'combined_stats' folder contains the metrics recorded for each flow. The 4 columns stand for Time (sec), Bitrate, Delay, Jitter and Package Loss.

- The 'flows' folder contains all the commands necessary for the forwarding rules to be installed. It contains 3 flows (h4->h11, h2->h6 and h6->h7) and each of them have initial and alternate routes.

- The 'AbilineTopo.py' file is to create the network topology based on Abilene Network topology.

- The 'generate_flow_D-ITG.txt' file contains information needed to start Mininet, create the network and generate traffic using D-ITG (https://traffic.comics.unina.it/software/ITG/)

- The hw03.pdf file contains a description of the work process, results and commentary.

- The hw03.xlsx file is the file where the statistics from each flow were processed to create graphs.
