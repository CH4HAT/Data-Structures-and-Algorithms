from time import perf_counter_ns
import statistics, os

#1

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
    return nanoseconds/1000

#2

def two():
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
    return nanoseconds/1000


#3

def three():
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
    return nanoseconds/1000


#4

def four():
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
    return nanoseconds/1000



#5

def five():
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
    return nanoseconds/1000




#6

def six():
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
    return nanoseconds/1000




#7

def seven():
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
    return nanoseconds/1000



#8

def eight():
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
    return nanoseconds/1000

#9
def nine():
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
    return nanoseconds/1000



#10

def ten():
    results=[]
    for i in range(1000):
        listy=list(range(1000000))
        start = perf_counter_ns()
        if 5 in listy:
            end = perf_counter_ns()
        else:
            print('not')
        duration = end-start
        results.append(duration)
    nanoseconds = statistics.mean(results)
    print(nanoseconds/1000)
    return nanoseconds/1000



#11

def eleven():
    results=[]
    for i in range(1000):
        listy=list(range(10))
        start = perf_counter_ns()
        if 5357 not in listy:
            pass
        end = perf_counter_ns()
        duration = end-start
        results.append(duration)
    nanoseconds = statistics.mean(results)
    print(nanoseconds/1000)
    return nanoseconds/1000




#12

def tweleve():
    results=[]
    for i in range(1000):
        listy=list(range(1000000))
        start = perf_counter_ns()
        if 5357 not in listy:
            pass
        end = perf_counter_ns()
        duration = end-start
        results.append(duration)
    nanoseconds = statistics.mean(results)
    print(nanoseconds/1000)
    return nanoseconds/1000





#13

def thirteen():
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
    return nanoseconds/1000




#14

def fourteen():
    results={}
    result=[]

    for i in range(1000):

        for num in range(1000000):
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
    return nanoseconds/1000



#15

def fifteen():
    results={}
    result=[]

    for i in range(1000):

        for num in range(10):
            results[num]=num

        start = perf_counter_ns()
        if 5742 not in results:
            end = perf_counter_ns()
        else:
            print('it has')
        duration = end-start
        result.append(duration)
    nanoseconds = statistics.mean(results)
    print(nanoseconds/1000)
    return nanoseconds/1000



#16

def sixteen():
    results={}
    result=[]

    for i in range(1000):

        for num in range(1000000):
            results[num]=num

        start = perf_counter_ns()
        if 56438 not in results:
            pass
        end = perf_counter_ns()
        duration = end-start
        result.append(duration)
    nanoseconds = statistics.mean(results)
    print(nanoseconds/1000)
    return nanoseconds/1000



final_list = [one(),two(),three()
,four()
,five()
,six()
,seven()
,eight()
,nine()
,ten()
,eleven()
,tweleve()
,thirteen()
,fourteen()
,fifteen()
,sixteen()]

filepath = './Week 2/time.txt'
if os.path.exists(filepath):
    with open(filepath, 'a') as fp:
        for i in final_list:
            fp.write(f"{i}\n")
        
else:
    with open(filepath,'w') as fp:
        for i in final_list:
            fp.write(f"{i} \n")
        
        
