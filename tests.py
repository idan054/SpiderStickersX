from Scripts.A1_wooGetAPI import woocomarce_api
from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)
async_result = pool.apply_async(woocomarce_api, (25560,)) # tuple of args for foo

# do some other stuff in the main process

first_name, last_name, address_1, street_num, street, city, \
email, phone, high_quantity, deliveryNeeded, customer_note = async_result.get()  # get the return value from your function.
print(street_num)

