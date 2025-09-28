import _sqlite3 as _sql
import argparse
from Consts import *
arpars = argparse.ArgumentParser(description="Todo App")
subparsing = arpars.add_subparsers(dest="command",help="Komutlar")

Optionparser = subparsing.add_parser("optionid",help="Select Option(1-5)")
Optionparser.add_argument("taskid",type=int,help="select(1-5)options")
args = arpars.parse_args()


def Connectdb (dbname:str):
    return _sql.connect(f"{dbname}")

Con = Connectdb(Dbname)
def Commit():
    Con.commit()
    Con.close()

def Intreducer():
    cur = Con.cursor()
    cur.execute(SqlTableCreate)
    Commit()


def GetAllTasks():
    cur = Con.cursor()
    data =  cur.execute(SqlGetAll).fetchall()
    Tasklist = data
    Commit()
    if len(tasklists) != 0:
        for task in Tasklist:
            state = "x" if task[2] == 0 else "✓"
            print(f"id:{task[0]},Task:{task[1]},status:{state}")
    else:
        print("you Has no Tasks Added!")

def AddTask(task):
    cur = Con.cursor()
    cur.execute(SqlAddOne,(task,0))
    Commit()
    print("Task Added")

def DeleteOne(id:int):
    cur = Con.cursor()
    data = GetOne(id)
    if data != None:
        cur.execute(SqlDeleteOne,(id,))
        Commit()
        print(f"Task with id:{id} was deleted!")
    else:
        print(f"There is no such task with This id:{id}")
    

def UpdateStatus(id:int):
    cur = Con.cursor()
    data = GetOne(id)
    if data != None:
        cur.execute(SqlCompleteOne,(id,))
        Commit()
        print(f"Task with id:{id} is completed!")
    else:
        print(f"There is no such task with this id:{id},to complete!")
    
def GetOne(id:int):
    cur = Con.cursor()
    print(type(cur))
    task = cur.execute(SqlGetOne,(id,)).fetchone()
    if(task):
        return task
    else:
        print(f"there is no such task with this id:{id}")
        return None
        
argt = args._get_kwargs()

if argt[0][1] == "optionid"  and args.taskid == 1:
    print(tasklists)
elif argt[0][1] == "optionid"  and args.taskid == 2:
    GetAllTasks()
elif argt[0][1] == "optionid"  and args.taskid == 3:
    task = input("task:")
    AddTask(task=task)
elif argt[0][1] == "optionid"  and args.taskid == 4:
    id = int(input("Task To Finished id:"))
    UpdateStatus(id)
elif argt[0][1] == "optionid"  and args.taskid == 5:
    id = int(input("Task To delete id:"))
    DeleteOne(id)
else:
    print("this option does not exists or invalid")
