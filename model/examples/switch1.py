from testcases import *


tasks = {
    0: Task(0, 10, 1000, periodical=False),
    4: Task(4, 10, 990, periodical=False),
    7: Task(7, 10, 980, periodical=False),
    9: Task(9, 10, 970, periodical=False),
}
scheduler = Scheduler(switch_time=3, cpus=1)
goal = 4

WCET_switch(tasks, scheduler, goal)
