import requests
from multiprocessing.pool import ThreadPool as Pool

dir_list = open("/usr/share/wordlists/dirb/common.txt").read().splitlines()
url = "http://10.10.10.168:8080/"

pool_size = 10
def worker(dir):
    try:
        url_to_check = url+dir+"/SuperSecureServer.py"
        resp = requests.get(url_to_check)
        if resp.status_code == 200:
            print("found path: "+url_to_check)
    except:
        pass

pool = Pool(pool_size)
for dir in dir_list:
    pool.apply_async(worker, (dir,))

pool.close()
pool.join()