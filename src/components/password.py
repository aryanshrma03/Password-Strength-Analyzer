import customtkinter as ctk


def create_password_input(parent, variable, on_change, on_toggle):
    frame = ctk.CTkFrame(parent, fg_color="transparent")
    frame.pack(fill="x", padx=30, pady=(10, 5))

    entry = ctk.CTkEntry(
        frame,
        textvariable=variable,
        width=600,
        height=48,
        show="*",
        font=("Segoe UI", 15),
        corner_radius=12,
        placeholder_text="Enter a password to analyze...",
    )
    entry.pack(side="left", fill="x", expand=True)
    entry.bind("<KeyRelease>", on_change)

    show_var = ctk.BooleanVar(value=False)

    checkbox = ctk.CTkCheckBox(
        frame,
        text="Show",
        variable=show_var,
        command=lambda: on_toggle(entry, show_var),
        font=("Segoe UI", 12),
    )
    checkbox.pack(side="right", padx=(12, 0))

    return entry, show_var


def toggle_password(entry, variable):
    entry.configure(show="" if variable.get() else "*")
