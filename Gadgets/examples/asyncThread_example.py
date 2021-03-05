from time import sleep

def foo(bar):
  sleep(1)
  # print('hello {0}'.format(bar))
  return 'foo'

from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)

async_result = pool.apply_async(foo, ('world',)) # tuple of args for foo

# do some other stuff in the main process

return_val = async_result.get()  # get the return value from your function.
print(return_val)

while True:
    x = async_result.get()
    print(x)

