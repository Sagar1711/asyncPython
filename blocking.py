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
    start = time.time()
    for i in range(parallel_req):
        apiGET(i, iURL, jURL)

    print("took: {}s".format(time.time() - start))

