logfile = '/root/python/access.log'
ipcounter = {}

log = open(logfile)

for logline in log:

    ip = logline.split()[0]
    if ip not in ipcounter:
     
        ipcounter[ip] = 1
       
    else:

        ipcounter[ip] = ipcounter[ip] + 1
        
print(ipcounter)
log.close()
