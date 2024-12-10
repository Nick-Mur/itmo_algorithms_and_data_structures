# Lab2/Task4/main.py

import os
from lab2.Task4.src.BinarySearcher import BinarySearcher
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
    target=int(lines[1].strip()) if len(lines)>1 else None

    result=BinarySearcher.binary_search(array,target)

    IOHandler.write_file(output_path,str(result))
    print("Обработка завершена. Результат записан в output.txt")

if __name__=='__main__':
    main()
