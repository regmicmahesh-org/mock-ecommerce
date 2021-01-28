import logging
import time
def retry(func):

    def inner_func(*args, **kwargs):
        counter = 0
        res = 0
        while counter < 5:
            try:
                res = func(*args, **kwargs)
                return res
            except:
                counter += 1
                time.sleep(counter)
                print( "Retrying... " + str(counter))
        return res

    return inner_func
