logfile = input('Enter your accesslog name : ')
minhits = input('Enter minimum number of Hits : ')

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
