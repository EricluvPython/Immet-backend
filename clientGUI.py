import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
from PIL import Image, ImageTk
import os
import subprocess
import threading
import shutil
import time
# import pyglet

class ClientGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Infinity Co.")
        self.root.geometry("300x600")
        self.bgcolor = "#1520A6"
        self.fgcolor = "#808080"
        self.bgcolor2 = "#797Ef6"
        self.contentbgcolor = "#538BC8"
        # pyglet.font.add_file("Bungee-Regular.ttf")
        # if (not pyglet.font.have_font("Bungee")):
        #     exit()
        # self.fontfamily = pyglet.font.load("Bungee")
        self.fontfamily = "Courier"
        self.finishedtasks = {}
        self.runningtasks = {}
        self.curjobid = 0
        self.balance = 15390
        self.create_login_screen()

    def create_login_screen(self):
        login_frame = tk.Frame(self.root)
        login_frame.pack(expand=True, fill=tk.BOTH)

        # logo
        logo_image = ImageTk.PhotoImage(Image.open('assets/logo-flipped.png').resize((100, 90)))
        canvas = tk.Canvas(login_frame, bg=self.bgcolor, width=100, height=90, highlightthickness=0)
        canvas.pack(pady=(80, 15))
        canvas.create_image(0, 0, image=logo_image, anchor=tk.NW)
        
        logo_label = tk.Label(login_frame, image=logo_image)
        logo_label.image = logo_image  # To prevent garbage collection

        # slogan
        slogan1_label = tk.Label(login_frame, text="Compute with", bg=self.bgcolor, font=(self.fontfamily, 16), fg="white")
        slogan1_label.pack(pady=(5, 0))

        slogan2_label = tk.Label(login_frame, text="Infinity Cloud", bg=self.bgcolor, font=(self.fontfamily, 18, "bold"), fg="white")
        slogan2_label.pack(pady=(0, 30))

        # login box
        login_box_frame = tk.Frame(login_frame, bg=self.fgcolor, padx=80)
        login_box_frame.pack(pady=(10, 0))

        # login title
        log_in_title_label = tk.Label(login_box_frame, text="LOG IN", bg=self.fgcolor, font=(self.fontfamily, 18, "bold"))
        log_in_title_label.pack(pady=(30, 5))

        # username box
        username_entry = tk.Entry(login_box_frame, font=(self.fontfamily, 12))
        username_entry.insert(0, "EricFrenzy")
        username_entry.pack(pady=(20, 10))

        # password box
        password_entry = tk.Entry(login_box_frame, show="*", font=(self.fontfamily, 12))
        password_entry.insert(0, "Password")
        password_entry.pack(pady= (10, 20))

        # login button
        login_button = tk.Button(login_box_frame, text="Login", command=self.show_homepage, font=(self.fontfamily, 12))
        login_button.pack(pady=(10, 20))

        # Additional options
        forgot_password_label = tk.Label(login_box_frame, text="Forgot your password?", bg=self.fgcolor)
        forgot_password_label.pack(pady=(10, 5))

        sign_up_label = tk.Label(login_box_frame, text="Sign up", bg=self.fgcolor)
        sign_up_label.pack(pady=(5, 15))

        # Changeable background
        login_frame.configure(bg=self.bgcolor)

        # # background
        # bg_image = ImageTk.PhotoImage(Image.open('assets/BG.png').resize((300, 600)))
        # bg_canvas = tk.Canvas(self.root, bg=self.bgcolor, width=300, height=600, highlightthickness=0)
        # bg_canvas.pack(fill="both", expand=True)
        # bg_canvas.create_image(0, 0, image=bg_image, anchor=tk.NW)
        
        # bg_label = tk.Label(self.root, image=bg_image)
        # bg_label.image = bg_image  # To prevent garbage collection

    def show_homepage(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.geometry("800x600")
        homepage_frame = tk.Frame(self.root)
        homepage_frame.pack(expand=True, fill=tk.BOTH)
        # Left menu column
        menu_column = tk.Frame(homepage_frame, width=100, bg=self.bgcolor)
        menu_column.pack(side=tk.LEFT, fill=tk.Y)

        # logo
        logo_image = ImageTk.PhotoImage(Image.open('assets/logo-flipped.png').resize((80, 72)))
        canvas = tk.Canvas(menu_column, bg=self.bgcolor, width=80, height=72, highlightthickness=0)
        canvas.pack(pady=(60, 20), padx=(30, 30))
        canvas.create_image(0, 0, image=logo_image, anchor=tk.NW)
        logo_label = tk.Label(menu_column, image=logo_image)
        logo_label.image = logo_image  # To prevent garbage collection

        text_label = tk.Label(menu_column, text="United in Infinity.", bg=self.bgcolor, fg="white", font=(self.fontfamily, 12, "italic", "bold"))
        text_label.pack(pady=(10, 30))
        
        # new job button
        new_job_button = tk.Button(menu_column, text="Submit new job", command=self.show_submit_job, bg=self.bgcolor2, font=(self.fontfamily, 18, "bold"))
        new_job_button.pack(pady=(0, 10))

        # review job button
        review_job_button = tk.Button(menu_column, text="Review my jobs", command=self.show_review_jobs, bg=self.bgcolor2, font=(self.fontfamily, 18, "bold"))
        review_job_button.pack(pady=10)

        # settings button
        settings_button = tk.Button(menu_column, text="   Settings   ", command=self.show_settings, bg=self.bgcolor2, font=(self.fontfamily, 18, "bold"))
        settings_button.pack(pady=10)

        # balance
        balance_label = tk.Label(menu_column, text="Your InfiniCoins:", font=(self.fontfamily, 14, "bold"))
        balance_label.pack()

        coin_image_file = Image.open('assets/Coin.png')
        coin_image = ImageTk.PhotoImage(coin_image_file.resize((50, 50)))
        canvas = tk.Canvas(menu_column, bg=self.bgcolor, width=50, height=50, highlightthickness=0)
        canvas.place(x=20, y=450)
        canvas.create_image(0, 0, image=coin_image, anchor=tk.NW)
        self.coin_label = tk.Label(menu_column, text=f": {self.balance:,}", font=(self.fontfamily, 18, "bold"), bg=self.bgcolor, fg="white")
        self.coin_label.image = coin_image  # To prevent garbage collection
        self.coin_label.place(x=75, y=455)

        self.increment_label = tk.Label(menu_column, text="+ 0.0 / s", bg=self.bgcolor, fg="grey", font=(self.fontfamily, 18, "bold"))
        self.increment_label.pack(pady=(60,0))
        self.update_coin()

        # Right interactive interface
        self.content_frame = tk.Frame(homepage_frame, bg=self.contentbgcolor)
        self.content_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        self.show_submit_job()   


    def show_submit_job(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # submit job page title
        submit_job_title_label = tk.Label(self.content_frame, text="UPLOAD YOUR SCRIPTS", bg=self.contentbgcolor, font=(self.fontfamily, 18, "bold"), width=400)
        submit_job_title_label.pack(pady=(40, 10))

        # browse file button
        browse_button = tk.Button(self.content_frame, text="Browse files", command=self.browse_files, font=(self.fontfamily, 16, "bold"))
        browse_button.pack(pady=20, padx=10)

        # selected file region
        selected_files_frame = tk.Frame(self.content_frame)
        selected_files_frame.pack()
        self.selected_file_label = tk.Label(selected_files_frame, text="Selected Files:\n\n", font=(self.fontfamily, 16, "bold"), anchor="w", justify="left")
        self.selected_file_label.pack(pady=(10, 20),padx=(20, 20))

        # select number of nodes
        nodes_label = tk.Label(self.content_frame, text="Number of Nodes:", font=(self.fontfamily, 16, "bold"))
        nodes_label.pack(pady=20)

        self.nodes_entry = tk.Spinbox(self.content_frame, width=2, from_=1, to=10, increment=1, font=(self.fontfamily, 16, "bold"))
        self.nodes_entry.pack(pady=(0, 10))

        # put run command
        command_label = tk.Label(self.content_frame, text="Command to be distributed:", font=(self.fontfamily, 16, "bold"))
        command_label.pack(pady=(20, 0))

        command_clarification_label = tk.Label(self.content_frame, text="e.g. python mytask.py", bg=self.contentbgcolor, font=(self.fontfamily, 14))
        command_clarification_label.pack(pady=(5, 20))

        self.command_entry = tk.Entry(self.content_frame, font=(self.fontfamily, 16))
        self.command_entry.pack(pady=(0, 10))

        # submit button
        submit_button = tk.Button(self.content_frame, text="Submit Task", font=(self.fontfamily, 16, "bold"), command=self.submit_task)
        submit_button.pack(pady=10)
    
    def show_review_jobs(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # review job page title
        review_job_title_label = tk.Label(self.content_frame, text="YOUR JOB HISTORY", bg=self.contentbgcolor, font=(self.fontfamily, 18, "bold"), width=400)
        review_job_title_label.pack(pady=(40, 30))

        # selected file region
        finished_jobs_frame = tk.Frame(self.content_frame)
        finished_jobs_frame.pack()
        self.finished_file_label = tk.Label(finished_jobs_frame, text="Finished Jobs:\n\n", font=(self.fontfamily, 16, "bold"), anchor="w", justify="left")
        self.finished_file_label.pack(pady=(10, 20),padx=(20, 20))
        
        tasksstr = "\n".join([f"{i[1]} on {i[0]} nodes" for i in self.finishedtasks.values()])
        self.finished_file_label.config(text=f"Finished Jobs:\n\n{tasksstr}")

        # button for fetching results
        get_result_button = tk.Button(self.content_frame, text="Download results", command=self.download_results, font=(self.fontfamily, 16, "bold"))
        get_result_button.pack(pady=20)

    def show_settings(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def browse_files(self):
        self.file_paths = tkinter.filedialog.askopenfiles()
        files = "\n".join([file_path.name.split("/")[-1] for file_path in self.file_paths])
        self.selected_file_label.config(text=f"Selected Files:\n\n{files}")

    def submit_task(self):
        numofnodes = int(self.nodes_entry.get())
        command = self.command_entry.get()
        if (command == "" or numofnodes < 0):
            return
        # for file in self.file_paths:
        #     shutil.copyfile(file, "./uploaded/")
        command_thread = threading.Thread(target=lambda :subprocess.run(["mpiexec",  "-n", str(numofnodes)] + command.split(" "), text=True, capture_output=True))
        tk.messagebox.showinfo("Submission Success",  "Your task has been uploaded. Please check your results in 'Review my Jobs' after some time.")
        command_thread.start()
        self.runningtasks[self.curjobid] = [numofnodes, command]
        self.monitor_thread_status(command_thread, self.curjobid)
        self.finishedtasks[self.curjobid] = [numofnodes, command]
        self.curjobid += 1
        self.show_submit_job()

    def download_results(self):
        if self.finishedtasks == {}:
            return
        savedir = tkinter.filedialog.askdirectory(initialdir="./")
        resultdir = "./results/"
        results = os.listdir(resultdir)
        for filename in results:
            shutil.move(resultdir+filename, savedir)
        self.finishedtasks = {}
        tk.messagebox.showinfo("Download Success",  f"Your results have been saved under {savedir}.")
        self.show_submit_job()

    def monitor_thread_status(self, command_thread, jobid):
        if command_thread.is_alive():
            self.root.after(500, lambda :self.monitor_thread_status(command_thread, jobid))
        else:
            self.finishedtasks[jobid] = self.runningtasks[jobid]
            del self.runningtasks[jobid]
            tk.messagebox.showinfo("Task Completed",  f"Your task {jobid} is completed. Please check your results in 'Review my Jobs'.")

    def update_coin(self):
        decval = 0
        for jid in self.runningtasks:
            decval += int(self.runningtasks[jid][0]) * 2
        self.balance -= decval
        self.coin_label.config(text=f": {self.balance:,}")
       
        # Change inc/dec color based on the state
        if decval == 0:
            self.increment_label.configure(fg="grey", text="+ 0.0 / s")
        else:
            self.increment_label.configure(fg="red", text=f"- {decval:.2f} / s")

        # Call the update_timer function after 1000 milliseconds (1 second)
        self.coin_timer = self.root.after(1000, self.update_coin)
            
if __name__ == "__main__":
    root = tk.Tk()
    app = ClientGUI(root)
    root.mainloop()
