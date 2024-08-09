# Copyright 2024 Scalizer (<https://www.scalizer.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).
from odoo import fields, models, api
from odoo.tools import config


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    project_sequence = fields.Integer(compute='_compute_project_sequence')

    def _compute_project_sequence(self):
        for rec in self:
            if self.env.context.get('default_project_id'):
                project_id = self.env['project.project'].browse(self.env.context.get('default_project_id'))
                rec.project_sequence = project_id.ordered_type_ids.filtered(lambda x: x.type_id.id == rec.id).sequence
            else:
                rec.project_sequence = 0

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        project_id = None
        for i, condition in enumerate(domain):
            if isinstance(condition, list) and condition[0] == 'project_ids':
                project_id = self.env['project.project'].browse(condition[2])
                domain[i] = ['id', 'in', project_id.ordered_type_ids.type_id.ids]
        res = super(ProjectTaskType, self).search_read(domain=domain, fields=fields, offset=offset, limit=limit,
                                                       order=order)
        if project_id:
            for rec in res:
                ordered_type_id = project_id.ordered_type_ids.filtered(lambda x: x.type_id.id == rec['id'])
                rec['project_sequence'] = ordered_type_id.sequence
        res = sorted(res, key=lambda x: x['project_sequence'])

        return res

    def write(self, vals):
        if 'sequence' in vals and 'force_sequence' not in self.env.context and not config['test_enable']:
            vals.pop('sequence')
        res = super(ProjectTaskType, self).write(vals)
        return res

