# Lab2/Task3/main.py

import os
from lab2.Task3.src.InversionsCounter import InversionsCounter
from lab2.utils.IOHandler import IOHandler
from lab2.utils.consts import *
from lab2.utils.decorate import measure_time_and_memory

@measure_time_and_memory
def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir=IOHandler.get_path(current_dir,TXT_DIR)
    input_path=IOHandler.get_path(txtf_dir,INPUT_FILES_DIR,'input.txt')
    output_path=IOHandler.get_path(txtf_dir,OUTPUT_FILES_DIR,'output.txt')

    lines=IOHandler.read_file(input_path)
    array=list(map(int,lines[0].split()))
    temp_array=[0]*len(array)

    inv_count=InversionsCounter.merge_sort_and_count(array,temp_array,0,len(array)-1)

    IOHandler.write_file(output_path,str(inv_count))
    print("Обработка завершена. Результат записан в output.txt")

if __name__=='__main__':
    main()
