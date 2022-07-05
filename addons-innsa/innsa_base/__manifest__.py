# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Innsa Base',
    'category': 'Innsa',
    'author': 'Huan Nguyen',
    'sequence': 500,
    'version': '1.0',
    'summary': '',
    'description':
        """
        =====================
        Innsa Base
        """,
    'depends': ['hr'],
    'data': [
        'security/innsa_security.xml',
        'security/ir.model.access.csv',
        'views/innsa_farm_views.xml',
        'views/innsa_planting_views.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
        ],
        'web.qunit_suite_tests': [
        ],
        'web.assets_qweb': [],
    },
    'license': 'LGPL-3',
}
