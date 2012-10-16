import subprocess
import os
import StringIO
import time


def change_number_of_cities(newNum):
	try:
		f = open("route.dat", "r+")
		
		content = f.readlines()
		
		f.seek(0)
		
		f.write(str(newNum)+"\n")
		
		content.pop(0)
		
		for line in content:
        	
        		f.write(str(line))
		
		f.close()
	except:
		print "Error while trying to change number of cities"

MIN_NUM_CITIES = 10
MAX_NUM_CITIES = 11

MIN_NUM_WORKERS = 1
MAX_NUM_WORKERS = 8

NUM_RUNS = 5

FILE_NAMES = ["RaceTrap", "working"]

f = open("results.txt", "w+")

f.write("FILENAME, NUM_CITIES, NUM_WORKERS, RUNTIME\n")

# Running different versions
for file in FILE_NAMES:
	
	
	
	
	# Running different number of cities
	for curr_num_cities in range(MIN_NUM_CITIES, MAX_NUM_CITIES+1):
		
		change_number_of_cities(curr_num_cities)
		
		# Running different number of workers
		for curr_num_workers in range(MIN_NUM_WORKERS, MAX_NUM_WORKERS):

		
		
			
			avg = []
			
			print "Filename", file, "\tCities: ", curr_num_cities, "\tWorkers ", curr_num_workers
			for run in range(NUM_RUNS):
				
				
				output = os.popen("./" + file + " -cilk_set_worker_count=" + str(curr_num_workers)).read()
				output = StringIO.StringIO(output)
				
				x =  output.readline().split(" ")
				#print x
				
				sumRunning = 0
				
				for count in range(0, len(x)):
					if x[count] == "min.":
						
						sumRunning += int(x[count - 1]) * 60000
			
					if x[count] == "seconds":
						sumRunning += int(x[count -1])*1000
			
					if x[count] == "ms":
						ms =  int(x[count-1])
						sumRunning += ms   
						
				avg.append(sumRunning)		
				print "RUNTIME", sumRunning
			
			avg_runtime = sum(avg) / len(avg)
			print "AVG: ", avg_runtime
			results = "%s, %d, %d, %d \n" % (file, curr_num_cities, curr_num_workers, avg_runtime)
			f.write(results)
f.close()
		

#def make(filename):
    	#output = os.popen(('make %s' % (file_name))).read()
	
	



##a = os.popen('lamboot -v hosts.lam').read()
##p.wait()
#timelist = []
#tmplist = []

#sizes = [16, 32, 64, 128, 256, 512, 1024, 2048]
##sizes = [8192]

##files = ["dynamic", "master"]
#files = ["RoadMap"]
#runs = 1




##changeNodeCount()

#time.sleep(2)

#print "Execute test"

#f =  open("seqTest.cvs", "w+")
#columns = "nodes, filename, average, numruns, size\n"
#f.write(columns)


##while (MORE_NODES):
    ##f.write(("\n\nRUNNING ON %d NODES\n"%(len(runningNodes))))
    ##os.popen("lamboot -v hosts.lam")
#for file_name in files:
    #for size in sizes:
        #change_size(file_name, size)
        #make(file_name)
        
        #tmplist = []
        
        #for i in range (0, runs):
            ##a = os.popen(('mpirun C -ssi rpi tcp ./%s' % (file_name))).read()
            #a = os.popen(('./%s' % (file_name))).read()
            
            
            #a = StringIO.StringIO(a)
            
            #sumRunning = 0
            #for line in a.readlines():
                    ## if line.count("Time taken:") == 1:
    
                #x = line.split(" ")
                
                #for count in range(0, len(x)):
                    #if x[count] == "min.":
                        
                            #sumRunning += int(x[count - 1]) * 60000

                    #if x[count] == "seconds":
                        #sumRunning += int(x[count -1])*1000

                    #if x[count] == "ms":
                        #ms =  int(x[count-1])
                        #sumRunning += ms   

            #tmplist.append(sumRunning)    
                        
        
        #result =  "%s, %s, %d, %d, %d X %d\n" % (len(runningNodes), file_name, (sum(tmplist) / len(tmplist)), runs, size, size)
        #print result
        #f.write(result)
    ##changeNodeCount()


##output = os.popen("lamhalt").read()
#f.close



                           
                            
                                
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
        
