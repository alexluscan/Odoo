from odoo import models, fields
from odoo.fields import Command


class Project:
    def __init__(self, name, url, rating, contributors=[]):
        name = fields.Char(string='Project name')
        contributors = fields.Many2many('project', string='Contributors')
        self.name = name
        self.url = url
        self.rating = rating
        self.contributors = contributors

    def set_url(self, url):
        self.url = url

    def set_rating(self, rating):
        self.rating = rating

    def get_name(self):
        return self.name

    def get_url(self):
        return self.url

    def get_rating(self):
        return self.rating

    def get_contributors(self):
        return self.contributors


class Contributor:
    def __init__(self, name, projects):
        name = fields.Char(string='Contributor name')
        projects = fields.Many2many('contributor', string='Projects')
        self.name = name
        self.project = projects

    def get_name(self):
        return self.name

    def get_project(self):
        return self.project
