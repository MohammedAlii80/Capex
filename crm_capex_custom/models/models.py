from odoo import api, fields, models,_

class capexcontact(models.Model):
    _inherit = 'crm.lead'

    contact_name = fields.Char(
        'Applicant Full Name', tracking=30,
        compute='_compute_contact_name', readonly=False, store=True)


    new_field_mobile = fields.Integer(string="Mobile", required=False, )
    second_rm = fields.Many2one(comodel_name="hr.employee", string="Second Rm", required=False, )

    date = fields.Date(string="Date", required=False, )

    area_area = fields.Many2one(comodel_name="res.city", string="Area", required=False, )
    deal_amount = fields.Float(string='Deal Amount', tracking=True)
    deal_status = fields.Selection(string="Deal Status", selection=[('current', 'Current'), ('new', 'New'), ], required=False, )
    Investments_in_millions = fields.Float(string='Investments In Millions', tracking=True)
    start_of_production = fields.Date(string="Start Of Production", required=False, )
    tax_tax = fields.Binary(string="Tax", required=True)
    company_type = fields.Selection(string="Company Type", selection=[('One-person company (OPC)', 'One-person company (OPC)'), ('Limited laibility company(LLC)', 'Limited laibility company(LLC)'),
                                                                      ('A company limited by shares','A company limited by shares'),
                                                                      ('joint-stock company','joint-stock company'),
                                                                      ('Partnership company','Partnership company'),
                                                                      ('Limited Partnership company','Limited Partnership company'),
                                                                      ('Sole proprietorsip','Sole proprietorsip'),
                                                                      ], required=False, )
    year_business = fields.Selection(string="Year in business", selection=[('1-2years', '1-2years'),
                                                                           ('3-5Years','3-5Years'),
                                                                           ('5-10years','5-10years'),
                                                                           ('10+years', '10+years'), ], required=False, )

    industry_id = fields.Many2one(comodel_name="res.partner.industry", string="Company Industry")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", required=False, )
    sales_turn_over= fields.Selection(string="Sales Turn Over", selection=[('Below EGP 5 M', 'Below EGP 5 M'),
                                                   ('From EGP 5 M to EGP 10 M', 'From EGP 5 M to EGP 10 M'),
                                                   ('From EGP 20 M to EGP 30 M', 'From EGP 20 M to EGP 30 M'),
                                                   ('From EGP30M to 40M', 'From EGP30M to 40M'),
                                                   ('From EGP40M to 50M', 'From EGP40M to 50M'),
                                                   ('From EGP 50M to 100', 'From EGP 50M to 100'),
                                                   ('From EGP 100 to 200 M', 'From EGP 100 to 200 M'),
                                                   ('More than EGP 200 ', 'More than EGP 200 '),
                                                   ], required=False, )
