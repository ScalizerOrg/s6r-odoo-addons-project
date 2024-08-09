# Copyright 2024 Scalizer (<https://www.scalizer.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).
from odoo import fields, models


class ProjectTaskTypeSequence(models.Model):
    _name = 'project.task.type.sequence'
    _description = 'Project Task Type Sequence'

    _order = 'project_id, sequence, id'

    sequence = fields.Integer(default=50)
    project_id = fields.Many2one('project.project', string='Project')
    type_id = fields.Many2one('project.task.type', string='Stage')
    name = fields.Char(related='type_id.name')
    fold = fields.Boolean(related='type_id.fold')
