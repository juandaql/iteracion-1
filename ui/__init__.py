
# ui/dashboard.py

import customtkinter as ctk

from storage.json_repository import load_data


class Dashboard(ctk.CTkFrame):
    """Panel de inicio de Autos Colombia."""

    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        self.grid_columnconfigure(
            (0, 1, 2, 3), weight=1, uniform="cards"
        )

        self.create_header()
        self.create_stat_cards()
        self.create_activity_section()

    def create_header(self):
        header = ctk.CTkFrame(
            self, fg_color="transparent"
        )
        header.grid(
            row=0, column=0, columnspan=4,
            sticky="ew", pady=(0, 24)
        )

        ctk.CTkLabel(
            header,
            text="Panel principal",
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color="#F3F4F6",
        ).pack(anchor="w")

        ctk.CTkLabel(
            header,
            text="Resumen general del parqueadero",
            font=ctk.CTkFont(size=13),
            text_color="#9CA3AF",
        ).pack(anchor="w", pady=(5, 0))

    def create_stat_cards(self):
        try:
            users = len(load_data("usuarios"))
            vehicles = len(load_data("vehiculos"))
            spaces = load_data("celdas")
            stays = load_data("estancias")

            occupied_spaces = sum(
                1 for space in spaces
                if space.get("estado") == "ocupada"
            )

            active_stays = sum(
                1 for stay in stays
                if stay.get("estado") == "activa"
            )

            stats = [
                ("Usuarios registrados", users, "#60A5FA"),
                ("Vehículos registrados", vehicles, "#A78BFA"),
                ("Celdas ocupadas", occupied_spaces, "#F87171"),
                ("Estancias activas", active_stays, "#34D399"),
            ]

        except (ValueError, OSError) as error:
            stats = [
                ("Usuarios registrados", "—", "#60A5FA"),
                ("Vehículos registrados", "—", "#A78BFA"),
                ("Celdas ocupadas", "—", "#F87171"),
                ("Estancias activas", "—", "#34D399"),
            ]
            print(f"Error al cargar indicadores: {error}")

        for column, (title, value, accent) in enumerate(stats):
            card = ctk.CTkFrame(
                self,
                fg_color="#1F2937",
                corner_radius=12,
                border_width=1,
                border_color="#374151",
            )
            card.grid(
                row=1,
                column=column,
                padx=(0 if column == 0 else 8, 0),
                sticky="nsew",
                pady=(0, 20),
            )

            ctk.CTkLabel(
                card,
                text=title,
                font=ctk.CTkFont(size=12),
                text_color="#9CA3AF",
                wraplength=145,
            ).pack(anchor="w", padx=16, pady=(18, 8))

            ctk.CTkLabel(
                card,
                text=str(value),
                font=ctk.CTkFont(size=30, weight="bold"),
                text_color=accent,
            ).pack(anchor="w", padx=16, pady=(0, 18))

    def create_activity_section(self):
        section = ctk.CTkFrame(
            self,
            fg_color="#1F2937",
            corner_radius=12,
            border_width=1,
            border_color="#374151",
        )
        section.grid(
            row=2, column=0, columnspan=4,
            sticky="nsew"
        )
        section.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            section,
            text="Actividad reciente",
            font=ctk.CTkFont(size=17, weight="bold"),
            text_color="#F3F4F6",
        ).grid(
            row=0, column=0,
            sticky="w", padx=20, pady=(20, 6)
        )

        ctk.CTkLabel(
            section,
            text=(
                "Los movimientos de entrada y salida "
                "aparecerán aquí cuando implementemos "
                "el módulo de estancias."
            ),
            font=ctk.CTkFont(size=13),
            text_color="#9CA3AF",
            wraplength=650,
            justify="left",
        ).grid(
            row=1, column=0,
            sticky="w", padx=20, pady=(4, 24)
        )
