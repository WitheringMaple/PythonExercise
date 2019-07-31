# encoding: utf-8
'''
@author: YH
@time: 2019/7/30 14:20
'''

# import threading
# import time
# def thread_job():
#     # print('This is an added Thread, number is %s' % threading.current_thread())
#     print('T1 start\n')
#     for i in range(10):
#         time.sleep(0.1)
#     print('T1 finish\n')
#
# def T2_job():
#     print('T2 start\n')
#     print('T2 finish\n')
#
# def main():
#
#     added_thread = threading.Thread(target=thread_job(), name = 'T1' )
#     thread2 = threading.Thread(target=T2_job,name='T2')
#     added_thread.start()
#     thread2.start()
#     added_thread.join()
#     thread2.join()
#     print(threading.active_count())
#     print(threading.enumerate())
#     print(threading.current_thread())
#     print('all done\n')
#
# if __name__ == '__main__':
#     main()

# import threading
# import time
# from queue import Queue
#
# def job(l,q):
#     for i in range(len(l)):
#         l[i] = l[i]**2
#     q.put(l)
#
# def multithreading():
#     q = Queue()
#     threads = []
#     data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
#     for i in range(4):
#         t = threading.Thread(target=job,args=(data[i],q))
#         t.start()
#         threads.append(t)
#     for thread in threads:
#         thread.join()
#     results = []
#     for _ in range(4):
#        results.append(q.get())
#     print(results)
# if __name__ == '__main__':
#     multithreading()

# import threading
# from queue import Queue
# import copy
# import time
#
# def job(l, q):
#     res = sum(l)
#     q.put(res)
#
# def multithreading(l):
#     q = Queue()
#     threads = []
#     for i in range(4):
#         t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
#         t.start()
#         threads.append(t)
#     [t.join() for t in threads]
#     total = 0
#     for _ in range(4):
#         total += q.get()
#     print(total)
#
# def normal(l):
#     total = sum(l)
#     print(total)
#
# if __name__ == '__main__':
#     l = list(range(1000000))
#     s_t = time.time()
#     normal(l*4)
#     print('normal: ',time.time()-s_t)
#     s_t = time.time()
#     multithreading(l)
#     print('multithreading: ', time.time()-s_t)

import threading
import time
def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A += 1
        time.sleep(0.1)
        print('job1', A)
    lock.release()

def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A += 10
        time.sleep(0.1)
        print('job2', A)
    lock.release()

if __name__ == '__main__':
    A = 0
    lock = threading.Lock()
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()