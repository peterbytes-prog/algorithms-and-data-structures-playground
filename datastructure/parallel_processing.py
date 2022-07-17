"""
Task. ==>  You have a program which is parallelized and uses 𝑛 independent threads to process the given list of 𝑚 jobs. Threads take jobs in the order they are given in the input. If there is a free thread, it immediately takes the next job from the list. If a thread has started processing a job, it doesn’t interrupt or stop until it finishes processing the job. If several threads try to take jobs from the list simultaneously, the thread with smaller index takes the job. For each job you know exactly how long will it take any thread to process this job, and this time is the same for all the threads. You need to determine for each job which thread will process it and when will it start processing.

Input Format.==>   The first line of the input contains integers 𝑛 and 𝑚.
The second line contains 𝑚 integers 𝑡𝑖 — the times in seconds it takes any thread to process 𝑖-th job. The times are given in the same order as they are in the list from which threads take jobs.
Threads are indexed starting from 0.

Constraints. ==>  1≤𝑛≤105;1≤𝑚≤105;0≤𝑡𝑖 ≤109.

Output Format. ==>  Output exactly 𝑚 lines. 𝑖-th line (0-based index is used) should contain two space- separated integers — the 0-based index of the thread which will process the 𝑖-th job and the time in seconds when it will start processing that job.
"""
# python3

from collections import namedtuple, deque
from time import sleep


AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
JOB = namedtuple('JOB', "processor started")

class Worker:
    def __init__(self, addr=0, next_free_time=0):
        self.addr = addr
        self.next_free_time = next_free_time

def getParentIndex(i):
	return (i-1)//2

def getRightChildIndex(i):
	return (2 * i) + 1

def isLeaf(heap, pos):
    return pos*2 > len(heap)

def getLeftChildIndex(i):
	return 2 * i

inp = [5,4,3,2,1]

def heapViolated(heap, i):
    #heap is violated if the smallest is not on top or if they are equal and the lowest index is not on top
    if i<=0:
        return False
    r = getRightChildIndex(i)
    l = getLeftChildIndex(i)
    smallest = i
    min_ind = heap[i][0]
    if r<len(heap) and ((heap[r][1]<heap[smallest][1]) or (heap[r][1] == heap[smallest][1] and heap[r][0]<heap[smallest][0])):
        smallest = r
    if l<len(heap) and ((heap[l][1]<heap[smallest][1]) or (heap[l][1] == heap[smallest][1] and heap[l][0]<heap[smallest][0])):
        smallest = l
    if (heap[i][1]>heap[smallest][1]) or (heap[i][1] == heap[smallest][1] and heap[i][0]>heap[smallest][0]):
        return smallest
    return False

def swap(heap,x,y):
    ref = heap[x]
    heap[x] = heap[y]
    heap[y] = ref
    return heap
def shiftDown(heap, ind):
    ref = ind
    while heapViolated(heap,ind):
        x = heapViolated(heap,ind)
        heap=swap(heap,x,ind)
        ind = x
    return heap

def build_heap(heap):
    """Build a min heap from ``data`` inplace.
    """
    i = 1
    n = int((len(heap)//2))
    for i in range(n, -1, -1):
        if heapViolated(heap,i):
            heap = shiftDown(heap, i)
    return heap


def naive_assign_jobs(n, jobs):
    processors = [{"p_time_lapsed":0, "current_job_time_left":0} for i in range(n)]
    job_tracker = deque([])
    while len(jobs):
        time_lapsed = min([p["current_job_time_left"] for p in processors])
        for i in range(len(processors)):
            processors[i]["p_time_lapsed"] += time_lapsed
            processors[i]["current_job_time_left"] -= time_lapsed
            if processors[i]["current_job_time_left"] == 0 and len(jobs):
                j = jobs.popleft()
                new_job = JOB(i,processors[i]["p_time_lapsed"])
                processors[i]["current_job_time_left"] = j
                job_tracker.append(new_job)
    for job in job_tracker:
        yield job

def assign_jobs(n_workers, jobs):
    result = []
    next_free_time = [0, *[[i,0] for i in range(n_workers)]]
    while len(jobs):
        job = jobs.popleft()
        min_ind = 1
        result.append(AssignedJob(next_free_time[min_ind][0], next_free_time[min_ind][1]))
        next_free_time[min_ind][1] += job
        next_free_time = shiftDown(next_free_time, 1)
    return result

def main():#n_workers, jobs
    n_workers, n_jobs = map(int, input().split())
    jobs = deque(list(map(int,input().split())))
    assert len(jobs) == n_jobs
    assigned_jobs = assign_jobs(n_workers, jobs)
    for job in assigned_jobs:
        # print(job.processor, job.started)
        yield (job.worker, job.started_at)



if __name__ == "__main__":
    main()
