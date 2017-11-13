import threading
import markOne as mo
import time

def apiGET(id, iURL, jURL, parent=None):
    print("--" * 10)
    # res1 = mo.apiGetJSON(jURL)
    # res2 = mo.apiGetImage(iURL, id)
    time.sleep(12-id)
    parent and parent.callbackfunc(id)
    # print(res1)
    # print(res2)

class parent():

    def __init__(self, threads=None):
        self.threads = []

    def starProcess(self):
        parallel_req = 10
        iURL = "https://dwa5x7aod66zk.cloudfront.net/assets/labtocat-be5eee0434960a8f73e54910df8e87b8a5a3b2d651c0b301670c04a9cc26a70f.png"
        jURL = "https://api.github.com"
        for i in range(parallel_req):
            th = threading.Thread(target=apiGET, args=(i, iURL, jURL, self))
            self.threads.append(th)
        start = time.time()
        for k in range(len(self.threads)):
            self.threads[k].start()
            print(str(k) + " Started")
        
        for l in range(len(self.threads)):
            self.threads[l].join()
            # print(str(l) + " finished")

        print("took: {}s".format(time.time() - start))
    
    def callbackfunc(self, data):
        # self.threads[data].join()
        print(str(data) + " finished")

obj = parent()
obj.starProcess()