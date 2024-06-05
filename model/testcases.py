from scheduler import *
from resource import *


def WCET_resource_touch(tasks, scheduler, goal):
    while scheduler.tasks_done < goal:
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


def WCET_switch(tasks, scheduler, goal):
    while scheduler.tasks_done < goal:
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


def WCET_all_time(tasks, scheduler, goal):
    while scheduler.tasks_done < goal:
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


def WCET_extra_time(tasks, scheduler, goal):
    while scheduler.tasks_done < goal:
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
