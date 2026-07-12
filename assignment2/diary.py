# Task 1: Diary

import traceback

init_question = "What happened today? "
question = "What else? "
stop_line = "done for now"
current_text = ""
result_text = ""

try:
    with open('diary.txt', 'a') as file:
        current_text = input(init_question)
        while current_text != stop_line:
            result_text = result_text + current_text  + "\n"
            current_text = input(question)
        file.write(result_text)
except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")

# Task 2: Read a CSV File
