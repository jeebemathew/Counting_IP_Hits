import argparse

args = argparse.ArgumentParser()
args.add_argument('-f', type=str, help='input log file to check', required=False)
passedArgs = vars(args.parse_args())
logfile = passedArgs['f']

minhits = input('Enter minimum number of Hits : ')
if logfile == None:
    logfile = '/root/python/access.log'

ipcounter = {}

log = open(logfile)

for logline in log:

    ip = logline.split()[0]
    if ip not in ipcounter:
     
        ipcounter[ip] = 1
       
    else:

        ipcounter[ip] = ipcounter[ip] + 1
        
for ip in ipcounter:

    hits = ipcounter[ip]
    if hits >= int(minhits):
        output = '{:20} :{}'.format(ip,hits)
        print(output)

log.close()
