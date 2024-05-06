class Task:
    def __init__(self, first_arr_time, time_needed, first_deadline, resources=None, periodical=True, n=1):
        if resources is None:
            resources = [[None, 0]]
        self.first_arr_time = first_arr_time
        self.time_needed = time_needed
        self.first_deadline = first_deadline
        self.deadline = first_arr_time + (first_deadline - first_arr_time) * n
        self.periodical = periodical
        self.n = n
        self.time_passed = 0
        self.resources = resources
        self.current_resource = None

    def __str__(self):
        return f'выполнено: {self.time_passed} надо: {self.time_needed} дедлайн: {self.deadline}'

    def __repr__(self):
        return self.__str__()

    def is_periodical(self):
        return self.periodical

    def is_done(self):
        return self.time_passed >= self.time_needed

    def get_next(self):
        return Task(self.first_arr_time, self.time_needed, self.first_deadline, self.periodical, self.n + 1)

    def get_needed_resource(self):
        resource = None
        for el in self.resources:
            if el[1] > self.time_passed:
                break
            resource = el[0]
        return resource
