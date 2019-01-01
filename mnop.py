#!/usr/bin/python
globvar = 1;
f = open("pass.txt","w+")
def passis():
    print "starting"
    for i in range(0,1001):
        f.write("mnop%d+%d@@\r\n"%(globvar,i))
        if i == 1000:
            def set_glob():
                global globvar
                globvar += 1
            set_glob()    
            print "|+| Go TO %d"%(globvar)
            passis()
        if globvar == 1000:
            f.close()
            print "|+| Finish"
    
passis();
