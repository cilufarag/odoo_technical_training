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
    'depends': ['base'],
    'data': ['security/academy_security.xml', 
             'security/ir.model.access.csv',
             'views/academy_menu_items.xml'],
    'demo': []
}