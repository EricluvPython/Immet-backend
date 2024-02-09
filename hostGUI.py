import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
# import pyglet

class HostGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Infinity Co.")
        self.root.geometry("300x600")
        self.bgcolor = "#1520A6"
        self.fgcolor = "#808080"
        self.connected = False
        # pyglet.font.add_file("Bungee-Regular.ttf")
        # if (not pyglet.font.have_font("Bungee")):
        #     exit()
        # self.fontfamily = pyglet.font.load("Bungee")
        self.fontfamily = "Courier"
        self.balance = 15390
        self.create_login_screen()

    def create_login_screen(self):
        login_frame = tk.Frame(self.root)
        login_frame.pack(expand=True, fill=tk.BOTH)

        # logo
        logo_image = ImageTk.PhotoImage(Image.open('assets/logo.png').resize((100, 90)))
        canvas = tk.Canvas(login_frame, bg=self.bgcolor, width=100, height=90, highlightthickness=0)
        canvas.pack(pady=(80, 15))
        canvas.create_image(0, 0, image=logo_image, anchor=tk.NW)
        
        logo_label = tk.Label(login_frame, image=logo_image)
        logo_label.image = logo_image  # To prevent garbage collection

        # slogan
        slogan1_label = tk.Label(login_frame, text="Earn from", bg=self.bgcolor, font=(self.fontfamily, 16), fg="white")
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
        homepage_frame = tk.Frame(self.root)
        homepage_frame.pack(expand=True, fill=tk.BOTH)

        # Top bar
        self.connection_label = tk.Label(homepage_frame, text="Disconnected", padx=120, bg="red", fg="white", font=(self.fontfamily, 18, "bold"))
        self.connection_label.pack(pady=(0, 0))

        # Connect button
        self.connect_button = tk.Button(homepage_frame, text="Connect", font=(self.fontfamily, 24, "bold"), bg="red", fg="white", command=self.toggle_connect)
        self.connect_button.pack(pady=(70, 70))

        # Balance
        balance_label = tk.Label(homepage_frame, text="Your InfiniCoins:", font=(self.fontfamily, 16, "bold"))
        balance_label.pack()

        coin_image_file = Image.open('assets/Coin.png')
        coin_image = ImageTk.PhotoImage(coin_image_file.resize((50, 50)))
        canvas = tk.Canvas(homepage_frame, bg=self.bgcolor, width=50, height=50, highlightthickness=0)
        canvas.place(x=60, y=280)
        canvas.create_image(0, 0, image=coin_image, anchor=tk.NW)
        self.coin_label = tk.Label(homepage_frame, text=f": {self.balance:,}", font=(self.fontfamily, 18, "bold"), bg=self.bgcolor, fg="white")
        self.coin_label.image = coin_image  # To prevent garbage collection
        self.coin_label.place(x=120, y=285)

        self.increment_label = tk.Label(homepage_frame, text="+ 0.0 / s", bg=self.bgcolor, fg="grey", font=(self.fontfamily, 18, "bold"))
        self.increment_label.pack(pady=(60,0))

        # Analytics
        analytics_image = ImageTk.PhotoImage(Image.open('assets/Analytics.png').resize((280, 150)))
        canvas = tk.Canvas(homepage_frame, bg=self.bgcolor, width=280, height=150, highlightthickness=0)
        canvas.pack(pady=(20, 10))
        canvas.create_image(0, 0, image=analytics_image, anchor=tk.NW)
        
        analytics_label = tk.Label(homepage_frame, image=analytics_image)
        analytics_label.image = analytics_image  # To prevent garbage collection
    
        # Navbar
        navbar_image = ImageTk.PhotoImage(Image.open('assets/Navbar.png').resize((305, 55)))
        canvas = tk.Canvas(homepage_frame, bg=self.bgcolor, width=305, height=55, highlightthickness=0)
        canvas.pack(pady=(10, 0))
        canvas.create_image(0, 0, image=navbar_image, anchor=tk.NW)
        
        navbar_label = tk.Label(homepage_frame, image=navbar_image)
        navbar_label.image = navbar_image  # To prevent garbage collection
        # Changeable background
        homepage_frame.configure(bg=self.bgcolor)
    
    def toggle_connect(self):
        self.connected = not self.connected
        if self.connected:
            self.timer = time.time()

        # Change button color based on the state
        if not self.connected:
            self.connect_button.configure(bg="red", text="Connect")
            self.connection_label.configure(bg="red", text="Disconnected")
            self.increment_label.configure(fg="grey", text="+ 0.0 / s")
            self.stop_update_coin()
        else:
            self.connect_button.configure(bg="orange", text = "Disconnect")
            self.connection_label.configure(bg="orange", text = "Connected")
            self.increment_label.configure(fg="grey", text="+ 0.0 / s")
            self.root.after(5000, self.become_running)
            
    def become_running(self):
        self.connect_button.configure(bg="green", text = "Disconnect", state="disabled")
        self.connection_label.configure(bg="green", text = "Task Running")
        self.increment_label.configure(fg="green", text="+ 2.0 / s")
        self.root.after(6000, self.become_available)
        self.update_coin()
    
    def become_available(self):
        self.stop_update_coin()
        self.connect_button.configure(bg="orange", text = "Disconnect", state="normal")
        self.connection_label.configure(bg="orange", text = "Connected")
        self.increment_label.configure(fg="grey", text="+ 0.0 / s")

    def stop_update_coin(self):
        self.root.after_cancel(self.coin_timer)

    def update_coin(self):
        # Update the timer label text
        self.balance += 2
        self.coin_label.config(text=f": {self.balance:,}")

        # Call the update_timer function after 1000 milliseconds (1 second)
        self.coin_timer = self.root.after(1000, self.update_coin)
            
if __name__ == "__main__":
    root = tk.Tk()
    app = HostGUI(root)
    root.mainloop()
