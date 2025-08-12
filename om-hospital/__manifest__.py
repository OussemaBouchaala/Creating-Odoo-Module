{
    'name' : 'Hospital Management System',
    'author' : 'Oussema Bouchaala',
    'description' : 'Hospital Management System',
    'license' : 'LGPL-3',
    'category' : 'Hospital',
    'version' : '1.0.0',
    'depends' : [
        'mail'
    ],
    'data': [
        "security/ir.model.access.csv",
        "views/patient_views_readonly.xml",
        "views/patient_views.xml",
        "views/menu.xml",
    ]
}