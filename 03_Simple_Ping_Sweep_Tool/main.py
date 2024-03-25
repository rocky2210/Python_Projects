import threading
import time
from ping3 import ping  # Importing the ping function from the ping3 module
import socket
import sys
import argparse  # Importing the ArgumentParser class from the argparse module
from color import colors, fg, bg  # Importing color-related functions from the color module

# Define the PingSweep class
class PingSweep:
    def __init__(self, targets):
        self.targets = targets  # Initialize the targets attribute with the provided targets
        self.results = {}  # Initialize an empty dictionary to store ping results
        self.output_lock = threading.Lock()  # Create a threading lock object for thread safety
        
    # Method to print the tool name and version
    def print_tool_name(self):
        print(fg.blue + "  ____  _                  ____                         ")
        print(" |  _ \\(_)_ __   __ _     / ___|_      _____  ___ _ __  ")
        print(" | |_) | | '_ \\ / _` |____\\___ \\ \\ /\\ / / _ \\/ _ \\ '_ \\ ")
        print(" |  __/| | | | | (_| |_____|__) \\ V  V /  __/  __/ |_) |")
        print(" |_|   |_|_| |_|\\__, |    |____/ \\_/\\_/ \\___|\\___| .__/ ")
        print("                |___/                            |_|     ")
        print(fg.green + "          Version 0.1 - Simple Ping Sweep Tool" + colors.reset)
        print(fg.purple + "\noptions:")  # Print section for options
        print("  -h, --help            show this help message and exit")
        print("  -i INPUT [INPUT ...], --input INPUT [INPUT ...]")
        print("                        List of IP addresses or DNS names to sweep" + colors.reset)

    # Method to resolve DNS and return IP address
    def resolve_dns(self, hostname):
        try:
            ip = socket.gethostbyname(hostname)  # Resolve hostname to IP address
            return ip
        except socket.gaierror:
            print(fg.red + f"Error: Cannot resolve DNS name {hostname}" + colors.reset)  # Print error message if DNS resolution fails
            sys.exit(1)  # Exit the program with error code 1
    
    # Method to ping the provided IP address and return the result
    def ping_address(self, ip):
        try:
            response_time = ping(ip, timeout=1)  # Ping the IP address with a timeout of 1 second
            if response_time is not None:
                result = f" {fg.green}Reachable ({ip}) - Response Time: {response_time:.2f} ms{colors.reset}"  # Print reachable message with response time
            else:
                result = f"{fg.red}Unreachable ({ip}){colors.reset}"  # Print unreachable message
        except Exception:
            result = f"{fg.orange}Error pinging {ip}{colors.reset}"  # Print error message if ping fails
        return result

    # Method to start the ping sweep
    def start_ping_sweep(self):
        self.print_tool_name()  # Print the tool name and version
        print("Ping sweep starting for target(s):", ', '.join(self.targets))  # Print the targets for the ping sweep
        print("Pinging.....")  # Print message indicating start of pinging
        for ip in self.targets:
            if ip in self.results:
                continue  # Skip if the IP address has already been pinged
            try:
                message = self.ping_address(ip)  # Ping the IP address and get the result
            finally:
                self.results[ip] = message  # Store the result in the results dictionary

        with self.output_lock:
            print("Ping results:")  # Print message indicating start of ping results
            for ip, message in self.results.items():
                print(message)  # Print each ping result

# Main function to parse command line arguments and start ping sweep  
def main():
    parser = argparse.ArgumentParser(description="Simple Ping Sweep Tool")  # Create ArgumentParser object with description
    parser.add_argument("-i", "--input", nargs="+", help="List of IP addresses or DNS names to sweep")  # Add argument for IP addresses or DNS names
    args = parser.parse_args()  # Parse command line arguments 
    
    if args.input:
        targets = args.input  # Get targets from command line arguments
    else:
        parser.error("Please specify target(s) to sweep using the -i/--input option")  # Print error message if no targets provided
    
    ping_sweep = PingSweep(targets)  # Create PingSweep object with targets
    ping_sweep.start_ping_sweep()  # Start ping sweep

if __name__ == '__main__':
    main()  # Execute main function if script is run directly
