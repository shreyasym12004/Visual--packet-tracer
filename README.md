Visual Packet Tracker

Visual Packet Tracker is a Python-based tool that parses network packets from a .pcap file and visualizes the communication paths between source and destination IP addresses on a geographic map using KML (Keyhole Markup Language).
The generated KML output can be loaded into tools like Google Earth to visualize global packet flows.

📌 Features

Parses .pcap files using the dpkt library

Extracts source and destination IP addresses

Uses GeoIP (GeoLiteCity.dat) to retrieve latitude and longitude

Generates KML visualizations for mapping packet trajectories

Outputs placemarks and line paths showing network communication

Helps in network forensics and traffic visualization
