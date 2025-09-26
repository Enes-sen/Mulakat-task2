import _sqlite3 as _sql
import argparse
from Consts import *

arpars = argparse.ArgumentParser(description="Todo App")
subparsing = arpars.add_subparsers(dest="command",help="Komutlar")

Optionparser = subparsing.add_parser("optionid",help="Select Option(1-5)")
Optionparser.add_argument("taskid",type=int,help="select(1-5)options")

args = arpars.parse_args()

def Intreducer():
    con = _sql.connect("Todo.db")
    cur = con.cursor()
    cur.execute(SqlTableCreate)
    con.commit()
    con.close()

def GetAllTasks():
    Intreducer()
    con = _sql.connect("Todo.db")
    cur = con.cursor()
    data =  cur.execute(SqlGetAll).fetchall()
    Tasklist = data
    con.commit()
    con.close()
    if len(tasklists) != 0:
        for task in Tasklist:
            state = "x" if task[2] == 0 else "✓"
            print(f"id:{task[0]},Task:{task[1]},status:{state}")
    else:
        print("you Has no Tasks Added!")

def AddTask(task):
    Intreducer()
    con = _sql.connect("Todo.db")
    cur = con.cursor()
    cur.execute(SqlAddOne,(task,0))
    con.commit()
    con.close()
    print("Task Added")

def DeleteOne(id):
    Intreducer()
    con = _sql.connect("Todo.db")
    cur = con.cursor()
    data = cur.execute(SqlGetOne,(id,)).fetchone()
    if data != None:
        cur.execute(SqlDeleteOne,(id,))
        con.commit()
        con.close()
        print(f"Task with id:{id} was deleted!")
    else:
        print(f"There is no such task with This id:{id}")
    

def UpdateStatus(id):
    Intreducer()
    con = _sql.connect("Todo.db")
    cur = con.cursor()
    data = cur.execute(SqlGetOne,(id,)).fetchone()
    if data != None:
        cur.execute(SqlCompleteOne,(id,))
        con.commit()
        con.close()
        print(f"Task with id:{id} is completed!")
    else:
        print(f"There is no such task with this id:{id},to complete!")
    
def GetOne(id):
    con = _sql.connect("Todo.db")
    cur = con.cursor()
    task = cur.execute(SqlGetOne,(id,)).fetchone()
    if(task):
        print(f"id:{task[0]},task:{task[1]},completed:","X" if task[2] == 0 else "✓")
    else:
        print(f"there is no such task with this id:{id}")
        
if args.taskid == 1:
    print(tasklists)
elif args.taskid == 2:
     GetAllTasks()
elif args.taskid == 3:
    task = input("task:")
    AddTask(task=task)
elif args.taskid == 4:
    id = int(input("Task To Finished id:"))
    UpdateStatus(id)
elif args.taskid == 5:
    id = int(input("Task To delete id:"))
    DeleteOne(id)
else:
    print(f"this option does not exists or invalid")