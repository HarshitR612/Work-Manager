import os
import sys
import io

arg = sys.argv
params = arg[1:]

cmd = ["--help", "push", "pop", "erase", "swap", "reform"]
file = "/home/frodo612/Desktop/PythonProjects/todo/todo.txt"

JOBS = []

try :
    fp = open(file, "r");
    arg = fp.read().split("\n");
except IOError :
    #create a new file
    arg = []

for i in arg :
    if(i != '') :
        JOBS.append(i);

def pop(task) :
    try :
        arg = int(task)
        data = JOBS[arg - 1]
    except :
        data = task

    try :
        JOBS.remove(data)
    except ValueError:
        print("\"%s\" not found" % task)
        display()
        sys.exit(0)

def util() :
    n = 0
    for i in JOBS :
        n = max(n, len(i))
    return n


def display() :
    # get the console window width
    l, w = os.popen('stty size', 'r').read().split()

    col = min(util() + 9, int(w) - 1)
    if col < 25 :
        col = 25

    if col % 2 == 0 :
        col = col + 1
    top_size = int((col - 19) / 2)
    top = ""
    bottom = ""

    for i in range(top_size) :
        top += "*"
    for i in range(col) :
        bottom += "*"

    print("\n"+top+"      :TASKS TO DO:      "+top)
    
    if len(JOBS) == 0:
        print("Phew! You have no todos for now")
    else:
        for i in range(len(JOBS)):
            print(str(i + 1) + ": " + JOBS[i])
    print(bottom)
    
    
if len(params) == 0:
    # just print all todos
    display()
    sys.exit(0)

elif params[0] == cmd[0]:
    print("Prints all tasks in list if no arguments provided\n\n"
        "--help         : Print this message and exit\n"
        "push [JOB]     : Add [JOB] in TODO list\n"
        "pop [JOB]      : Remove [JOB] from TODO list\n"
        "erase          : Empty todo list\n"
        "swap [i] [j]   : swap task i and j in the list\n"
        "reform [i]     : modify description of task [i]")
    sys.exit(0)

elif params[0] == cmd[1]:
    # insert into todo list
    for i in range(1, len(params)):
        JOBS.append(params[i].strip())

elif params[0] == cmd[2]:
    # delete from todo list
    # param can be the index or the item itself
    for i in range(1, len(params)):
        delete(params[i])

elif params[0] == cmd[3]:
    #delete all tasks
    JOBS = []

elif params[0] == cmd[4]:
    l = int(params[1]) - 1
    r = int(params[2]) - 1
    JOBS[l], JOBS[r] = JOBS[r], JOBS[l]

elif params[0] == cmd[5]:
    idx = int(params[1]) - 1
    print("Write the new value of:\"",JOBS[idx],"\"")
    JOBS[idx] = input().strip()

else:
    print("Enter Valid Command")
    sys.exit(0)

fp = open(file,"w")
for i in JOBS:
    fp.write(i)
    fp.write("\n")

fp.close()

display()