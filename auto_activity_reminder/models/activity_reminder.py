from odoo import models, fields, api
from datetime import datetime, timedelta


class ActivityReminder(models.Model):
    _name = 'auto.activity.reminder'
    _description = 'Rappel automatique pour activités'

    def send_reminder(self):
        partners_to_treat = self.env['res.partner'].search([('date', '=', fields.Date.today())])
        for partner in partners_to_treat:
            event = self.env['calendar.event'].create({'user_id': partner.user_id.id,
                                                       'start': datetime.now(),
                                                       'stop': datetime.now() + timedelta(hours=1),
                                                       'duration': 1,
                                                       'name': 'Appel suite à la création du contact',
                                                       'res_model': 'res.partner',
                                                       'res_model_id': 85})
            event.write({'create_uid': partner.user_id.id,
                         'partner_ids': [partner.id]})
            for attendee in event.attendee_ids:
                if attendee.partner_id.id == 2:
                    attendee.write({'partner_id': 3,
                                    'common_name': 'Administrator'})
                    break

            partner.date = False
