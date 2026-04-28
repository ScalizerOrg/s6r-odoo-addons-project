# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

from random import randint

from odoo import fields, models


class ProjectRole(models.Model):
    """Add missing fields expected by Odoo 19 core views to the OCA
    ``project.role`` model.

    Odoo 19 core defines ``project.role`` with ``color`` and ``sequence``
    fields used in list, kanban and task views.  The OCA ``project_role``
    module redefines the same model without those fields, causing the core
    views to crash.  This bridge adds them so both sets of views work.
    """

    _inherit = "project.role"

    def _default_color(self):
        return randint(1, 11)

    color = fields.Integer(string="Color", default=_default_color)
    sequence = fields.Integer(string="Sequence", default=10)
