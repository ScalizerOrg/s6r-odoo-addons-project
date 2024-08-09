# Copyright 2024 Scalizer (<https://www.scalizer.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).
from odoo import fields, models, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    ordered_type_ids = fields.One2many('project.task.type.sequence', 'project_id', string='Ordered Types',
                                       compute='_compute_ordered_type_ids', store=True, readonly=False)

    def write(self, vals):
        res = super(ProjectProject, self).write(vals)
        if 'ordered_type_ids' in vals:
            for project in self:
                project._compute_type_ids()
        return res

    def web_read(self, specification):
        if self._name == 'project.project' and len(self) == 1:
            self = self.with_context(project_id=self.id)
        return super(ProjectProject, self).web_read(specification)

    @api.depends('type_ids')
    def _compute_ordered_type_ids(self):
        if self.env.context.get('compute_type_ids'):
            return
        for project in self:
            if isinstance(project.id, models.NewId):
                continue
            for type_id in project.type_ids:
                if type_id.ids[0] not in project.ordered_type_ids.type_id.ids:
                    self.env['project.task.type.sequence'].create({'project_id': project.ids[0],
                                                                   'type_id': type_id.ids[0],
                                                                   'sequence': type_id.sequence})
            for ordered_type_id in project.ordered_type_ids:
                if ordered_type_id.type_id.ids[0] not in project.type_ids.ids:
                    project.write({'ordered_type_ids': [(2, ordered_type_id.id)]})

    def _compute_type_ids(self):
        for project in self:
            for type_id in project.ordered_type_ids.type_id:
                if type_id.ids[0] not in project.type_ids.ids:
                    project.write({'type_ids': [(4, type_id.id)]})

            for type_id in project.type_ids:
                if type_id.ids[0] not in project.ordered_type_ids.type_id.ids:
                    project.with_context(compute_type_ids=True).write({'type_ids': [(3, type_id.id)]})
