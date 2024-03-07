######Getting output of linux command - using os######
import os

cmd = 'ls -ltrh'

output = os.popen(cmd)
print(output) ##This will print just an generator object::
'''
<open file 'ls -ltrh', mode 'r' at 0x7f522b4e25d0>
'''

#We need to convert it to list by using 'list' function
print(list(output))

#or we can directly apply loop on results:
for line in os.popen(cmd):
    print(line.rstrip())


##Get return status + Run command(showing output on screen but not capturing it)
r_code = os.system(cmd) ##Runs command and prints output on screen
print(r_code) ##get return status 






######Getting return-status/output of linux command - using subprocess######
import subprocess

cmd = 'ls -ltrh'

#For return status(call) - Run the command described by args. Wait for command to complete, then return the returncode attribute.
##subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)

return_status = subprocess.call(["ls","-ltrh"]) ##By passing arguments in form of list
print(return_status)

return_status = subprocess.call(cmd,shell=True) ##By passing complete command, use shell=True. Altough, as per python documentation, invoking the system shell with shell=True can be a security hazard if combined with untrusted input
print(return_status)

##For getting output(check_output) - Run command with arguments & return its output as a byte string.use decode('utf-8') to convert output to string
#subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)
##If the return code was non-zero it raises a CalledProcessError. The CalledProcessError object will have the return code in the returncode attribute and any output in the output attribute.

output = subprocess.check_output(["ls","-ltrh"]) ##By passing arguments in form of list
print(output)

output = subprocess.check_output(cmd,shell=True) ##By passing complete command, use shell=True. Altough, as per python documentation, invoking the system shell with shell=True can be a security hazard if combined with untrusted input
print(output)
print(type(output)) ##This will be 'bytes'
output = output.decode("utf-8") ##converting to string
print(output)
for line in output.split("\n"): ##Need to split output by new-line for applying loop on it
    print('popen:' + line)

#output = subprocess.check_output('ls abc.txt',shell=True) ##This will raise CalledProcessError since return code was non-zero as there is no file names as abc.txt'
''' script will die with below error
ls: cannot access abc.txt: No such file or directory
Traceback (most recent call last):
  File "run_linux_commands.py", line 58, in <module>
      output = subprocess.check_output('ls abc.txt',shell=True) ##This will raise CalledProcessError since return code was non-zero as there is no file names as abc.txt
        File "/usr/lib64/python3.4/subprocess.py", line 617, in check_output
            raise CalledProcessError(retcode, process.args, output=output)
            subprocess.CalledProcessError: Command 'ls abc.txt' returned non-zero exit status 2
'''

##To also capture standard error in the result, use stderr=subprocess.STDOUT:
output_error = subprocess.check_output('ls abc.txt; exit 0',stderr=subprocess.STDOUT,shell=True) ##In this case script eill not die, since we used exit 0
print(output_error)#b'ls: cannot access abc.txt: No such file or directory\n'


##subprocess.check_call is similar to subprocess.check_output but it returns return_status in place of output
