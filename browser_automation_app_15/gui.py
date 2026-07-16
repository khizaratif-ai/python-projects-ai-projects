import tkinter as tk
from tkinter import messagebox
from main import WebAutomation


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Automation GUI")
        self.root.geometry("400x320")

        self.web_automation = None

        # Login Frame
        login_frame = tk.LabelFrame(root, text="Login")
        login_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(login_frame, text="Username").grid(row=0, column=0, padx=5, pady=5)
        self.entry_username = tk.Entry(login_frame, width=30)
        self.entry_username.grid(row=0, column=1, padx=5)

        tk.Label(login_frame, text="Password").grid(row=1, column=0, padx=5, pady=5)
        self.entry_password = tk.Entry(login_frame, show="*", width=30)
        self.entry_password.grid(row=1, column=1, padx=5)

        # Form Frame
        form_frame = tk.LabelFrame(root, text="Text Box Form")
        form_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(form_frame, text="Full Name").grid(row=0, column=0, padx=5, pady=5)
        self.entry_fullname = tk.Entry(form_frame, width=30)
        self.entry_fullname.grid(row=0, column=1)

        tk.Label(form_frame, text="Email").grid(row=1, column=0, padx=5, pady=5)
        self.entry_email = tk.Entry(form_frame, width=30)
        self.entry_email.grid(row=1, column=1)

        tk.Label(form_frame, text="Current Address").grid(row=2, column=0, padx=5, pady=5)
        self.entry_current = tk.Entry(form_frame, width=30)
        self.entry_current.grid(row=2, column=1)

        tk.Label(form_frame, text="Permanent Address").grid(row=3, column=0, padx=5, pady=5)
        self.entry_permanent = tk.Entry(form_frame, width=30)
        self.entry_permanent.grid(row=3, column=1)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Submit", width=15, command=self.submit).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Close Browser", width=15, command=self.close_browser).grid(row=0, column=1, padx=5)

    def submit(self):
        try:
            self.web_automation = WebAutomation()

            self.web_automation.login(
                self.entry_username.get(),
                self.entry_password.get()
            )

            self.web_automation.fill_form(
                self.entry_fullname.get(),
                self.entry_email.get(),
                self.entry_current.get(),
                self.entry_permanent.get()
            )

            messagebox.showinfo("Success", "Automation completed.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def close_browser(self):
        if self.web_automation:
            self.web_automation.close()
            messagebox.showinfo("Success", "Browser closed.")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()