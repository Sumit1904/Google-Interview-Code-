X=[['9:00','10:30'],['12:00','13:00'],['16:00','18:00']]
xt=['9:00','20:00']
Y=[['10:00','11:30'],['12:30','14:30'],['14:30','15:00'],['16:00','17:00']]
yt=['10:00','18:30']
mt=30/60

def ischeckfree(Y, i, mt):
    prev = getstr2time(Y[0][1])
    for j in Y:
        if getstr2time(j[0]) == i:
            return 0
        if getstr2time(j[0]) < i and getstr2time(j[1]) > i:
            return 0
        if getstr2time(j[0]) > i and prev <= i and getstr2time(j[0]) >= (i+mt):
            return 1
        prev = getstr2time(j[1])
    return 0
def getstr2time(st):
    hminsplit = st.split(":")
    time = round(int(hminsplit[1])/60,2)+int(hminsplit[0])
    return time
def gettime2str(time):
    a = int(time)
    a = time - a
    hmin = str(int(time)) +":"+str(int(a*60))
    return hmin
def getSlab(xt,yt):
    time=[]
    if(getstr2time(xt[0]) < getstr2time(yt[0])):
        time.append(yt[0])
    else:
        time.append(xt[0])
    if(getstr2time(xt[1]) > getstr2time(yt[1])):
        time.append(yt[1])
    else:
        time.append(xt[1])
    return time
    

time = getSlab(xt,yt)
meeting=[]
i=getstr2time(time[0])
while(i<getstr2time(time[1])):
    if ischeckfree(Y,i,mt) and ischeckfree(X,i,mt):
        meeting.append([gettime2str(i), gettime2str(i+mt)])
    i+=0.5
        
print(meeting)
