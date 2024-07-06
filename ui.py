from domain import Project
from service import Service
import tkinter as tk
from tkinter import ttk

projects = [
    Project("Project1", "http://one.example.com", 9),
    Project("Project2", "http://two.example.com", 8),
    Project("Project3", "http://three.example.com", 10)
]

class ProjectApp:
    def __init__(self, root, service = Service()):
        self.root = root
        self.root.title("Project Viewer")
        self.service = service

        # Setting up the frame
        frame = tk.Frame(root)
        frame.pack(fill=tk.BOTH, expand=True)

        # Adding a treeview widget
        self.tree = ttk.Treeview(frame, columns=('Name', 'URL', 'Rating'), show='headings')
        self.tree.heading('Name', text='Name')
        self.tree.heading('URL', text='URL')
        self.tree.heading('Rating', text='Rating')

        # Adding scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Adding projects to the treeview
        for project in projects:
            self.tree.insert('', tk.END, values=(project.name, project.url, project.rating))

root = tk.Tk()
app = ProjectApp(root)
root.geometry('600x400')
root.mainloop()