# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    category_id = fields.Many2one(
        "project.category",
        string="Category",
        ondelete="set null",
        index=True,
    )
