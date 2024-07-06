from domain import Project

class Repository:
    def __init__(self):
        self._projects = []

    def add_project(self, project: Project):
        self._projects.append(project)

    def remove_project(self, project_name: str):
        self._projects = [project for project in self._projects if project.get_name() != project_name]

    def update_project(self, old_name: str, new_project: Project):
        for i, project in enumerate(self._projects):
            if project.get_name() == old_name:
                self._projects[i] = new_project
                break

    def add_contributor(self, project_name: str, contributor: str):
        for project in self._projects:
            if project.get_name() == project_name:
                project.add_contributor(contributor)
                break

    def remove_contributor(self, project_name: str, contributor: str):
        for project in self._projects:
            if project.get_name() == project_name:
                project.remove_contributor(contributor)
                break

    def get_projects(self):
        return self._projects