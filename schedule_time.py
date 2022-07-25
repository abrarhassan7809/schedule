import timesched
from datetime import datetime, time

from scheduler.trigger import Monday


def Work_day(self):
    print('Its a working day '.format(self, datetime.now()))

s = timesched.Scheduler()

s.oneshot(2, 0, Work_day, 1)

s.repeat_on_days('MTWTFss', time(13, 37), 0, Work_day, 1)

# s.repeat(2, 0, job, 2)

s.run()



# ---------------------------------
# import sched, time
#
# # Creating an instance for scheduler class
# s = sched.scheduler(time.time, time.sleep)
#
# def print_event(name):
#     print('EVENT:', time.time(), name)
#     s.enter(5, 2, print_event, (name,))
#
# print('START:', time.time())
#
# e1 = s.enter(1, 1, print_event, (' 1st', ))
#
# e2 = s.enter(2, 1, print_event, (' 2nd', ))
#
# s.run()

# ---------------------------------------
# from time import time, sleep
# from sched import scheduler
#
# def abrar(self):
#     print('its time to work')
#     self.enter(2, 1, abrar, (self,))
#
# if __name__ == '__main__':
#     time_is = scheduler(time, sleep)
#     time_is.enter(2, 1, abrar, (time_is,))
#     time_is.run()



# s = sched.scheduler(time.time, time.sleep)
# def print_time(a='default'):
#     print("From print_time", time.time(), a)
#
# def print_some_times():
#     print(time.time())
#     for i in range(60):
#         s.enter(5 * i, 1, print_time)
#         s.enter(5 * i, 2, print_time, argument=('positional',))
#         s.enter(5 * i, 1, print_time, kwargs={'a': 'keyword'})
#
#     s.run()
#
# print_some_times()

# ------------------------------
# schedule.run_pending()
# time.sleep(1)

# its_on = True
# i = 0
# while its_on:
#     if i <= 2:
#         schedule.run_pending()
#         time.sleep(1)
#     else:
#         print("its over !")
#         its_on = False
