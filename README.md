# Simple Task

A lightweight command-line task management application.

---

## ✨ Features
- Add tasks  
- Delete tasks  
- Update tasks  
- List all tasks  
- Filter tasks by status (**todo**, **in-progress**, **done**)  
- Change task status (mark as in-progress or done)  

---

## 🚀 Usage

Run commands with:

```bash
python <command> <arguments>
```

### Commands

**Add a new task**
```bash
python add "<description>"
```

**Delete a task**
```bash
python delete <task_id>
```

**Update a task**
```bash
python update <task_id> "<new description>"
```

**List all tasks**
```bash
python list
```

**List tasks by status**
```bash
python list <status>
# status can be: todo | in-progress | done
```

**Mark a task as in-progress**
```bash
python mark-in-progress <task_id>
```

**Mark a task as done**
```bash
python mark-done <task_id>
```

---

## 📌 Notes
- `<task_id>` is the unique identifier assigned to each task.  
- Valid statuses are: **todo**, **in-progress**, **done**.  
