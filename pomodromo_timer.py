import tkinter as tk
import time

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")

        self.work_time = 25 * 60  # 25 minutes in seconds
        self.break_time = 5 * 60  # 5 minutes in seconds
        self.is_running = False
        self.is_break = False

        self.label = tk.Label(root, text="Pomodoro Timer", font=("Helvetica", 24))
        self.label.pack(pady=20)

        self.time_label = tk.Label(root, text=self.format_time(self.work_time), font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer, font=("Helvetica", 14))
        self.start_button.pack(side=tk.LEFT, padx=20)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer, font=("Helvetica", 14))
        self.reset_button.pack(side=tk.RIGHT, padx=20)

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    def update_timer(self):
        if self.is_running:
            if self.is_break:
                self.break_time -= 1
                self.time_label.config(text=self.format_time(self.break_time))
                if self.break_time <= 0:
                    self.is_running = False
                    self.is_break = False
                    self.break_time = 5 * 60
                    self.label.config(text="Break Over! Back to Work!")
            else:
                self.work_time -= 1
                self.time_label.config(text=self.format_time(self.work_time))
                if self.work_time <= 0:
                    self.is_running = False
                    self.is_break = True
                    self.work_time = 25 * 60
                    self.label.config(text="Work Session Over! Take a Break!")

            if self.is_running:
                self.root.after(1000, self.update_timer)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.label.config(text="Work Time!" if not self.is_break else "Break Time!")
            self.update_timer()

    def reset_timer(self):
        self.is_running = False
        self.is_break = False
        self.work_time = 25 * 60
        self.break_time = 5 * 60
        self.label.config(text="Pomodoro Timer")
        self.time_label.config(text=self.format_time(self.work_time))

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
