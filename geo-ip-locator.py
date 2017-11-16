import pygeoip #importing pygeoip module

gi = pygeoip.GeoIP('GeoLiteCity.dat') #loading the file with city names
gii = pygeoip.GeoIP('GeoIP.dat') #loading the file with Country names
print gi.record_by_addr('64.233.161.99') #IP input

print gii.country_code_by_name('google.com') #SG
print gii.country_code_by_addr('64.233.161.99') #US
print gii.country_name_by_addr('64.233.161.99') #United States
print gii.country_name_by_name('google.com') #Singapore


import os

#os.system('id')

#os.system('uname -a')


"""import subprocess

cmd_str = 'uname -a'
command =   subprocess.Popen([cmd_str],stdout=subprocess.PIPE,shell=True)
(output,error) = command.communicate()
print output

"""