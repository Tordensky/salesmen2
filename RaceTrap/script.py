import subprocess
import os
import StringIO
import time

MORE_NODES = True
#nodes = ['0-3', '1-0', '1-1', '1-3', '2-0', '2-2', '2-3', '3-2', '4-3', '5-1', '6-1', '6-2', '6-3', '7-1', '7-2', '7-3', '8-0', '8-1', '8-2', '8-3', '9-0']
nodes = ['9-0']
runningNodes = ['0-0', '0-1', '0-3', '1-0', '1-1', '1-3', '2-0', '2-2', '2-3', '3-2', '4-3', '5-1', '6-1', '6-2', '6-3', '7-1', '7-2', '7-3', '8-0', '8-1', '8-2', '8-3']

def change_size(filename, size):
    f = open((filename+".c"), "r+")

    content = f.readlines()
    
    f.seek(0)
    
    f.write("#define WIDTH " + str(size) + "\n")
    f.write("#define HEIGHT " + str(size) + "\n")
    
    content.pop(0)
    content.pop(0)
    for line in content:
        
        f.write(str(line))
    
    f.close()
    
def changeNodeCount():
    output = os.popen("lamhalt").read()
       
    if len(nodes) != 0:
        runningNodes.append(nodes.pop())
        
        lamfile  = open("hosts.lam", 'w')
        for node in runningNodes:
            lamfile.write(("compute-%s\n") % (node))
            
        lamfile.close()
        
        
        
    else:
        MORE_NODES = False

    


def make(filename):
    output = os.popen(('make %s' % (file_name))).read()
    #print output

#starting the computers




#a = os.popen('lamboot -v hosts.lam').read()
#p.wait()
timelist = []
tmplist = []

sizes = [16, 32, 64, 128, 256, 512, 1024, 2048]
#sizes = [8192]

#files = ["dynamic", "master"]
files = ["RoadMap"]
runs = 1




#changeNodeCount()

time.sleep(2)

print "Execute test"

f =  open("seqTest.cvs", "w+")
columns = "nodes, filename, average, numruns, size\n"
f.write(columns)


#while (MORE_NODES):
    #f.write(("\n\nRUNNING ON %d NODES\n"%(len(runningNodes))))
    #os.popen("lamboot -v hosts.lam")
for file_name in files:
    for size in sizes:
        change_size(file_name, size)
        make(file_name)
        
        tmplist = []
        
        for i in range (0, runs):
            #a = os.popen(('mpirun C -ssi rpi tcp ./%s' % (file_name))).read()
            a = os.popen(('./%s' % (file_name))).read()
            
            
            a = StringIO.StringIO(a)
            
            sumRunning = 0
            for line in a.readlines():
                    # if line.count("Time taken:") == 1:
    
                x = line.split(" ")
                
                for count in range(0, len(x)):
                    if x[count] == "min.":
                        
                            sumRunning += int(x[count - 1]) * 60000

                    if x[count] == "seconds":
                        sumRunning += int(x[count -1])*1000

                    if x[count] == "ms":
                        ms =  int(x[count-1])
                        sumRunning += ms   

            tmplist.append(sumRunning)    
                        
        
        result =  "%s, %s, %d, %d, %d X %d\n" % (len(runningNodes), file_name, (sum(tmplist) / len(tmplist)), runs, size, size)
        print result
        f.write(result)
    #changeNodeCount()


#output = os.popen("lamhalt").read()
f.close



                           
                            
                                
                                #line = line.replace("Time taken: ","")
                                #line = line.replace(" ms" ,"")
                                #millisecond = line
                                
                                #time += int(millisecond)
                                
                                #seconds = 0
                                
                                #if line.count("seconds") == 1:
                                    #milliseconds = line[line.find("seconds ") + 8 :]
                                    #line = line.replace(" seconds ", "")
                                    #seconds = line[:-len(milliseconds)]
                                    #time += int(seconds)* 1000
                                    ##+ int(milliseconds)
                                
                                #if line.count("seconds") == 1:
                                    #milliseconds = line[line.find("seconds ") + 8 :]
                                    #line = line.replace(" seconds ", "")
                                    #seconds = line[:-len(milliseconds)]
                                    #time += int(seconds)* 1000
                                    ##+ int(milliseconds)
                                
                                #print time
                                    
                                
                                
                                
                                
                #f.write(str(tmplist))
                #f.write("\n\n")
                #timelist.extend(tmplist)
                
                #print "completed iteration : " + str(i);
        #print "test run"
            #result =  "file: %s Avg: %5dms of %2d iters of size %d X %d\n" % (file_name, (sum(tmplist) / len(tmplist)), runs, size, size)
    
        

#totaltime = 0
#for time in timelist:
        #totaltime += time

#avgtime = totaltime/len(timelist) 
#f.write("avg time : " + str(avgtime))
#print "avg time : " + str(avgtime);

#Time taken: 
#for line in f:

#line = "Time taken: 763 ms , rank 1"
#line2 = "Time taken: 1 seconds 200 ms , rank 3"
##if line[0:10] = "Time taken:":
#line = line.replace("Time taken: ","")
#line = line.replace(" ms , rank " ,"")
#line = line[:-1]
#print line

#if line2.find("seconds"):
        #line2 = line2.replace("Time taken: ","")
        #line2 = line2.replace(" ms , rank " ,"")
        #miliseconds = line2[:-1].replace(" seconds ", "")
        #print miliseconds
        
