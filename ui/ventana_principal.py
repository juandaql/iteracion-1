
# ui/ventana_principal.py

import customtkinter as ctk

from ui.dashboard import Dashboard


class VentanaPrincipal(ctk.CTk):
    """Ventana principal de Autos Colombia."""

    BG = "#111827"
    SIDEBAR = "#0B1220"
    PANEL = "#1F2937"
    BORDER = "#374151"
    TEXT = "#F3F4F6"
    MUTED = "#9CA3AF"
    ACCENT = "#2563EB"

    def __init__(self):
        super().__init__()

        self.title("Autos Colombia | Gestión de parqueadero")
        self.geometry("1180x720")
        self.minsize(900, 600)
        self.configure(fg_color=self.BG)

        self.current_view = "Panel principal"

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()
        self.create_main_area()
        self.show_view("Panel principal")

    def create_sidebar(self):
        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0,
            fg_color=self.SIDEBAR,
        )
        self.sidebar.grid(
            row=0, column=0, sticky="nsew"
        )
        self.sidebar.grid_propagate(False)
        self.sidebar.grid_columnconfigure(0, weight=1)

        # Identidad del sistema
        brand = ctk.CTkFrame(
            self.sidebar, fg_color="transparent"
        )
        brand.grid(
            row=0, column=0,
            sticky="ew", padx=18, pady=(28, 30)
        )

        ctk.CTkLabel(
            brand,
            text="AC",
            width=42,
            height=42,
            corner_radius=10,
            fg_color=self.ACCENT,
            text_color="#FFFFFF",
            font=ctk.CTkFont(size=18, weight="bold"),
        ).pack(side="left", padx=(0, 10))

        brand_text = ctk.CTkFrame(
            brand, fg_color="transparent"
        )
        brand_text.pack(side="left", fill="y")

        ctk.CTkLabel(
            brand_text,
            text="AUTOS",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.TEXT,
        ).pack(anchor="w")

        ctk.CTkLabel(
            brand_text,
            text="COLOMBIA",
            font=ctk.CTkFont(size=10, weight="bold"),
            text_color=self.MUTED,
        ).pack(anchor="w")

        ctk.CTkLabel(
            self.sidebar,
            text="MENÚ PRINCIPAL",
            font=ctk.CTkFont(size=10, weight="bold"),
            text_color="#6B7280",
        ).grid(
            row=1, column=0,
            sticky="w", padx=20, pady=(0, 10)
        )

        self.nav_buttons = {}

        menu_items = [
            "Panel principal",
            "Usuarios",
            "Vehículos",
            "Celdas",
            "Entradas y salidas",
            "Historial",
            "Novedades",
        ]

        for index, name in enumerate(menu_items, start=2):
            button = ctk.CTkButton(
                self.sidebar,
                text=name,
                anchor="w",
                height=42,
                corner_radius=8,
                fg_color="transparent",
                hover_color="#1F2937",
                text_color=self.MUTED,
                font=ctk.CTkFont(size=13),
                command=lambda view=name: self.show_view(view),
            )
            button.grid(
                row=index, column=0,
                sticky="ew", padx=12, pady=3
            )

            self.nav_buttons[name] = button

        # Información al pie del menú
        footer = ctk.CTkFrame(
            self.sidebar,
            fg_color="transparent",
        )
        footer.grid(
            row=20, column=0,
            sticky="ew", padx=18, pady=20
        )

        ctk.CTkFrame(
            footer,
            height=1,
            fg_color=self.BORDER,
        ).pack(fill="x", pady=(0, 14))

        ctk.CTkLabel(
            footer,
            text="Sistema local",
            font=ctk.CTkFont(size=12),
            text_color=self.TEXT,
        ).pack(anchor="w")

        ctk.CTkLabel(
            footer,
            text="Versión inicial 1.0",
            font=ctk.CTkFont(size=10),
            text_color=self.MUTED,
        ).pack(anchor="w", pady=(4, 0))

    def create_main_area(self):
        self.main_area = ctk.CTkFrame(
            self,
            fg_color=self.BG,
            corner_radius=0,
        )
        self.main_area.grid(
            row=0, column=1, sticky="nsew"
        )
        self.main_area.grid_columnconfigure(0, weight=1)
        self.main_area.grid_rowconfigure(1, weight=1)

        # Barra superior
        self.topbar = ctk.CTkFrame(
            self.main_area,
            height=70,
            corner_radius=0,
            fg_color=self.BG,
        )
        self.topbar.grid(
            row=0, column=0, sticky="ew"
        )
        self.topbar.grid_columnconfigure(0, weight=1)
        self.topbar.grid_propagate(False)

        self.page_title = ctk.CTkLabel(
            self.topbar,
            text="Panel principal",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=self.TEXT,
        )
        self.page_title.grid(
            row=0, column=0,
            sticky="w", padx=28, pady=22
        )

        ctk.CTkLabel(
            self.topbar,
            text="Autos Colombia",
            font=ctk.CTkFont(size=12),
            text_color=self.MUTED,
        ).grid(
            row=0, column=1,
            sticky="e", padx=28
        )

        # Área donde se dibujan las pantallas
        self.content_frame = ctk.CTkFrame(
            self.main_area,
            fg_color=self.BG,
            corner_radius=0,
        )
        self.content_frame.grid(
            row=1, column=0,
            sticky="nsew", padx=28, pady=(12, 28)
        )
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

    def show_view(self, view_name):
        """Muestra una pantalla y actualiza el menú activo."""
        self.current_view = view_name
        self.page_title.configure(text=view_name)

        for name, button in self.nav_buttons.items():
            if name == view_name:
                button.configure(
                    fg_color=self.ACCENT,
                    text_color="#FFFFFF",
                    hover_color="#1D4ED8",
                )
            else:
                button.configure(
                    fg_color="transparent",
                    text_color=self.MUTED,
                    hover_color=self.PANEL,
                )

        for widget in self.content_frame.winfo_children():
            widget.destroy()

        if view_name == "Panel principal":
            page = Dashboard(self.content_frame)
            page.grid(
                row=0, column=0,
                sticky="nsew"
            )
            return

        # Pantallas temporales: se implementarán por etapas.
        placeholder = ctk.CTkFrame(
            self.content_frame,
            fg_color=self.PANEL,
            corner_radius=12,
        )
        placeholder.grid(
            row=0, column=0,
            sticky="nsew"
        )

        ctk.CTkLabel(
            placeholder,
            text=view_name,
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=self.TEXT,
        ).pack(
            anchor="w", padx=28, pady=(30, 10)
        )

        ctk.CTkLabel(
            placeholder,
            text=(
                "Esta pantalla se desarrollará en una "
                "siguiente etapa del proyecto."
            ),
            font=ctk.CTkFont(size=13),
            text_color=self.MUTED,
            wraplength=500,
        ).pack(
            anchor="w", padx=28, pady=(0, 25)
        )
