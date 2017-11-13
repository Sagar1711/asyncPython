import threading
import markOne as mo
import time

def apiGET(id, iURL, jURL):
    print("--" * 10)
    res1 = mo.apiGetJSON(jURL)
    res2 = mo.apiGetImage(iURL, id)

    print(res1)
    print(res2)

if __name__ == "__main__":
    parallel_req = 10
    iURL = "https://dwa5x7aod66zk.cloudfront.net/assets/labtocat-be5eee0434960a8f73e54910df8e87b8a5a3b2d651c0b301670c04a9cc26a70f.png"
    jURL = "https://api.github.com"
    t = []
    for i in range(parallel_req):
        th = threading.Thread(target=apiGET, args=(i, iURL, jURL))
        t.append(th)
    start = time.time()
    for k in range(len(t)):
        t[k].start()
        print(str(k) + " Started")
    
    for l in range(len(t)):
        t[l].join()
        print(str(l) + " finished")

    print("took: {}s".format(time.time() - start))
