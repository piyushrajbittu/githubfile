import tkinter as tk
root = tk.Tk()
def add():
    print('Adding task to the list')
    data = entry.get()
    if data:
        # task_list.insert(0, data)
        task_list.insert(tk.END, data)
        entry.delete(0, tk.END)
def delete():
    print('Deleting task from the list')
    task_list.delete(tk.ACTIVE)
root.geometry('400x400')
root.resizable(width=False, height=False)
root.title('To Do List')
entry = tk.Entry(root)
entry.pack(padx=10, pady=10, fill='x')
add_button = tk.Button(root, text='Add Task',command=add, width=20, bg='red', fg='white')
add_button.pack()
task_list = tk.Listbox(root)
task_list.pack(fill='x', padx=20, pady=10)
delete_button = tk.Button(root, text='Delete Task',command=delete, width=20)
delete_button.pack()
root.mainloop()