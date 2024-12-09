import math
import numpy as np

class task:
    def __init__(self, name, executionTime, taskPeriod, activationJitter):
        self.name = name
        self.executionTime = executionTime
        self.period = taskPeriod
        self.activationJitter = activationJitter

    
    def cal_best_response_time(self, tasks):
        response_time = self.period
        x = 0
        while x != response_time:
            x=response_time
            other_tasks = [(math.ceil((x)/task.period) -1) * task.executionTime for task in tasks]
            response_time = self.executionTime + sum(other_tasks )
                
        return response_time
    
    def cal_worst_response_time(self, tasks):
        response_time = 0
        x = 1
        while x != response_time:
            # print(response_time)
            x=response_time
            other_tasks = sum([math.ceil((x)/task.period) * task.executionTime for task in tasks])
            response_time = self.executionTime + other_tasks 
                
        return response_time
        

def cal_rm_best_response_times(tasks):
    responce_times = np.zeros(len(tasks))
    for i in range(0, len(tasks)):
        selectedTask = tasks[i]
        other_tasks = [task for task in tasks if task.period <= selectedTask.period  and task != selectedTask]
        responce_times[i] = tasks[i].cal_best_response_time(other_tasks)
        
    return responce_times

def cal_rm_worst_response_times(tasks):
    responce_times = np.zeros(len(tasks))
    for i in range(0, len(tasks)):
        selectedTask = tasks[i]
        other_tasks = [task for task in tasks if task.period <= selectedTask.period  and task != selectedTask]
        responce_times[i] = tasks[i].cal_worst_response_time(other_tasks )
        
    return responce_times


def main():
    print("Background Scheduling")
    print("Single Task Spawn")
    job_exc_time = [task("Job0", 5, 10000, 0),
                    task("Job1", 40, 10001, 0),
                    task("Job2", 240, 10003, 0)
                    ]

    for i in range(len(job_exc_time)):
        l = [
            task("T1", 2, 20, 0),
            task("T2", 10, 40, 0),
            task("T3", 20, 60, 0),
            job_exc_time[i]
        ]
            
        # print(l)
        
        print(f"Job {i} : BR: {cal_rm_best_response_times(l)[-1]}, WR: {cal_rm_worst_response_times(l)[-1]}")
    
    print("all task spawn")
    l = [
            task("T1", 2, 20, 0),
            task("T2", 10, 40, 0),
            task("T3", 20, 60, 0)
        ]

    for j in range(len(job_exc_time)):
        l.append(job_exc_time[j])
    
    best = cal_rm_best_response_times(l)
    worst = cal_rm_worst_response_times(l)
    
    for i in range(len(l)):
        print(f"Job {l[i].name} : BR: {best[i]}, WR: {worst[i]}")
    
    

if __name__ == "__main__":
    main()