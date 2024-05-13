from scheduler import *
from resource import *


def WCET_resource_touch():
    r1 = Resource("r1")
    tasks = {
        0: Task(0, 10, 1000, resources=[[r1, 0]], periodical=False),
        7: Task(7, 10, 990, resources=[[r1, 0]], periodical=False),
        13: Task(13, 10, 980, resources=[[r1, 0]], periodical=False),
        18: Task(18, 10, 970, resources=[[r1, 0]], periodical=False),
    }
    scheduler = Scheduler(switch_time=2, resource_touch_time=4, cpus=1)
    while scheduler.tasks_done < 4:
        if scheduler.current_time in tasks.keys():
            task = tasks[scheduler.current_time]
            scheduler.add_task(task)
        print("CURRENT TIME:", scheduler.current_time)
        print("CURRENT TASKS:", scheduler.current_tasks)
        print("TASK LIST:", scheduler.task_list)
        print()
        success = scheduler.make_step()
        if success:
            print("STEPPED SUCCESSFULLY\n")
        else:
            print("ERROR\n")
            break
    print("WORK IS DONE")
    print("CURRENT TIME:", scheduler.current_time)
    print("CURRENT TASKS:", scheduler.current_tasks)
    print("TASK LIST:", scheduler.task_list)
    print("TOTAL RESOURCE TOUCH TIME:", scheduler.total_resource_touch_time)



def WCET_switch():
    # r1 = Resource("r1")
    tasks = {
        0: Task(0, 10, 1000, periodical=False),
        4: Task(4, 10, 990, periodical=False),
        7: Task(7, 10, 980, periodical=False),
        9: Task(9, 10, 970, periodical=False),
    }
    scheduler = Scheduler(switch_time=3, cpus=1)
    while scheduler.tasks_done < 4:
        if scheduler.current_time in tasks.keys():
            task = tasks[scheduler.current_time]
            scheduler.add_task(task)
        print("CURRENT TIME:", scheduler.current_time)
        print("CURRENT TASKS:", scheduler.current_tasks)
        print("TASK LIST:", scheduler.task_list)
        print()
        success = scheduler.make_step()
        if success:
            print("STEPPED SUCCESSFULLY\n")
        else:
            print("ERROR\n")
            break
    print("WORK IS DONE")
    print("CURRENT TIME:", scheduler.current_time)
    print("CURRENT TASKS:", scheduler.current_tasks)
    print("TASK LIST:", scheduler.task_list)
    print("TOTAL SWITCH TIME:", scheduler.total_switch_time)


def WCET_based():
    r1 = Resource("r1")
    r2 = Resource("r2")
    r3 = Resource("r3")
    tasks = {
        0: [Task(0, 2, 4, resources=[[r1, 0]], periodical=False), Task(0, 2, 2, resources=[[r2, 0]])],
        1: [Task(1, 2, 8, resources=[[r3, 0]], periodical=False), Task(1, 3, 6, periodical=False)],
        5: [Task(5, 2, 7, periodical=False)]
    }
    scheduler = Scheduler(switch_time=0, cpus=2)
    while scheduler.tasks_done < 7:
        if scheduler.current_time in tasks.keys():
            for task in tasks[scheduler.current_time]:
                scheduler.add_task(task)
        print("CURRENT TIME:", scheduler.current_time)
        print("CURRENT TASKS:", scheduler.current_tasks)
        print("TASK LIST:", scheduler.task_list)
        print()
        success = scheduler.make_step()
        if success:
            print("STEPPED SUCCESSFULLY\n")
        else:
            print("ERROR\n")
            break
    print("WORK IS DONE")
    print("CURRENT TIME:", scheduler.current_time)
    print("CURRENT TASKS:", scheduler.current_tasks)
    print("TASK LIST:", scheduler.task_list)


def main():
    scheduler = Scheduler(switch_time=2, cpus=3)
    task1 = Task(scheduler.current_time, 2, 4)
    task2 = Task(scheduler.current_time, 2, 4)
    task3 = Task(scheduler.current_time, 2, 4)
    scheduler.add_task(task1)
    scheduler.add_task(task2)
    scheduler.add_task(task3)
    for _ in range(50):
        print("CURRENT TIME:", scheduler.current_time)
        print("CURRENT TASKS:", scheduler.current_tasks)
        print("TASK LIST:", scheduler.task_list)
        print()
        success = scheduler.make_step()
        if success:
            print("STEPPED SUCCESSFULLY\n")
        else:
            print("ERROR\n")
            break
    print("WORK IS DONE")
    print("CURRENT TIME:", scheduler.current_time)
    print("CURRENT TASKS:", scheduler.current_tasks)
    print("TASK LIST:", scheduler.task_list)


def WCET_final():
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
    while scheduler.tasks_done < 8:
        if scheduler.current_time in tasks.keys():
            for task in tasks[scheduler.current_time]:
                scheduler.add_task(task)
        print("CURRENT TIME:", scheduler.current_time)
        print("CURRENT TASKS:", scheduler.current_tasks)
        print("TASK LIST:", scheduler.task_list)
        print()
        success = scheduler.make_step()
        if success:
            print("STEPPED SUCCESSFULLY\n")
        else:
            print("ERROR\n")
            break
    print("WORK IS DONE")
    print("CURRENT TIME:", scheduler.current_time)
    print("CURRENT TASKS:", scheduler.current_tasks)
    print("TASK LIST:", scheduler.task_list)
    print("AVG EXTRA TIME:", sum(scheduler.extra_times)/len(scheduler.extra_times))


def WCET_switch1():
    # r1 = Resource("r1")
    tasks = {
        40: Task(40, 100, 5000, periodical=False),
        30: Task(30, 20, 4000, periodical=False),
        20: Task(20, 30, 3000, periodical=False),
        10: Task(10, 60, 2000, periodical=False),
        0: Task(0, 70, 1000, periodical=False),
    }
    scheduler = Scheduler(switch_time=1, cpus=1)
    while scheduler.tasks_done < 5:
        if scheduler.current_time in tasks.keys():
            task = tasks[scheduler.current_time]
            scheduler.add_task(task)
        print("CURRENT TIME:", scheduler.current_time)
        print("CURRENT TASKS:", scheduler.current_tasks)
        print("TASK LIST:", scheduler.task_list)
        print()
        success = scheduler.make_step()
        if success:
            print("STEPPED SUCCESSFULLY\n")
        else:
            print("ERROR\n")
            break
    print("WORK IS DONE")
    print("CURRENT TIME:", scheduler.current_time)
    print("CURRENT TASKS:", scheduler.current_tasks)
    print("TASK LIST:", scheduler.task_list)
    print("TOTAL SWITCH TIME:", scheduler.total_switch_time)
# main()
# WCET_based()
# WCET_switch()
# WCET_resource_touch()
# WCET_final()
WCET_switch1()