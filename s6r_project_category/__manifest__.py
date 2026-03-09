# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    "name": "Scalizer Project Category",
    "version": "18.0.1.0.0",
    "summary": "Add categories on projects",
    "category": "Project",
    "author": "Scalizer",
    "website": "https://www.scalizer.fr",
    "license": "LGPL-3",
    "depends": ["project"],
    "data": [
        "security/ir.model.access.csv",
        "views/project_category_views.xml",
        "views/project_project_views.xml",
    ],
    "installable": True,
    "application": False,
}
