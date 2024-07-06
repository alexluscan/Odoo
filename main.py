from ui import UI
from domain import Project
from service import Service

Projects = [Project("proj1", "url", 10, ['c1', 'c2'])]

ui = UI(Projects, Service())

ui.display_project_details()