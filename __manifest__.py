# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Practical Task",
    'version': '16.0.1.0.0',
    'summary': 'Practical Task',
    'author': 'Ramiz Belim',
    'sequence': 10,
    'description': """
Patient & Records """,
    'category': 'Accounting/Accounting',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['sale_management', 'mail'],
    'data': [
        'security/ir.model.access.csv',

        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
        'views/project_views.xml',
        'views/hr_employee_views.xml',
        'views/project_planning_line.xml'
    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
