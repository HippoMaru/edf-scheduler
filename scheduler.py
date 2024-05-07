from task import *
from task_list import *


class Scheduler:
    def __init__(self, task_list=TaskList(), switch_time=0, resource_touch_time=0, cpus=1):
        self.switch_time = switch_time
        self.tasks_done = 0
        self.total_switch_time = 0
        self.resource_touch_time = resource_touch_time
        self.current_time = 0
        self.task_list = task_list
        self.cpus = cpus
        self.cpus_ready_time = [switch_time] * cpus
        self.current_tasks = [None] * cpus
        cur = task_list.head
        self.current_resources = [None] * cpus
        i = 0
        while not self.current_tasks[-1]:
            if not cur:
                break
            if not cur.task.get_needed_resource() or cur.task.get_needed_resource() in self.current_resources:
                cur = cur.next
                continue
            self.current_tasks[i] = cur.task
            self.current_resources[i] = cur.task.get_needed_resource()
            self.current_resources[i].ready_time = resource_touch_time
            i += 1
            cur = cur.next

    def add_task(self, task: Task):
        self.task_list.insert_task(task)

    def make_step(self):
        top_tasks = []
        top_resources = []
        cur = self.task_list.head
        while len(top_tasks) < self.cpus:
            if not cur:
                break
            if cur.task.get_needed_resource() and cur.task.get_needed_resource() in top_resources:
                cur = cur.next
                continue
            top_tasks.append(cur.task)
            top_resources.append(cur.task.get_needed_resource())
            cur = cur.next
        print(top_tasks)
        for i in range(self.cpus):
            current_cpu_task = self.current_tasks[i]
            if not current_cpu_task or current_cpu_task not in top_tasks:
                for top_task in top_tasks:
                    if top_task not in self.current_tasks:
                        current_cpu_task = top_task
                        self.current_tasks[i] = top_task
                        self.cpus_ready_time[i] = self.switch_time
                        current_cpu_resource = current_cpu_task.get_needed_resource()
                        self.current_resources[i] = current_cpu_resource
                        break
                if not current_cpu_task:
                    continue
            if self.cpus_ready_time[i] != 0:
                self.total_switch_time += 1
                self.cpus_ready_time[i] -= 1
            else:
                if self.current_resources[i] and self.current_resources[i].task != current_cpu_task:
                    self.current_resources[i].ready_time = self.resource_touch_time
                    self.current_resources[i].task = current_cpu_task
                if self.current_resources[i] and self.current_resources[i].ready_time != 0:
                    self.current_resources[i].ready_time -= 1
                else:
                    current_cpu_task.time_passed += 1
                    if current_cpu_task.is_done():
                        self.tasks_done += 1
                        if current_cpu_task.is_periodical():
                            self.add_task(current_cpu_task.get_next())
                        self.current_tasks[i] = None
                        print(current_cpu_task, self.task_list)
                        self.task_list.remove_task(current_cpu_task)
                        top_tasks.remove(current_cpu_task)
                        self.current_resources[i] = None
        self.current_time += 1
        return all([not task or task.deadline > self.current_time for task in self.current_tasks])
