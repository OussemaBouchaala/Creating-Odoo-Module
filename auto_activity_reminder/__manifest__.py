{
    'name': 'Auto Activity Reminder',
    'version': '17.0.1.0',
    'category': 'Productivity',
    'summary': 'Crée automatiquement une activité "Appel" pour les contacts',
    'author': 'Oussema Soft',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron.xml',
    ],
}
