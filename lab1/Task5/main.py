# Lab1/Task5/main.py

import os
from lab1.Task5.src.SelectionSorter import SelectionSorter
from lab1.utils.IOHandler import IOHandler
from lab1.utils.consts import *
from lab1.utils.decorate import measure_time_and_memory

@measure_time_and_memory
def main():
    current_dir=os.path.dirname(os.path.abspath(__file__))
    txtf_dir=IOHandler.get_path(current_dir,TXT_DIR)
    input_path=IOHandler.get_path(txtf_dir,INPUT_FILES_DIR,'input.txt')
    output_path=IOHandler.get_path(txtf_dir,OUTPUT_FILES_DIR,'output.txt')

    lines=IOHandler.read_file(input_path)
    arr=list(map(int,lines[0].split()))

    sorted_arr = SelectionSorter.selection_sort(arr)
    IOHandler.write_file(output_path,' '.join(map(str,sorted_arr)))
    print("Обработка завершена. Результат записан в output.txt")

if __name__=='__main__':
    main()
