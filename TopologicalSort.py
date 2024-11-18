class Task:
    def __init__(self, task_name, start_time, end_time):
        self.task_name = task_name
        self.start_time = start_time
        self.end_time = end_time

def sort_by_finish_time(taskA, taskB):
    return taskB.end_time - taskA.end_time

tasks = [
    Task("watch", 9, 10),
    Task("shirt", 1, 8),
    Task("tie", 2, 5),
    Task("jacket", 3, 4),
    Task("belt", 6, 7),
    Task("pants", 12, 15),
    Task("undershorts", 11, 16),
    Task("socks", 17, 18),
    Task("shoes", 13, 14)
]

tasks.sort(key=lambda task: task.end_time, reverse=True)

print("Topological Sort:")
for task in tasks:
    print(task.task_name)
