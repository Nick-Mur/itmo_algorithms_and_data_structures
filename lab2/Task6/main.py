# Lab2/Task6/main.py

from lab2.Task6.src.SortPerformanceTester import SortPerformanceTester
from lab2.utils.decorate import measure_time_and_memory

@measure_time_and_memory
def main():
    SortPerformanceTester.find_threshold(max_size=1000)

if __name__=='__main__':
    main()
