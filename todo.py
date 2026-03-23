import json
import os
from datetime import datetime

TODO_FILE = "todos.json"

def load_todos():
    """加载待办事项"""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_todos(todos):
    """保存待办事项"""
    with open(TODO_FILE, 'w', encoding='utf-8') as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

def add_todo(task):
    """添加新任务"""
    todos = load_todos()
    new_todo = {
        "id": len(todos) + 1,
        "task": task,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    todos.append(new_todo)
    save_todos(todos)
    print(f"✅ 任务已添加: {task}")

def view_todos():
    """查看所有任务"""
    todos = load_todos()
    if not todos:
        print("📭 没有任务")
        return
    
    print("\n📋 待办事项：")
    print("-" * 50)
    for todo in todos:
        status = "✅" if todo['completed'] else "⭕"
        print(f"{status} [{todo['id']}] {todo['task']}")
    print("-" * 50)

def complete_todo(todo_id):
    """标记任务为完成"""
    todos = load_todos()
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = True
            save_todos(todos)
            print(f"✅ 任务已完成: {todo['task']}")
            return
    print("❌ 任务不存在")

def delete_todo(todo_id):
    """删除任务"""
    todos = load_todos()
    for i, todo in enumerate(todos):
        if todo['id'] == todo_id:
            task_name = todo['task']
            todos.pop(i)
            save_todos(todos)
            print(f"🗑️  任务已删除: {task_name}")
            return
    print("❌ 任务不存在")

def main():
    """主程序"""
    while True:
        print("\n🎯 待办事项应用")
        print("1. 查看任务")
        print("2. 添加任务")
        print("3. 完成任务")
        print("4. 删除任务")
        print("5. 退出")
        
        choice = input("请选择 (1-5): ")
        
        if choice == '1':
            view_todos()
        elif choice == '2':
            task = input("输入任务: ")
            if task:
                add_todo(task)
        elif choice == '3':
            view_todos()
            try:
                todo_id = int(input("输入任务编号: "))
                complete_todo(todo_id)
            except ValueError:
                print("❌ 请输入有效的编号")
        elif choice == '4':
            view_todos()
            try:
                todo_id = int(input("输入任务编号: "))
                delete_todo(todo_id)
            except ValueError:
                print("❌ 请输入有效的编号")
        elif choice == '5':
            print("👋 再见!")
            break
        else:
            print("❌ 无效选择")

if __name__ == "__main__":
    main()