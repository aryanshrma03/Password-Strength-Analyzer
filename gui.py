import customtkinter as ctk

from checker import (
    check_password_strength,
    generate_secure_password,
    check_data_breach
)

# Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class PasswordCheckerApp:
    def __init__(self):
        self.root = ctk.CTk()

        self.root.title("Password Strength Checker")
        self.root.geometry("750x620")
        self.root.resizable(False, False)

        # Title
        self.title = ctk.CTkLabel(
            self.root,
            text="🔐 Password Strength Checker",
            font=("Segoe UI", 30, "bold")
        )
        self.title.pack(pady=(30, 10))

        # Subtitle
        self.subtitle = ctk.CTkLabel(
            self.root,
            text="Analyze Password Security Using Python",
            font=("Segoe UI", 14),
            text_color="gray"
        )
        self.subtitle.pack(pady=(0, 20))

        # Password Entry
        self.password_entry = ctk.CTkEntry(
            self.root,
            width=450,
            height=45,
            show="*",
            placeholder_text="Enter Password...",
            font=("Segoe UI", 14),
            corner_radius=12
        )
        self.password_entry.pack(pady=10)

        # Show Password Checkbox
        self.show_var = ctk.BooleanVar()

        self.show_checkbox = ctk.CTkCheckBox(
            self.root,
            text="Show Password",
            variable=self.show_var,
            command=self.toggle_password
        )
        self.show_checkbox.pack(pady=5)

        # Check Button
        self.check_button = ctk.CTkButton(
            self.root,
            text="Check Password Strength",
            command=self.check_strength,
            width=260,
            height=50,
            font=("Segoe UI", 16, "bold"),
            corner_radius=12
        )
        self.check_button.pack(pady=15)

        # Generate Password Button
        self.generate_button = ctk.CTkButton(
            self.root,
            text="Generate Secure Password",
            command=self.generate_password,
            width=260,
            height=50,
            font=("Segoe UI", 16, "bold"),
            fg_color="#4444ff",
            hover_color="#2222aa",
            corner_radius=12
        )
        self.generate_button.pack(pady=10)

        # Result Label
        self.result_label = ctk.CTkLabel(
            self.root,
            text="",
            font=("Segoe UI", 24, "bold")
        )
        self.result_label.pack(pady=10)

        # Feedback Box
        self.feedback_box = ctk.CTkTextbox(
            self.root,
            width=580,
            height=180,
            font=("Segoe UI", 13),
            corner_radius=12
        )
        self.feedback_box.pack(pady=15)

        # Footer
        self.footer = ctk.CTkLabel(
            self.root,
            text="Developed by Aryan Sharma",
            text_color="gray",
            font=("Segoe UI", 12, "bold")
        )
        self.footer.pack(side="bottom", pady=15)

    # Toggle Password Visibility
    def toggle_password(self):
        if self.show_var.get():
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")

    # Generate Secure Password
    def generate_password(self):
        password = generate_secure_password()

        self.password_entry.delete(0, "end")
        self.password_entry.insert(0, password)

        self.result_label.configure(
            text="Secure Password Generated",
            text_color="cyan"
        )

    # Check Password Strength
    def check_strength(self):
        password = self.password_entry.get()

        if not password:
            self.result_label.configure(
                text="Please enter a password.",
                text_color="red"
            )
            return

        strength, color, feedback = check_password_strength(password)

        self.result_label.configure(
            text=f"Password Strength: {strength}",
            text_color=color
        )

        self.feedback_box.delete("1.0", "end")

        # Feedback Messages
        if feedback:
            for item in feedback:
                self.feedback_box.insert(
                    "end",
                    f"• {item}\n"
                )
        else:
            self.feedback_box.insert(
                "end",
                "✅ Excellent! Your password is secure.\n"
            )

        # Data Breach Check
        breach_count = check_data_breach(password)

        if breach_count:
            self.feedback_box.insert(
                "end",
                f"\n⚠ WARNING: Password found in {breach_count} data breaches!\n"
            )
        else:
            self.feedback_box.insert(
                "end",
                "\n✅ Password not found in known data breaches.\n"
            )

    # Run App
    def run(self):
        self.root.mainloop()