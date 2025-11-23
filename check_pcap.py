import dpkt
import socket

def main():
    with open('port.pcapng', 'rb') as f:
        pcap = dpkt.pcapng.Reader(f)
        count = 0
        for ts, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            if not isinstance(eth.data, dpkt.ip.IP):
                continue
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print(f"Packet {count}: {src} -> {dst}")
            count += 1
            if count >= 10:
                break

if __name__ == '__main__':
    main()
