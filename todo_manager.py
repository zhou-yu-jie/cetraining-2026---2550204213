import json
import os

# ---------------------- 文件读写模块 ----------------------
FILE_NAME = "todo_data.json"

def load_todos():
    """从文件加载待办数据"""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_todos(todo_list):
    """保存待办数据到JSON文件"""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(todo_list, f, ensure_ascii=False, indent=2)

# ---------------------- 数据管理模块 ----------------------
def add_todo(todo_list, content, priority, deadline):
    """添加待办：内容、优先级(1高~5低)、截止日期"""
    new_todo = {
        "content": content,
        "priority": int(priority),
        "deadline": deadline,
        "is_finished": False
    }
    todo_list.append(new_todo)

def sort_by_priority(todo_list):
    """按优先级从高到低排序"""
    return sorted(todo_list, key=lambda x: x["priority"])

def sort_by_deadline(todo_list):
    """按截止日期升序排序"""
    return sorted(todo_list, key=lambda x: x["deadline"])

def mark_finished(todo_list, index):
    """标记为已完成"""
    todo_list[index]["is_finished"] = True

def delete_finished(todo_list):
    """删除所有已完成事项"""
    return [item for item in todo_list if not item["is_finished"]]

def filter_todos(todo_list, status):
    """筛选：all全部 / unfinished未完成 / finished已完成"""
    if status == "unfinished":
        return [t for t in todo_list if not t["is_finished"]]
    elif status == "finished":
        return [t for t in todo_list if t["is_finished"]]
    else:
        return todo_list

# ---------------------- 用户交互菜单模块 ----------------------
def show_menu():
    print("===== 个人待办事项管理器 =====")
    print("1. 添加待办事项")
    print("2. 查看待办(按优先级排序)")
    print("3. 查看待办(按截止日期排序)")
    print("4. 标记事项为已完成")
    print("5. 删除所有已完成事项")
    print("6. 筛选事项：全部/未完成/已完成")
    print("0. 退出程序")
    print("==============================")

def print_todo_list(todo_list):
    if len(todo_list) == 0:
        print("暂无待办事项！")
        return
    for idx, item in enumerate(todo_list):
        status = "✅已完成" if item["is_finished"] else "🔴未完成"
        print(f"{idx}. {status} | 优先级:{item['priority']} | 截止:{item['deadline']} | 内容:{item['content']}")

def main():
    todo_list = load_todos()
    while True:
        show_menu()
        choice = input("请输入功能序号：")
        if choice == "1":
            content = input("请输入待办内容：")
            priority = input("请输入优先级(1最高，5最低)：")
            deadline = input("请输入截止日期(例：2026-06-30)：")
            add_todo(todo_list, content, priority, deadline)
            save_todos(todo_list)
            print("添加成功！\n")

        elif choice == "2":
            data = sort_by_priority(todo_list)
            print_todo_list(data)

        elif choice == "3":
            data = sort_by_deadline(todo_list)
            print_todo_list(data)

        elif choice == "4":
            print_todo_list(todo_list)
            num = int(input("输入要完成事项的序号："))
            mark_finished(todo_list, num)
            save_todos(todo_list)
            print("标记完成！\n")

        elif choice == "5":
            todo_list = delete_finished(todo_list)
            save_todos(todo_list)
            print("已清空所有已完成事项！\n")

        elif choice == "6":
            opt = input("输入筛选条件(all/unfinished/finished)：")
            data = filter_todos(todo_list, opt)
            print_todo_list(data)

        elif choice == "0":
            print("程序退出")
            break
        else:
            print("输入错误，请重新选择！\n")

if __name__ == "__main__":
    main()
