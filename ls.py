import os
from pathlib import Path
import subprocess
import argparse

pth = Path()

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--all", action="store_true")

args = parser.parse_args()


files = []
for fl in pth.cwd().iterdir():
	if args.all == False:
		if fl.name[0] != '.':
			files.append(fl.name)
	else:
		files.append(fl.name)

print(*files, sep="  ")
