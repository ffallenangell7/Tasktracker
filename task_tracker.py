import json
import os
from colorama import Fore, Style, init
import pyfiglet
from datetime import datetime, timedelta
import sys
import time

TASKS_FILE = "tasks.json"

init(autoreset=True)

# ----- ENHANCED TITLE WITH ANIMATION -----
def show_title():
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_banner = pyfiglet.figlet_format("Daily Task Tracker", font="slant")
    print(Fore.CYAN + Style.BRIGHT + ascii_banner)
    print(Fore.MAGENTA + "🚀 Version 2.0 | Modern & Interactive Edition!\n")

# ----- ANIMATION EFFECTS -----
def typing_effect(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def loading_animation(text="Loading", duration=2):
    animation = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    start_time = time.time()
    i = 0
    while time.time() - start_time < duration:
        print(f"\r{Fore.YELLOW}{text} {animation[i % len(animation)]}", end="", flush=True)
        time.sleep(0.1)
        i += 1
    print(f"\r{Fore.GREEN}✅ {text} complete!{' ' * 20}")

# ----- ENHANCED MENU WITH EMOJIS -----
def show_menu():
    print(f"\n{Fore.BLUE}🎯 {Style.BRIGHT}MAIN MENU")
    print(Fore.YELLOW + "┌────────────────────────────────────────┐")
    print(Fore.YELLOW + "│ 1️⃣   Add New Task                      │")
    print(Fore.YELLOW + "│ 2️⃣   View All Tasks                    │")
    print(Fore.YELLOW + "│ 3️⃣   Mark Task as Done                 │")
    print(Fore.YELLOW + "│ 4️⃣   Search Tasks                      │")
    print(Fore.YELLOW + "│ 5️⃣   Edit Task                         │")
    print(Fore.YELLOW + "│ 6️⃣   Delete Task                       │")
    print(Fore.YELLOW + "│ 7️⃣   Task Statistics                   │")
    print(Fore.YELLOW + "│ 8️⃣   Save Tasks                        │")
    print(Fore.YELLOW + "│ 9️⃣   Load Tasks                        │")
    print(Fore.RED    + "│ 0️⃣   Exit                             │")
    print(Fore.YELLOW + "└────────────────────────────────────────┘")

# ----- ENHANCED TASK FUNCTIONS -----
def add_task(tasks):
    print(f"\n{Fore.CYAN}➕ ADD NEW TASK")
    text = input(Fore.WHITE + "📝 Task description: ")
    
    # Due date with validation
    while True:
        due = input(Fore.WHITE + "📅 Due date (YYYY-MM-DD or +days for relative): ")
        if not due:
            due = None
            break
        elif due.startswith('+'):
            try:
                days = int(due[1:])
                due_date = datetime.now() + timedelta(days=days)
                due = due_date.strftime("%Y-%m-%d")
                print(Fore.GREEN + f"📅 Set to: {due}")
                break
            except ValueError:
                print(Fore.RED + "❌ Please enter + followed by number of days")
        else:
            try:
                datetime.strptime(due, "%Y-%m-%d")
                break
            except ValueError:
                print(Fore.RED + "❌ Invalid date format. Use YYYY-MM-DD")

    # Priority with emoji
    priority_map = {"1": "🔥 High", "2": "⚠️ Medium", "3": "💤 Low"}
    print(Fore.WHITE + "🎯 Priority: 1-🔥 High, 2-⚠️ Medium, 3-💤 Low")
    priority_choice = input(Fore.WHITE + "Choose (1/2/3): ")
    priority = priority_map.get(priority_choice, "⚠️ Medium")

    # Category
    category = input(Fore.WHITE + "📂 Category (Work/Personal/Study/Other): ").capitalize() or "Other"

    tasks.append({
        "text": text,
        "due": due,
        "priority": priority,
        "category": category,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "completed": None
    })
    
    loading_animation("Adding task")
    print(Fore.GREEN + "✅ Task added successfully!")

def view_tasks(tasks, filter_type="all"):
    if not tasks:
        print(Fore.RED + "📭 No tasks found.")
        return
    
    filtered_tasks = tasks
    if filter_type == "pending":
        filtered_tasks = [t for t in tasks if not t["done"]]
    elif filter_type == "completed":
        filtered_tasks = [t for t in tasks if t["done"]]
    elif filter_type == "today":
        today = datetime.now().strftime("%Y-%m-%d")
        filtered_tasks = [t for t in tasks if t["due"] == today]

    if not filtered_tasks:
        print(Fore.YELLOW + f"📭 No {filter_type} tasks.")
        return

    print(f"\n{Fore.MAGENTA}📋 TASKS ({filter_type.upper()})")
    print(Fore.CYAN + "─" * 80)
    
    for i, task in enumerate(filtered_tasks, 1):
        status = "✅" if task["done"] else "⏳"
        due = task["due"] if task["due"] else "No due date"
        
        # Color coding for overdue tasks
        if task["due"] and not task["done"]:
            due_date = datetime.strptime(task["due"], "%Y-%m-%d")
            if due_date < datetime.now():
                due = Fore.RED + f"🚨 {due} (OVERDUE)" + Fore.CYAN
        
        priority_color = {
            "🔥 High": Fore.RED,
            "⚠️ Medium": Fore.YELLOW,
            "💤 Low": Fore.GREEN
        }.get(task["priority"], Fore.WHITE)
        
        print(f"{i}. {status} {task['text']}")
        print(f"   📅 {due} | {priority_color}{task['priority']}{Fore.CYAN} | 📂 {task['category']}")
        if task["done"] and task["completed"]:
            print(f"   🎉 Completed: {task['completed']}")
        print(Fore.CYAN + "   " + "─" * 60)

def mark_done(tasks):
    pending_tasks = [t for t in tasks if not t["done"]]
    if not pending_tasks:
        print(Fore.GREEN + "🎉 All tasks are already completed!")
        return
        
    view_tasks(tasks, "pending")
    try:
        num = int(input(Fore.CYAN + "🎯 Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            if not tasks[num-1]["done"]:
                tasks[num-1]["done"] = True
                tasks[num-1]["completed"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                print(Fore.GREEN + "🎉 Task marked as done! Great job! 🏆")
            else:
                print(Fore.YELLOW + "ℹ️ Task is already completed.")
        else:
            print(Fore.RED + "❌ Invalid task number.")
    except ValueError:
        print(Fore.RED + "❌ Please enter a valid number.")

def search_tasks(tasks):
    term = input(Fore.CYAN + "🔍 Search term: ").lower()
    results = [t for t in tasks if term in t["text"].lower() or term in t["category"].lower()]
    
    if results:
        print(Fore.MAGENTA + f"\n🔍 Found {len(results)} matching tasks:")
        for i, task in enumerate(results, 1):
            status = "✅" if task["done"] else "⏳"
            print(f"{i}. {status} {task['text']} [{task['category']}]")
    else:
        print(Fore.RED + "❌ No matching tasks found.")

def edit_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input(Fore.CYAN + "✏️ Enter task number to edit: "))
        if 1 <= num <= len(tasks):
            task = tasks[num-1]
            print(Fore.YELLOW + f"Editing: {task['text']}")
            
            new_text = input(Fore.WHITE + f"New description (current: {task['text']}): ")
            if new_text:
                task["text"] = new_text
                
            new_due = input(Fore.WHITE + f"New due date (current: {task['due']}): ")
            if new_due:
                task["due"] = new_due
                
            print(Fore.GREEN + "✅ Task updated successfully!")
        else:
            print(Fore.RED + "❌ Invalid task number.")
    except ValueError:
        print(Fore.RED + "❌ Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input(Fore.RED + "🗑️ Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            deleted_task = tasks.pop(num-1)
            print(Fore.GREEN + f"✅ Deleted: {deleted_task['text']}")
        else:
            print(Fore.RED + "❌ Invalid task number.")
    except ValueError:
        print(Fore.RED + "❌ Please enter a valid number.")

def show_statistics(tasks):
    if not tasks:
        print(Fore.RED + "📊 No tasks to show statistics.")
        return
        
    total = len(tasks)
    completed = sum(1 for t in tasks if t["done"])
    pending = total - completed
    completion_rate = (completed / total) * 100 if total > 0 else 0
    
    # Priority statistics
    high_priority = sum(1 for t in tasks if "🔥" in t["priority"])
    medium_priority = sum(1 for t in tasks if "⚠️" in t["priority"])
    low_priority = sum(1 for t in tasks if "💤" in t["priority"])
    
    print(f"\n{Fore.CYAN}📊 TASK STATISTICS")
    print(Fore.MAGENTA + "┌────────────────────────────────────────┐")
    print(Fore.MAGENTA + f"│ 📈 Total Tasks: {total:>24} │")
    print(Fore.GREEN + f"│ ✅ Completed: {completed:>26} │")
    print(Fore.YELLOW + f"│ ⏳ Pending: {pending:>28} │")
    print(Fore.CYAN + f"│ 📊 Completion Rate: {completion_rate:>17.1f}% │")
    print(Fore.MAGENTA + "├────────────────────────────────────────┤")
    print(Fore.RED + f"│ 🔥 High Priority: {high_priority:>21} │")
    print(Fore.YELLOW + f"│ ⚠️ Medium Priority: {medium_priority:>18} │")
    print(Fore.GREEN + f"│ 💤 Low Priority: {low_priority:>22} │")
    print(Fore.MAGENTA + "└────────────────────────────────────────┘")

def save_tasks(tasks):
    loading_animation("Saving tasks")
    try:
        with open(TASKS_FILE, "w") as f:
            json.dump(tasks, f, indent=2)
        print(Fore.GREEN + f"💾 Tasks saved successfully! ({len(tasks)} tasks)")
    except Exception as e:
        print(Fore.RED + f"❌ Error saving tasks: {e}")

def load_tasks():
    loading_animation("Loading tasks")
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = json.load(f)
        print(Fore.GREEN + f"📂 Loaded {len(tasks)} tasks successfully!")
        return tasks
    except FileNotFoundError:
        print(Fore.YELLOW + "📂 No saved tasks found. Starting fresh!")
        return []
    except json.JSONDecodeError:
        print(Fore.RED + "❌ Error: tasks.json is corrupted.")
        return []

# ----- ENHANCED MAIN LOOP -----
def main():
    tasks = load_tasks()
    show_title()
    
    # Welcome message with typing effect
    typing_effect(Fore.GREEN + "🚀 Welcome to your task tracker! Let's get started...")
    
    while True:
        show_menu()
        choice = input(Fore.CYAN + "🎯 Select an option (0-9): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            print(f"\n{Fore.YELLOW}📋 VIEW OPTIONS: 1-All, 2-Pending, 3-Completed, 4-Today's")
            view_choice = input(Fore.CYAN + "Choose view: ")
            views = {"1": "all", "2": "pending", "3": "completed", "4": "today"}
            view_tasks(tasks, views.get(view_choice, "all"))
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            search_tasks(tasks)
        elif choice == "5":
            edit_task(tasks)
        elif choice == "6":
            delete_task(tasks)
        elif choice == "7":
            show_statistics(tasks)
        elif choice == "8":
            save_tasks(tasks)
        elif choice == "9":
            tasks = load_tasks()
        elif choice == "0":
            print(Fore.YELLOW + "💾 Saving before exit...")
            save_tasks(tasks)
            typing_effect(Fore.MAGENTA + "👋 Thank you for using Daily Task Tracker! See you soon! 🌟")
            break
        else:
            print(Fore.RED + "❌ Invalid option. Please choose 0-9.")
        
        input(Fore.CYAN + "\n↵ Press Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n👋 Goodbye! Thanks for using Daily Task Tracker!")
        sys.exit(0)