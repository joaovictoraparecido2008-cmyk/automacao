import customtkinter as ctk
import tkinter as tk

from apps_automatizados.youtube import youtube
from apps_automatizados.spotfy import pesquisar_musica
from apps_automatizados.programas import navegador, calculadora, arquivos


# ============================================================
# CONFIGURAÇÃO
# ============================================================

ctk.set_appearance_mode("dark")

BG = "#070708"
PANEL = "#0e0e11"
PANEL_2 = "#141418"
BORDER = "#29292f"
TEXT = "#f2f2f2"
MUTED = "#777780"
RED = "#c9182b"
RED_HOVER = "#e1263c"
RED_DARK = "#421018"
SUCCESS = "#43d17a"


class MiniAutomacao(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Automação PC")
        self.geometry("360x205")
        self.resizable(False, False)
        self.overrideredirect(True)
        self.attributes("-topmost", True)

        self.drag_x = 0
        self.drag_y = 0

        # Janela
        self.container = ctk.CTkFrame(
            self,
            corner_radius=22,
            fg_color=PANEL,
            border_width=1,
            border_color=BORDER
        )
        self.container.pack(fill="both", expand=True)

        # ====================================================
        # TOPO
        # ====================================================

        self.header = ctk.CTkFrame(
            self.container,
            height=42,
            corner_radius=0,
            fg_color="transparent"
        )
        self.header.pack(fill="x", padx=12, pady=(8, 0))
        self.header.pack_propagate(False)

        self.logo = ctk.CTkLabel(
            self.header,
            text="●  AUTOMACÃO",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=TEXT
        )
        self.logo.pack(side="left", padx=4)

        self.online = ctk.CTkLabel(
            self.header,
            text="ONLINE",
            font=ctk.CTkFont(size=8, weight="bold"),
            text_color=RED
        )
        self.online.pack(side="left", padx=8)

        # Apenas um X discreto para fechar.
        # Não existem botões de menu.
        self.close = ctk.CTkLabel(
            self.header,
            text="×",
            font=ctk.CTkFont(size=20),
            text_color=MUTED,
            cursor="hand2"
        )
        self.close.pack(side="right", padx=5)
        self.close.bind("<Button-1>", lambda e: self.destroy())

        # ====================================================
        # CAMPO DE COMANDO
        # ====================================================

        self.command_frame = ctk.CTkFrame(
            self.container,
            height=48,
            fg_color=PANEL_2,
            corner_radius=14,
            border_width=1,
            border_color=BORDER
        )
        self.command_frame.pack(fill="x", padx=14, pady=(8, 7))
        self.command_frame.pack_propagate(False)

        self.entrada = ctk.CTkEntry(
            self.command_frame,
            height=42,
            border_width=0,
            fg_color="transparent",
            text_color=TEXT,
            placeholder_text="Digite um comando...",
            placeholder_text_color="#5e5e67",
            font=ctk.CTkFont(size=12)
        )
        self.entrada.pack(side="left", fill="x", expand=True, padx=(12, 4))
        self.entrada.bind("<Return>", lambda e: self.processar())

        # ====================================================
        # MICROFONE
        # ====================================================

        self.mic = ctk.CTkLabel(
            self.command_frame,
            text="●",
            width=36,
            font=ctk.CTkFont(size=20),
            text_color=RED,
            cursor="hand2"
        )
        self.mic.pack(side="right", padx=(2, 8))

        self.mic.bind("<Button-1>", self.microfone)
        self.mic.bind("<Enter>", lambda e: self.mic.configure(text_color=RED_HOVER))
        self.mic.bind("<Leave>", lambda e: self.mic.configure(text_color=RED))

        # ====================================================
        # STATUS
        # ====================================================

        self.status = ctk.CTkLabel(
            self.container,
            text="●  Pronto  •  digite um comando",
            text_color=MUTED,
            font=ctk.CTkFont(size=10)
        )
        self.status.pack(anchor="w", padx=18, pady=(0, 2))

        self.hint = ctk.CTkLabel(
            self.container,
            text="youtube  •  spotify  •  navegador  •  calculadora  •  arquivos",
            text_color="#484851",
            font=ctk.CTkFont(size=9)
        )
        self.hint.pack(anchor="w", padx=18, pady=(0, 12))

        # Arrastar pelo topo
        for widget in (self.header, self.logo, self.online):
            widget.bind("<Button-1>", self.iniciar_arraste)
            widget.bind("<B1-Motion>", self.arrastar)

        self.after(100, self.posicionar)

    # ========================================================
    # POSIÇÃO
    # ========================================================

    def posicionar(self):
        largura = self.winfo_width()
        altura = self.winfo_height()

        x = self.winfo_screenwidth() - largura - 24
        y = self.winfo_screenheight() - altura - 55

        self.geometry(f"{largura}x{altura}+{x}+{y}")

    # ========================================================
    # ARRASTAR
    # ========================================================

    def iniciar_arraste(self, event):
        self.drag_x = event.x
        self.drag_y = event.y

    def arrastar(self, event):
        x = self.winfo_x() + event.x - self.drag_x
        y = self.winfo_y() + event.y - self.drag_y
        self.geometry(f"+{x}+{y}")

    # ========================================================
    # COMANDO
    # ========================================================

    def processar(self):
        comando = self.entrada.get().strip().lower()

        if not comando:
            return

        comandos = {
            "youtube": youtube,
            "yt": youtube,
            "spotify": pesquisar_musica,
            "sp": pesquisar_musica,
            "navegador": navegador,
            "opera": navegador,
            "calculadora": calculadora,
            "calc": calculadora,
            "arquivos": arquivos,
            "explorador": arquivos,
        }

        if comando not in comandos:
            self.status.configure(
                text="●  Comando não encontrado",
                text_color="#d98b8b"
            )
            self.entrada.delete(0, "end")
            return

        self.status.configure(
            text=f"●  Executando  •  {comando}",
            text_color=RED
        )
        self.update_idletasks()

        try:
            comandos[comando]()
            self.status.configure(
                text=f"●  Concluído  •  {comando}",
                text_color=SUCCESS
            )
        except Exception as erro:
            self.status.configure(
                text="●  Erro ao executar",
                text_color="#ff6577"
            )
            print(f"[ERRO] {erro}")

        self.entrada.delete(0, "end")

    # ========================================================
    # MICROFONE
    # ========================================================

    def microfone(self, event=None):
        # Por enquanto o microfone é visual.
        # Depois podemos conectar SpeechRecognition/Whisper.
        self.status.configure(
            text="●  Microfone selecionado • ainda não configurado",
            text_color=RED
        )


if __name__ == "__main__":
    app = MiniAutomacao()
    app.mainloop()
