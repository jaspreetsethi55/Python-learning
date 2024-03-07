import os

print(dir(os)) # will give all functions being used with os module. dir(modulename) - to list any module functions

print(os.getcwd()) #Get current working directory
print(os.chdir('/home/jsethi/python/Mark-Lutz/')) #Changing directory
print(os.getcwd())

print(os.listdir()) ##List of files/dir in current dir, we can also pass a path to list all files/dir from any other dir E.g. os.listdir('/tmp/')
print(os.listdir('/tmp/jsethi/python/'))

os.mkdir('test0') ##Will create a directory 'test0' in our current directory
os.makedirs('test1/test2') ##Create dire recursively(similar to mkdir -p) i.e. will first create 'test' in cwd then 'test2' in cwd/test1/
os.mkdir('test3/test4') ##will give error if test3 is not there

os.rmdir('test0')
os.removedirs('test1/test2') ##Delete dir recursively

os.rename('test.txt','test_new.txt') ##Renaming files

os.stat('test_new.txt') ##All info about file. Similar to linux 'stat' command. Output is not human friendly
os.stat('test_new.txt').st_size ##size in bytes
os.stat('test_new.txt').st_mtime ##Modification timestamp. Returns timestamp which is not in human readable format
##Converting aboce timestamp in human readbale format
from datetime import datetime
mod_time = os.stat('test_new.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

##Recursively traversing any directory os.walk
##os.walk - A generator that yields a tuple of 3 values while walking over directory tree. 1. dir path 2.List of dir withing that path 3. List of Files within that path
for path,dirname,dirfiles in os.walk('/home/jsethi/python/Mark-Lutz/'):
    print('Current Path:',path)
    print('Directories:',dirname)
    print('Files:',dirfiles)
    print()

##Environment variable
os.environ ##Prints all environment variables
os.environ.get('HOME') ##User's home directory env variable

file_path = os.environ.get('HOME') + 'test.txt'
##But sometimes os.environ.get('HOME') may not contain slash(/) at end, so we need to use '/' while concatenating and sometimes it may have '/', so if we use '/' then it may be doubled. So to overcome all this we can use os.path.join
os.path.join(os.environ.get('HOME'),'test.txt')



