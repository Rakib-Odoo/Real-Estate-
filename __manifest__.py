{
    'name': 'Real Estate',
    'version': '15.0.1.1.1',
    'description': 'Real estate module to show available properties',
    'author': 'Rakib Hasan',
    'category': 'Sales',
    'sequence': 1,
    'depends': [],
    'data': [
        # security files
        'security/ir.model.access.csv',


        #views tables
        'views/property_view.xml',

        # views file
        'views/meun_items.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,

}