# _*_ config: utf-8 _*_

{
    'name': 'Odoo Academy',
    'summary': """Academy app to manage training""",
    'description': """
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees
    """,
    'author': 'Carlos Garafulic',
    'website': 'https://www.clingdata.com',
    'license': 'LGPL-3',
    'category': 'Training',
    'version': '0.1.0',
    'depends': ['sale'],
    'data': ['security/academy_security.xml',
             'security/ir.model.access.csv',
             'views/academy_menu_items.xml',
             'views/course_views.xml',
             'views/session_views.xml',
             'views/sale_views_inherit.xml',
             'views/product_views_inherit.xml',
             'wizard/sale_wizard_view.xml',
             'report/session_report_templates.xml'
             ],
    'demo': ['demo/academy_demo.xml']
}
