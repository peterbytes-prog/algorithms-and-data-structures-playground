"""
Task. => You are given a series of incoming network packets, and your task is to simulate their processing. Packets arrive in some order. For each packet number 𝑖, you know the time when it arrived 𝐴𝑖 and the time it takes the processor to process it 𝑃𝑖 (both in milliseconds). There is only one processor, and it processes the incoming packets in the order of their arrival. If the processor started to process some packet, it doesn’t interrupt or stop until it finishes the processing of this packet, and the processing of packet 𝑖 takes exactly 𝑃𝑖 milliseconds.
The computer processing the packets has a network buffer of fixed size 𝑆. When packets ar- rive, they are stored in the buffer before being processed. However, if the buffer is full when a packet arrives (there are 𝑆 packets which have arrived before this packet, and the computer hasn’t finished processing any of them), it is dropped and won’t be processed at all. If several packets arrive at the same time, they are first all stored in the buffer (some of them may be dropped because of that — those which are described later in the input). The computer processes the packets in the order of their arrival, and it starts processing the next available packet from the buffer as soon as it finishes processing the previous one. If at some point the computer is not busy, and there are no packets in the buffer, the computer just waits for the next packet to arrive. Note that a packet leaves the buffer and frees the space in the buffer as soon as the computer finishes processing it.

Input Format. => The first line of the input contains the size 𝑆 of the buffer and the number 𝑛 of incoming network packets. Each of the next 𝑛 lines contains two numbers. 𝑖-th line contains the time of arrival 𝐴𝑖 and the processing time 𝑃𝑖 (both in milliseconds) of the 𝑖-th packet. It is guaranteed that the sequence of arrival times is non-decreasing (however, it can contain the exact same times of arrival in milliseconds — in this case the packet which is earlier in the input is considered to have arrived earlier).
Constraints. => All the numbers in the input are integers. 1 ≤ 𝑆 ≤ 105; 0 ≤ 𝑛 ≤ 105; 0 ≤ 𝐴𝑖 ≤ 106; 0≤𝑃𝑖 ≤103;𝐴𝑖 ≤𝐴𝑖+1 for1≤𝑖≤𝑛−1.
Output Format. => For each packet output either the moment of time (in milliseconds) when the processor began processing it or −1 if the packet was dropped (output the answers for the packets in the same order as the packets are given in the input).

Runing Time => O(n)
"""

# python3

from collections import namedtuple, deque
import sys

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])
Finished = namedtuple("Finished", ["starts", "ends"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque([])

    def process(self, request):
        #_copy_finished
        # copy_finished = deque([])
        # for each finished_time in finish_time
        while len(self.finish_time):
            # deque an if it finished time is greater or equal request time
            finished_time = self.finish_time[0]
            if finished_time.ends<=request.arrived_at:
                finished_time = self.finish_time.popleft()
            else:
                break
        if (len(self.finish_time)<self.size):

            if(len(self.finish_time)<=0): #if no package in buffer it will be process right away on it arrival
                finished_time = Finished(0,0)
            else:
                finished_time = self.finish_time[-1]
            starting = max((finished_time.ends,request.arrived_at))
            self.finish_time.append(Finished(starting,starting+request.time_to_process))
            return Response(False, starting)
        return Response(False, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        # print(response.started_at if not response.was_dropped else -1)
        yield (response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    for i in main():
        print(i)
