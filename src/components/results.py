import customtkinter as ctk


class ResultsPanel:
    def __init__(self, parent):
        self.frame = ctk.CTkFrame(parent, corner_radius=14)
        self.frame.pack(fill="both", expand=True, padx=30, pady=10)

        metrics = ctk.CTkFrame(self.frame, fg_color="transparent")
        metrics.pack(fill="x", padx=15, pady=(15, 8))

        self.entropy = self._metric(metrics, "Entropy", 0)
        self.crack = self._metric(metrics, "Offline Crack Estimate", 1)

        columns = ctk.CTkFrame(self.frame, fg_color="transparent")
        columns.pack(fill="both", expand=True, padx=15, pady=(5, 15))

        checks_frame = ctk.CTkFrame(columns, corner_radius=10)
        checks_frame.pack(side="left", fill="both", expand=True, padx=(0, 6))

        tips_frame = ctk.CTkFrame(columns, corner_radius=10)
        tips_frame.pack(side="right", fill="both", expand=True, padx=(6, 0))

        ctk.CTkLabel(
            checks_frame, text="Security Checks",
            font=("Segoe UI", 14, "bold")
        ).pack(anchor="w", padx=15, pady=(12, 5))

        ctk.CTkLabel(
            tips_frame, text="Recommendations",
            font=("Segoe UI", 14, "bold")
        ).pack(anchor="w", padx=15, pady=(12, 5))

        self.checks_box = ctk.CTkTextbox(checks_frame, height=180)
        self.checks_box.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.tips_box = ctk.CTkTextbox(tips_frame, height=180)
        self.tips_box.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    @staticmethod
    def _metric(parent, title, column):
        frame = ctk.CTkFrame(parent, corner_radius=10)
        frame.grid(row=0, column=column, sticky="ew", padx=5)
        parent.grid_columnconfigure(column, weight=1)

        ctk.CTkLabel(
            frame, text=title,
            text_color="#9aa4b2",
            font=("Segoe UI", 11),
        ).pack(anchor="w", padx=12, pady=(10, 2))

        value = ctk.CTkLabel(
            frame, text="—",
            font=("Segoe UI", 13, "bold"),
        )
        value.pack(anchor="w", padx=12, pady=(0, 10))

        return value

    def update(self, result):
        self.entropy.configure(text=f"{result.entropy:.1f} bits")
        self.crack.configure(text=result.crack_time)

        self.checks_box.configure(state="normal")
        self.checks_box.delete("1.0", "end")
        for check in result.checks:
            icon = "✓" if check.passed else "✗"
            self.checks_box.insert("end", f"{icon}  {check.name}\n")
        self.checks_box.configure(state="disabled")

        self.tips_box.configure(state="normal")
        self.tips_box.delete("1.0", "end")
        for tip in result.recommendations:
            self.tips_box.insert("end", f"•  {tip}\n\n")
        self.tips_box.configure(state="disabled")
