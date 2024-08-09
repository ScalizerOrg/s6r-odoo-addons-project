# Copyright 2024 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': 'Scalizer Project Stage Sequence',
    'version': '17.0.1.0.0',
    'author': 'Scalizer',
    'website': 'https://www.scalizer.fr',
    'summary': "Define a sequence for stages of each project",
    'sequence': 0,
    'license': 'AGPL-3',
    'depends': [
        'project',
        'project_task_default_stage',
    ],
    'category': 'Generic Modules/Scalizer',
    'complexity': 'easy',
    'description': '''
This module allows you to define a sequence of stages for each project.
    ''',
    'qweb': [
    ],
    'demo': [
    ],
    'images': [
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/project_views.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
}
