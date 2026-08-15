import customtkinter as ctk
from tkinter import messagebox

from analyzer.breach import BreachCheckError, check_password_breach
from analyzer.strength import analyze_password
from components.header import create_header
from components.password import create_password_input, toggle_password
from components.results import ResultsPanel
from components.strength_meter import StrengthMeter
from config.theme import load_theme


load_theme()


class PasswordStrengthAnalyzer:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Password Strength Analyzer")
        self.root.geometry("900x760")
        self.root.minsize(800, 700)

        self.password_var = ctk.StringVar(value="")

        create_header(self.root)

        self.password_entry, self.show_password_var = create_password_input(
            self.root,
            self.password_var,
            self.on_password_change,
            toggle_password,
        )

        self.meter = StrengthMeter(self.root)
        self.results = ResultsPanel(self.root)

        actions = ctk.CTkFrame(self.root, fg_color="transparent")
        actions.pack(fill="x", padx=30, pady=(4, 5))

        ctk.CTkButton(
            actions,
            text="Check Breach",
            command=self.check_breach,
            width=180,
            height=42,
            corner_radius=10,
            font=("Segoe UI", 13, "bold"),
        ).pack(side="left")

        ctk.CTkButton(
            actions,
            text="Clear",
            command=self.clear,
            width=120,
            height=42,
            corner_radius=10,
            fg_color="#3b3f46",
            hover_color="#4b5058",
            font=("Segoe UI", 13, "bold"),
        ).pack(side="right")

        ctk.CTkLabel(
            self.root,
            text="Passwords are analyzed locally. Breach checking sends only a 5-character SHA-1 hash prefix.",
            text_color="#7d8793",
            font=("Segoe UI", 11),
        ).pack(anchor="w", padx=30, pady=(5, 18))

        self.on_password_change()

    def on_password_change(self, event=None):
        result = analyze_password(self.password_var.get())
        self.meter.update(result.score, result.label)
        self.results.update(result)

    def check_breach(self):
        password = self.password_var.get()

        if not password:
            messagebox.showwarning(
                "Breach Check",
                "Enter a password before checking breach exposure.",
            )
            return

        try:
            count = check_password_breach(password)
        except BreachCheckError as exc:
            messagebox.showerror(
                "Breach Check Error",
                f"Could not complete the breach check.\n\n{exc}",
            )
            return

        if count:
            messagebox.showwarning(
                "Password Exposed",
                f"This password appears {count:,} times in known breach data.\n\n"
                "Do not use this password for an account.",
            )
        else:
            messagebox.showinfo(
                "Breach Check",
                "No match was found in the Have I Been Pwned dataset.",
            )

    def clear(self):
        self.password_var.set("")
        self.password_entry.focus_set()

    def run(self):
        self.root.mainloop()
