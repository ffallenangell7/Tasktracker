📝 Daily Task Tracker
A modern, interactive, and feature-rich command-line task management application built with Python. Stay organized with style! ✨

https://img.shields.io/badge/Python-3.6+-blue.svg
https://img.shields.io/badge/License-MIT-green.svg
https://img.shields.io/badge/Version-2.0-ff69b4.svg

🚀 Features
🎯 Core Functionality
➕ Add Tasks with descriptions, due dates, priorities, and categories

📋 View Tasks with multiple filter options (all, pending, completed, today's)

✅ Mark Tasks as Done with completion timestamps

🔍 Search Tasks by text or category

✏️ Edit Existing Tasks to update details

🗑️ Delete Tasks you no longer need

📊 Task Statistics with completion rates and priority breakdown

🎨 Enhanced User Experience
🌈 Colorful Interface with emojis and visual indicators

⌨️ Typing Effects for immersive interactions

⏳ Loading Animations for smooth transitions

🚨 Overdue Alerts with color-coded warnings

📱 Responsive Design that works on all terminals

💾 Data Management
💾 Auto-save functionality

📂 JSON Storage for persistent data

🔄 Import/Export capabilities

⚡ Quick Reload of saved tasks

🛠️ Installation
Prerequisites
Python 3.6 or higher

pip (Python package manager)

Step 1: Clone the Repository
bash
git clone https://github.com/ffallenangell7/Tasktracker
cd daily-task-tracker
Step 2: Install Required Packages
bash
pip install colorama pyfiglet
Step 3: Run the Application
bash
python task_tracker.py
📖 How to Use
Main Menu Options
text
🎯 MAIN MENU
┌────────────────────────────────────────┐
│ 1️⃣   Add New Task                      │
│ 2️⃣   View All Tasks                    │
│ 3️⃣   Mark Task as Done                 │
│ 4️⃣   Search Tasks                      │
│ 5️⃣   Edit Task                         │
│ 6️⃣   Delete Task                       │
│ 7️⃣   Task Statistics                   │
│ 8️⃣   Save Tasks                        │
│ 9️⃣   Load Tasks                        │
│ 0️⃣   Exit                             │
└────────────────────────────────────────┘
Adding Tasks
When adding a task, you can specify:

📝 Description: The main task text

📅 Due Date: Use YYYY-MM-DD format or +days (e.g., +3 for 3 days from now)

🎯 Priority:

1 - 🔥 High (Red)

2 - ⚠️ Medium (Yellow)

3 - 💤 Low (Green)

📂 Category: Work, Personal, Study, or Other

Viewing Options
All Tasks: Complete overview

Pending: Only unfinished tasks

Completed: Finished tasks with completion dates

Today's: Tasks due today

🎨 Screenshots
(Add your screenshots here)

Main menu interface

Task list view

Statistics dashboard

Adding a new task

📊 Task Features
Priority System
🔥 High: Critical tasks that need immediate attention

⚠️ Medium: Important but not urgent tasks

💤 Low: Tasks that can be done when convenient

Due Date Flexibility
Absolute dates: 2024-01-15

Relative dates: +5 (5 days from today)

No due date: Leave blank

Smart Notifications
🚨 OVERDUE: Red highlighting for past-due tasks

⏳ Pending: Yellow clock icon for unfinished tasks

✅ Completed: Green checkmark for finished tasks

💾 Data Storage
Tasks are automatically saved to tasks.json in the same directory. The file format is human-readable JSON:

json
[
  {
    "text": "Complete project proposal",
    "due": "2024-01-20",
    "priority": "🔥 High",
    "category": "Work",
    "done": false,
    "created": "2024-01-15 14:30",
    "completed": null
  }
]
🐛 Troubleshooting
Common Issues
Q: I get a ModuleNotFoundError when running the script
A: Make sure all dependencies are installed:

bash
pip install colorama pyfiglet
Q: The colors don't show up in my terminal
A: Some terminals may not support ANSI colors. Try using Windows Terminal, iTerm2, or a modern terminal emulator.

Q: My tasks aren't saving
A: Check if the application has write permissions in the current directory and that tasks.json isn't open in another program.

🤝 Contributing
We welcome contributions! Please feel free to submit pull requests or open issues for bugs and feature requests.

Development Setup
Fork the repository

Create a feature branch: git checkout -b feature/amazing-feature

Commit your changes: git commit -m 'Add amazing feature'

Push to the branch: git push origin feature/amazing-feature

Open a pull request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Colorama for cross-platform terminal colors

PyFiglet for ASCII art banners

Inspired by various task management methodologies
