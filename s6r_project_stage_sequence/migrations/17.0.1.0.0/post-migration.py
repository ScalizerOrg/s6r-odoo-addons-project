# Copyright 2024 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

import logging
from odoo import api, SUPERUSER_ID
_logger = logging.getLogger(__name__)


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    project_ids = env['project.project'].search([])
    for project_id in project_ids:
        project_id._compute_ordered_type_ids()
