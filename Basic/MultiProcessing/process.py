# encoding: utf-8
'''
@author: YH
@time: 2019/7/30 16:08
'''
# import multiprocessing as mp
# import threading as td
#
# def job(q):
#     # print('QQQ')
#     res = 0
#     for i in range(1000):
#         res += i + i**2 + i**3
#     q.put(res)#queue
#
# def main():
#     # t1 = td.Thread(target=job,args=(1,2))
#     # t1.start()
#     # t1.join()
#     q = mp.Queue()
#     p1 = mp.Process(target=job,args=(q,))
#     p2 = mp.Process(target=job,args=(q,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     res1 = q.get()
#     res2 = q.get()
#     print(res1 + res2)
#
# if __name__ == '__main__':
#     main()

# import multiprocessing as mp
# import threading as td
# import time
#
# def job(q):
#     # print('QQQ')
#     res = 0
#     for i in range(1000000):
#         res += i + i**2 + i**3
#     q.put(res)#queue
#
# def normal():
#     # print('QQQ')
#     res = 0
#     for _ in range(2):
#         for i in range(1000000):
#             res += i + i**2 + i**3
#     print('normal:',res)
#
# def multicore():
#     q = mp.Queue()
#     p1 = mp.Process(target=job,args=(q,))
#     p2 = mp.Process(target=job,args=(q,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     res1 = q.get()
#     res2 = q.get()
#     print('multicore:',res1 + res2)
#
# def multithread():
#     q = mp.Queue()
#     t1 = td.Thread(target=job,args=(q,))
#     t2 = td.Thread(target=job,args=(q,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     res1 = q.get()
#     res2 = q.get()
#     print('multithread:',res1 + res2)
#
# if __name__ == '__main__':
#     st = time.time()
#     normal()
#     st1 = time.time()
#     print('normal time:',st1-st)
#     multithread()
#     st2 = time.time()
#     print('multithread time:',st2-st1)
#     multicore()
#     st3 = time.time()
#     print('multicore time:',st3-st2)

# import multiprocessing as mp
#
# def job(x):
#     return x*x
#
# def multicore():
#     pool = mp.Pool(processes=2)
#     res = pool.map(job,range(10))
#     print(res)
#     res = pool.apply_async(job,(2,))
#     print(res.get())
#     multi_res = [pool.apply_async(job,(i,)) for i in range(10)]
#     print([res.get() for res in multi_res])
#
# if __name__ == '__main__':
#     multicore()

# import multiprocessing as mp
#
# value = mp.Value('d',1)
# array = mp.Array('i',[1,2,3])
# print(value)
# print(array)

import multiprocessing as mp
import time

def job(v,num,l):
    l.acquire()
    for _ in range(10):
        time.sleep(0.1)
        v.value += num
        print(v.value)
    l.release()

def multicore():
    l = mp.Lock()
    v= mp.Value('i',0)
    p1 = mp.Process(target=job,args=(v,1,l))
    p2 = mp.Process(target=job,args=(v,3,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    multicore()