# Copyright 2024 Scalizer (<https://www.scalizer.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).

from . import models

def compute_ordered_type_ids(env):
    project_ids = env['project.project'].search([])
    for project_id in project_ids:
        project_id._compute_ordered_type_ids()
