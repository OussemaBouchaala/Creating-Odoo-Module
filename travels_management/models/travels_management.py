from odoo import fields, models

class TravelsManagement(models.Model):
    _name = 'travels.management'
    _description = 'Travels Management'


    booking_reference = fields.Char(string='Booking reference',
                                    readonty=True,
                                    )
    partner_id=fields.Many2one('res.partner', required=True)
    product_id = fields.Many2one('product.template')
    company_id = fields.Many2one('res.company')
    no_of_passengers = fields.Integer("No of Passengers", default="2")
    booking_date = fields.Date("Booking Date", )
    state = fields.Selection(
        selection=[
            ('draft', "Draft"),
            ('confirmed', "Confirmed"),
        ],
        string = "Status",
        readonty = True,
        tracking = True,
        default = 'draft')