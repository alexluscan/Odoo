from domain import Project
from repository import Repository

class Service:
   def __init__(self, repo=Repository()):
        self.repo = repo

   def add_project(self, project: Project):
        self.repo.add_project(project)

   def remove_project(self, project_name: str):
        self.repo.remove_project(project_name)

   def update_project(self, old_name: str, new_project: Project):
        self.update_project(old_name, new_project)

   def add_contributor(self, project_name: str, contributor: str):
        self.add_contributor(project_name, contributor)

   def remove_contributor(self, project_name: str, contributor: str):
        self.remove_contributor(project_name, contributor)

   def get_projects(self):
        return self.repo.get_projects()


