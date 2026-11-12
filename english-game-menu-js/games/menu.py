import os
import tkinter as tk
from tkinter import messagebox
import webbrowser
from threading import Thread
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

class GameMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Menu")
        self.create_menu()

    def create_menu(self):
        # Dictionnaire des jeux
        games = {
            "BrickBreaker": "brickbreaker/index.html",
            "Snake": "snake/main.py",
            "Pacman": "pacman/pac-man.py",
            "Minesweeper": "minesweeper/Demineur.py"


        }
        # Créer les boutons pour chaque jeu
        for game_name, game_path in games.items():
            button = tk.Button(self.root, text=game_name, command=lambda p=game_path: self.launch_game(p))
            button.pack(pady=5)

    def launch_game(self, game_path):
        if game_path.endswith(".html"):  # Si c'est un projet web
            self.launch_web_game(game_path)
        else:
            try:
                os.system(f'python "{game_path}"')
            except Exception as e:
                messagebox.showerror("Error", f"Failed to launch {game_path}: {e}")

    def launch_web_game(self, html_file):
        def start_server():
            # Démarre un serveur HTTP pour servir le fichier HTML
            directory = os.path.dirname(html_file)
            os.chdir(directory)
            with TCPServer(("localhost", 8000), SimpleHTTPRequestHandler) as httpd:
                print("Serving at port 8000")
                httpd.serve_forever()

        # Démarre le serveur HTTP dans un thread séparé
        server_thread = Thread(target=start_server, daemon=True)
        server_thread.start()

        # Ouvre le fichier HTML dans un navigateur web
        webbrowser.open("http://localhost:8000/" + os.path.basename(html_file))

if __name__ == "__main__":
    root = tk.Tk()
    app = GameMenu(root)
    root.mainloop()
