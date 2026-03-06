# Python CLI Task Manager

A command-line task management tool built in Python. Tasks are stored in a local .JSON file for persistence. 

## Usage

```bash
# Create a new task
python task.py --new -n "Meeting XX/XX" -d "Create Power Point presentation, Prepare outfit." -p 1 -s "Not Started"

# Edit an existing task
python task.py --edit -n "Prepare for date" -s "Started"

# Mark a task as complete
python task.py --complete -n "Grocery Shopping"

# Delete a task
python task.py --delete -n "Build Portfolio"

# List all tasks
python task.py --list

# View a specific task
python task.py --list -n "Generic Task"
```

## Arguments

| Arguments | Short | Help |
|------|-------|-------------|
| `--new` |`N/A`| Create a new task |
| `--edit` |`N/A`| Edit an existing task |
| `--complete` | `-c` | Mark a task as complete |
| `--delete` | `-dl` | Delete a task |
| `--list` |`N/A`| List tasks |
| `--name` | `-n` | Task name (used as identifier) |
| `--description` | `-d` | Task description |
| `--priority` | `-p` | Priority level (integer) |
| `--status` | `-s` | Task status |