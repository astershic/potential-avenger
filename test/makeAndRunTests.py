#!/usr/bin/python

import os
from subprocess import call
import sys 
from colorama import init, Fore, Back, Style

init()

#see all folders
directory = "."
dirs = os.listdir(directory)
success = 0
count = 0
realdirs = []
for entry in dirs:
	if "test" in entry:
		count += 1
		realdirs.append(entry)

#make tests clean
for entry in realdirs:
	print(Fore.RED+"*cleaning "+entry+Fore.RESET)
	cmd1 = "make -C "+entry+" clean"
	os.system(cmd1)

#make tests
for entry in realdirs:
    print(Fore.RED+"*compiling "+entry+Fore.RESET)
    cmd1 = "make -C "+entry
    os.system(cmd1)

#run tests
for entry in realdirs:
	print(Fore.RED+"*running "+entry+Fore.RESET)
	cmd1 = "(cd "+entry+" && ./potential-avenger-launcher.py)"
	os.system(cmd1)

#compare
for entry in realdirs:
	print(Fore.RED+"*comparing "+entry+Fore.RESET)
	sys.path.append(entry)
	#sys.path.append(entry+"/compare.py")
	import compare
	#compare = imp.load_source("module.name",entry+"/compare.py")
	output = entry+"/raw_disp.out"
	gold = entry+"/raw_disp.gold"
	result = compare.main(output,gold)
	if (result == 1):
		print(Fore.GREEN+"*passed"+Fore.RESET)
	else:
		print(Fore.RED+"*failed"+Fore.RESET)
	assert(result == 1 or result == 0)
	success += result

print ""
if (success == count):
	print(Fore.GREEN+str(success)+" passed tests of "+str(count)+Fore.RESET)
else:
	print(Fore.RED+str(success)+" passed tests of "+str(count)+Fore.RESET)
