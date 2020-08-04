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
    if hits >= 1000:
        print(ip,hits)

log.close()
