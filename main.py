from random import Random
import time
from queue import Queue
import os
import sys
import threading
from threading import Thread




def qsort(sets,left,right):

    print("thead {0} is sorting {1}".format(threading.current_thread(), sets[left:right]))

    i = left
    j = right
    pivot = sets[(left + right)//2]
    temp = 0
    while(i <= j):
         while(pivot > sets[i]):
             i = i+1
         while(pivot < sets[j]):
             j = j-1
         if(i <= j):
             temp = sets[i]
             sets[i] = sets[j]
             sets[j] = temp
             i = i + 1
             j = j - 1

    lthread = None
    rthread = None

    if (left < j):
        lthread = Thread(target = lambda: qsort(sets,left,j))
        lthread.start()

    if (i < right):
        rthread = Thread(target=lambda: qsort(sets,i,right))
        rthread.start()

    if lthread is not None: lthread.join()
    if rthread is not None: rthread.join()
    return sets


'''testing below'''




def Quicksort(str,p,number):

    if p<number:
        q = Partition(str,p,number)
        Quicksort(str,p,q-1)
        Quicksort(str,q+1,number)


def Partition(str,p,number):

    x = str[number]
    a = p-1
   # j = p
    for j in range(p,number):
        if (str[j]<=x):
                a = a+1
                str[a],str[j] = str[j],str[a]
        #j=j+1
    str[a+1],str[number] = str[number],str[a+1]
    return a+1


def Max_Heapify(str,k,heap_size):
    largest = 0

    le = 2*k+1
    rt = 2*k+2


    if(le < heap_size and str[le] > str[k]):
        largest = le
    else:
        largest = k
    if(rt < heap_size and str[rt] > str[largest]):
        largest = rt
    if(largest != k):
        str[k], str[largest] = str[largest], str[k]
        Max_Heapify(str,largest,heap_size)




def Heapsort(str):
    heap_size = len(str)

    for i in range(len(str)//2-1,-1,-1):
        #print(i)
        Max_Heapify(str,i,heap_size)

    for j in range(len(str),0,-1):
        #print(j)
        str[0], str[j-1] = str[j-1], str[0]
        heap_size = heap_size-1
        Max_Heapify(str,0,heap_size)


'''
def Merge(str,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    L = ['' for i in range(0,n1+1)]
    R = ['' for j in range(0,n2+1)]
    for i in range(0,n1):
        L[i] = str[p+i]
    for j in range(0,n2):
        R[j] = str[q+j+1]
    L[n1] = '~'
    R[n2] = '~'
    i = 0
    j = 0
    for k in range(p,r+1):
        if(L[i] <= R[j]):
            str[k] = L[i]
            i = i + 1
        else:
            str[k] = R[j]
            j = j + 1
'''

'''
def Merge_sort(str,p,r):
    if(p<r):
        q = (p+r) // 2
        Merge_sort(str,p,q)
        Merge_sort(str,q+1,r)
        Merge(str,p,q,r)
'''

str = ''
str = list(str)

number = int(input())
str = ['' for x in range(0,number)]
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

length = len(chars)-1
random = Random()

for j in range(number):

    for i in range(6):
        str[j]+=chars[random.randint(0,length)]

#print(str)
#n = len(str)
path = 'runtime.txt'
f = open(path,'w')

start = time.time()
#Quicksort(str,0,number-1)
#Heapsort(str)
#Merge_sort(str,0,number-1)
qsort(str,0,number-1)
end = time.time()

#print(str)
print("執行時間：%f 秒" % (end - start))
print("執行時間：%f 秒" % (end - start),file=f)

