# So this tutorial is a lot more than just the sample code. 
# While you probably can just get by with the others without watching the video, 
# this one is going to probably make no sense without the video. That said:

# This tutorial is best followed in a shell / command prompt.
# Open yours up, type python, or python3, and then follow.
import subprocess

# Say you are on windows:
# module  call command in the shell
# you can change that if you'd like, eventually.
# IF YOU ARE NOT IN A SHELL, YOU WILL SEE NO OUTPUT!
subprocess.call('dir', shell=True)
subprocess.call('echo dir', shell=True)
# aquiring output
output = subprocess.check_output('dir', shell=True)
# can be combined with the sys module to get information from the script to shell and
# back