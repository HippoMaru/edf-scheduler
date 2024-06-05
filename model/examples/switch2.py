from testcases import *


tasks = {
    40: Task(40, 100, 5000, periodical=False),
    30: Task(30, 20, 4000, periodical=False),
    20: Task(20, 30, 3000, periodical=False),
    10: Task(10, 60, 2000, periodical=False),
    0: Task(0, 70, 1000, periodical=False),
}
scheduler = Scheduler(switch_time=1, cpus=1)
goal = 5

WCET_switch(tasks, scheduler, goal)
