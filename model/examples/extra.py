from testcases import *


r1 = Resource("r1")
r2 = Resource("r2")
r3 = Resource("r3")
r4 = Resource("r4")
tasks = {
    0: [Task(0, 10, 70, resources=[[r1, 0], [r2, 4], [None, 7]], periodical=False),
        Task(0, 7, 50, resources=[[r1, 0], [r3, 6], [None, 8]], periodical=False)],
    5: [Task(5, 7, 20, resources=[[r3, 0], [None, 3]], periodical=False),
        Task(5, 3, 14, resources=[[r1, 0]], periodical=False)],
    10: [Task(10, 8, 60, resources=[[None, 0]], periodical=False),
         Task(10, 3, 25, resources=[[r4, 0]], periodical=False)],
    15: [Task(15, 10, 70, resources=[[r4, 0], [r3, 5]], periodical=False),
         Task(15, 5, 55, resources=[[r3, 0], [None, 4]], periodical=False)],
}
scheduler = Scheduler(switch_time=2, resource_touch_time=4, cpus=2)
goal = 8

WCET_extra_time(tasks, scheduler, goal)
