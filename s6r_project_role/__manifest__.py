# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).
{
    "name": "S6R Project Role Bridge",
    "version": "19.0.1.0.0",
    "author": "Scalizer",
    "website": "https://www.scalizer.fr",
    "summary": "Bridge between OCA project_role and Odoo 19 core project.role",
    "license": "LGPL-3",
    "depends": ["project_role"],
    "category": "Project",
    "data": [
        "views/project_role_views.xml",
    ],
    "auto_install": True,
    "installable": True,
    "application": False,
}
