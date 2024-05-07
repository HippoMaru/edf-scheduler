from scheduler import *
from resource import *


def WCET_switch():
    # r1 = Resource("r1")
    tasks = {
        0: Task(0, 10, 1000, periodical=False),
        2: Task(2, 10, 990, periodical=False),
        4: Task(4, 10, 980, periodical=False),
        6: Task(6, 10, 970, periodical=False),
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
    tasks = {
        0: [Task(0, 2, 4, periodical=False), Task(0, 2, 2)],
        1: [Task(1, 2, 8, periodical=False), Task(1, 3, 6, periodical=False)],
        5: [Task(5, 2, 7, periodical=False)]
    }
    scheduler = Scheduler(switch_time=0, cpus=3)
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


# main()
# WCET_based()
WCET_switch()
