# Lab2/Task5/main.py

import os
from lab2.Task5.src.MajorityElementFinder import MajorityElementFinder
from lab2.utils.IOHandler import IOHandler
from lab2.utils.consts import *
from lab2.utils.decorate import measure_time_and_memory

@measure_time_and_memory
def main():
    current_dir=os.path.dirname(os.path.abspath(__file__))
    txtf_dir=IOHandler.get_path(current_dir,TXT_DIR)
    input_path=IOHandler.get_path(txtf_dir,INPUT_FILES_DIR,'input.txt')
    output_path=IOHandler.get_path(txtf_dir,OUTPUT_FILES_DIR,'output.txt')

    lines=IOHandler.read_file(input_path)
    array=list(map(int,lines[0].split()))

    result=MajorityElementFinder.majority_element(array)
    output=str(result) if result is not None else "Нет элемента большинства"
    IOHandler.write_file(output_path,output)
    print("Обработка завершена. Результат записан в output.txt")

if __name__=='__main__':
    main()
