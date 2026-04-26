import os
import time
from rich.panel import Panel
from rich.console import Console

console = Console()

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")