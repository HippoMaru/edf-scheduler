from testcases import *


r1 = Resource("r1")
tasks = {
    0: Task(0, 10, 1000, resources=[[r1, 0]], periodical=False),
    7: Task(7, 10, 990, resources=[[r1, 0]], periodical=False),
    13: Task(13, 10, 980, resources=[[r1, 0]], periodical=False),
    18: Task(18, 10, 970, resources=[[r1, 0]], periodical=False),
}
scheduler = Scheduler(switch_time=2, resource_touch_time=4, cpus=1)
goal = 4

WCET_resource_touch(tasks, scheduler, goal)
