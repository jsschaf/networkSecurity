import dpkt, sys;
from scapy.all import *;

packets = scapy.all.PcapReader(sys.argv[1]);

SYN_ips = {};
SYN_ips = defaultdict(lambda:0, SYN_ips);
SYNACK_ips = {};
SYNACK_ips = defaultdict(lambda:0, SYNACK_ips);


SYN = 0x02;
SYN_ACK = 0x12;

for pkt in packets:
    if(pkt.haslayer("TCP")):
        pkt_type = pkt["TCP"].flags;

        if (pkt_type == SYN):
            #get ip address
            ip = pkt["IP"].src;
            SYN_ips[ip] += 1;


        elif (pkt_type == SYN_ACK):
            #get ip address
            ip = pkt["IP"].dst;
            SYNACK_ips[ip] += 1;

for i in SYN_ips:
    syn_sent = SYN_ips[i];
    synack_received = SYNACK_ips[i];

    if (syn_sent > (3*synack_received)):
        print(i);
