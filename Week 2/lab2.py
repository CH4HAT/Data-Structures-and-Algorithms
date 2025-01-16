from time import perf_counter_ns
import statistics

#1
'''
def one():
    results=[]
    for i in range(1000):
        listy=list(range(10))
        start = perf_counter_ns()
        listy.insert(0, 5)
        end = perf_counter_ns()
        duration = end-start
        results.append(duration)
    nanoseconds = statistics.mean(results)
    print(nanoseconds/1000)

one()
'''
'''
def one():
    results=[]
    for i in range(1000):
        listy=list(range(1000000))
        start = perf_counter_ns()
        listy.insert(0, 3)
        end = perf_counter_ns()
        duration = end-start
        results.append(duration)
    nanoseconds = statistics.mean(results)
    print(nanoseconds/1000)

one()
'''
#3
'''
def one():
    results=[]
    for i in range(1000):
        listy=list(range(10))
        start = perf_counter_ns()
        listy.append(7)
        end = perf_counter_ns()
        duration = end-start
        results.append(duration)
    nanoseconds = statistics.mean(results)
    print(nanoseconds/1000)

one()
'''
#4
'''
def one():
    results=[]
    for i in range(1000):
        listy=list(range(1000000))
        start = perf_counter_ns()
        listy.append(5)
        end = perf_counter_ns()
        duration = end-start
        results.append(duration)
    nanoseconds = statistics.mean(results)
    print(nanoseconds/1000)

one()
'''


#7
'''
def one():
    results=[]
    for i in range(1000):
        listy=list(range(10))
        start = perf_counter_ns()
        listy.pop(0)
        end = perf_counter_ns()
        duration = end-start
        results.append(duration)
    nanoseconds = statistics.mean(results)
    print(nanoseconds/1000)

one()
'''
#8
'''
def one():
    results=[]
    for i in range(1000):
        listy=list(range(1000000))
        start = perf_counter_ns()
        listy.pop(0)
        end = perf_counter_ns()
        duration = end-start
        results.append(duration)
    nanoseconds = statistics.mean(results)
    print(nanoseconds/1000)

one()
'''

#10
'''
def one():
    results=[]
    for i in range(1000):
        listy=list(range(10))
        start = perf_counter_ns()
        if 5 in listy:
            end = perf_counter_ns()
        else:
            print('not')
        duration = end-start
        results.append(duration)
    nanoseconds = statistics.mean(results)
    print(nanoseconds/1000)

one()
'''
#11
'''
def one():
    results=[]
    for i in range(1000):
        listy=list(range(1000000))
        start = perf_counter_ns()
        if 5357 in listy:
            end = perf_counter_ns()
        else:
            print('not')
        duration = end-start
        results.append(duration)
    nanoseconds = statistics.mean(results)
    print(nanoseconds/1000)

one()
'''

#12
def one():
    results={}
    result=[]

    for i in range(1000):

        for num in range(10):
            results[num]=num

        start = perf_counter_ns()
        if 5 in results:
            end = perf_counter_ns()
        else:
            print('not')
        duration = end-start
        result.append(duration)
    nanoseconds = statistics.mean(results)
    print(nanoseconds/1000)

one()


