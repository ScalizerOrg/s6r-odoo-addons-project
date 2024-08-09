# Copyright 2024 Scalizer (<https://www.scalizer.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).
from odoo import fields, models, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        stage_ids = super()._read_group_stage_ids(stages, domain, order)
        if self.env.context.get('default_project_id') and len(self.env.context.get('active_ids', [])) == 1:
            stage_ids = stage_ids.sorted(key=lambda x: x.project_sequence)
        return stage_ids
