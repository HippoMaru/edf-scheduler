from scheduler import *


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


main()
