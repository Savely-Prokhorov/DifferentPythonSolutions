# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def left_child(i):
    return 2*i+1

def right_child(i):
    return 2*i+2

def sift_down(h, i):
    min_ind = i
    left = left_child(i)
    right = right_child(i)

    if left < len(h) and right < len(h) and h[left].started_at == h[right].started_at:
        min_ind = left
        if h[left].worker > h[right].worker:
            min_ind = right
    else:
        if right < len(h) and h[right].started_at < h[min_ind].started_at:
            min_ind = right
        if left < len(h) and h[left].started_at <= h[min_ind].started_at:
            min_ind = left

    if i != min_ind:
        h[i], h[min_ind] = h[min_ind], h[i]
        sift_down(h, min_ind)
    return 0

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    heap = [AssignedJob(i,0) for i in range(n_workers)]

    for job in jobs:
        result.append(heap[0])
        heap[0] = AssignedJob(heap[0].worker, heap[0].started_at + job)
        sift_down(heap, 0)
        """for i in range(n_workers):
            # если в текущем корне минимум
            left, right = left_child(i), right_child(i)
            to_swap = left
            if i <= n_workers // 2 - 1 and heap[i].started_at <= heap[left].started_at:
                # выбираем worker'a с наим номером
                if i <= n_workers // 2 - 2 and heap[i].started_at <= heap[right].started_at:
                    if heap[left].worker > heap[right].worker:
                        to_swap=right

                result.append(AssignedJob(heap[i].worker, heap[i].started_at))
                heap[i] = AssignedJob(heap[i].worker, heap[i].started_at+job)
                break
            else:
                if i <= n_workers // 2 - 1 and heap[i].started_at > heap[left_child(i)].started_at:
                    heap[i], heap[left_child(i)] = heap[left_child(i)], heap[i]
                    result.append(heap[i])
                    heap[i] = AssignedJob(heap[i].worker, heap[i].started_at + job)
                    break
                else:
                    if i <= n_workers // 2 - 2 and heap[i].started_at > heap[right_child(i)].started_at:
                        heap[i], heap[right_child(i)] = heap[right_child(i)], heap[i]
                        result.append(heap[i])
                        heap[i] = AssignedJob(heap[i].worker, heap[i].started_at + job)
                        break"""


    """next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job"""

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
