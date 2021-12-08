from tkinter import *
from tkinter import font
from tkinter.font import BOLD
import backend
from functools import partial

# Main window configuration
window = Tk()
window.configure(bg='#21215c')
window.geometry('500x700')
window.maxsize(width=500,height=700)
window.minsize(width=500,height = 700)
window.title('MoToDo')
list_of_tasks = backend.view()

# ADD Task Button 
class adding_task_functionality():
    def adding_tasks():
        add_task_window = Tk()
        add_task_window.configure(bg='#21215c')
        add_task_window.title('Add Task')
        add_task_window.geometry('370x125')
        add_task_window.maxsize(width=370,height=125)
        add_task_window.minsize(width=370,height=125)

        def get_task_details():
            title_input =task_title_input.get()
            backend.insert_tasks(title_input)
            list_of_tasks=backend.view()
            task_functionality.view_tasks(list_of_tasks)
                

        #task details
        task_font_settings = font.Font(size=20,weight = 'bold')
        task_title = Label(add_task_window, text = 'Task Title:',bg='#21215c',font = task_font_settings,fg='#fff').grid(row=1,column=1)
        task_title_input = Entry(add_task_window, width=26)
        task_title_input.grid(row=1,column=2)
        add_button = Button(add_task_window,text='Add Task',font=button_font_settings,command=get_task_details).grid(row=4, column=2)

        add_task_window.mainloop()


class task_functionality():
    def delete_task(task_id):
                    task_details.destroy()
                    check_mark.destroy()
                    delete_task_button.destroy()
                    backend.delete(task_id)
                    list_of_tasks = (backend.view())
                    
    def view_tasks(tasklist):
        task_label_distance = 80
        if len(tasklist) > 0:
            for i in tasklist:
                global check_mark
                check_mark = Checkbutton(window)
                check_mark.place(x=20, y = task_label_distance + 14,width=15,height=15)
                global task_details
                task_details = Label(window,text = i, width= 35, height = 2,font = 2, bg = '#6363eb')
                task_details.place(x = 40,y=task_label_distance)
                global delete_task_button
                delete_task_button=Button(window, text='delete', command=partial(task_functionality.delete_task, i))
                delete_task_button.place(x=445,y=task_label_distance+14)
                task_label_distance += 60
                window.update()
        else:
            return print('None')
            


button_font_settings = font.Font(size=20,weight = 'bold')

add_task_button = Button(window, text='add task', bg='#5e9fb1',width=10,height=1,font = button_font_settings, command= adding_task_functionality.adding_tasks)
add_task_button.place(x = 10,y = 10)

# Set Timer Button
set_timer_button = Button(window, text='set timer', bg='#949494',width=10,height=1,font = button_font_settings )
set_timer_button.place(x=315, y = 10)


