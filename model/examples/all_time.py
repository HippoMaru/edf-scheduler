from testcases import *


r1 = Resource("r1")
r2 = Resource("r2")
r3 = Resource("r3")
tasks = {
    0: [Task(0, 2, 4, resources=[[r1, 0]], periodical=False), Task(0, 2, 2, resources=[[r2, 0]])],
    1: [Task(1, 2, 8, resources=[[r3, 0]], periodical=False), Task(1, 3, 6, periodical=False)],
    5: [Task(5, 2, 7, periodical=False)]
}
scheduler = Scheduler(switch_time=0, cpus=2)
goal = 7

WCET_all_time(tasks, scheduler, goal)
