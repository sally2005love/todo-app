from todo import add_task, get_tasks, complete_task, delete_task

def main():
    while True:
        show_menu()
        choice = input("선택: ")

        if choice == "1":
            task = input("할 일 입력: ")
            add_task(task)

        elif choice == "2":
            print(get_tasks())

        elif choice == "3":
            idx = int(input("완료할 번호: "))
            complete_task(idx)

        elif choice == "4":
            idx = int(input("삭제할 번호: "))
            delete_task(idx)

