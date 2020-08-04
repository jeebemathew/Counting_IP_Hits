logfile = '/root/python/access.log'
log = open(logfile)
for logline in log:
    print(logline.split())
    break
log.close()
