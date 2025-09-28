Tasklist =[]
Dbname ="Todo.db"
SqlTableCreate ="CREATE TABLE IF NOT EXISTS Tasks(id INTEGER PRIMARY KEY AUTOINCREMENT,task Text,completed INTEGER)"
SqlGetAll ="SELECT * FROM Tasks"
SqlCompleteOne ="UPDATE Tasks SET completed = 1 WHERE id = ?"
SqlDeleteOne ="DELETE FROM Tasks WHERE id =?"
tasklists ="""\n-----------Todo App-----------\n
Todo App optionid ( selectable Options:1,2,3,4,5)\n
1:List Menu \n
2: List Todos\n
3:Add Todo\n
4:Complete Todo\n
5: Delete A Todo
"""
SqlGetOne ="SELECT * FROM Tasks WHERE id =?"
SqlAddOne ="INSERT INTO Tasks(task,completed) VALUES (?,?)"
