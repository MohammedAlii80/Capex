from odoo import api, fields, models,_

class capexcontact(models.Model):
    _inherit = 'crm.lead'

    contact_name = fields.Char(
        'Applicant Full Name', tracking=30,
        compute='_compute_contact_name', readonly=False, store=True)

    serial_number = fields.Text(string="serial number", required=False, )
    date = fields.Date(string="Date", required=False, )

    area_id = fields.Many2one(comodel_name="res.city", string="Area", required=False, )
    contact_name_person = fields.Text(string="Person", required=False, )
    deal_amount = fields.Float(string='Deal Amount', tracking=True)
    deal_status = fields.Selection(string="Deal Status", selection=[('current', 'Current'), ('new', 'New'), ], required=False, )
    Investments_in_millions = fields.Float(string='Investments In Millions', tracking=True)
    start_of_production = fields.Date(string="Start Of Production", required=False, )
    tax_tax = fields.Many2many('ir.attachment',string="Tax", required=True)
    company_type = fields.Selection(string="Company Type", selection=[('One-person company (OPC)', 'One-person company (OPC)'), ('Limited laibility company(LLC)', 'Limited laibility company(LLC)'),
                                                                      ('A company limited by shares','A company limited by shares'),
                                                                      ('joint-stock company','joint-stock company'),
                                                                      ('Partnership company','Partnership company'),
                                                                      ('Limited Partnership company','Limited Partnership company'),
                                                                      ('Sole proprietorsip','Sole proprietorsip'),
                                                                      ], required=False, )
    how_much = fields.Integer(string="How Much Do You Need To Borrow", required=False, )
    year_business = fields.Selection(string="Year in business", selection=[('1-2years', '1-2years'),
                                                                           ('3-5Years','3-5Years'),
                                                                           ('5-10years','5-10years'),
                                                                           ('10+years', '10+years'), ], required=False, )

    industry_id = fields.Many2one(comodel_name="res.partner.industry", string="Company Industry")

    # new_field = fields.Integer(string="People", required=False,compute="count_of_pepole" )

    # registry_id = fields.Many2many('ir.attachment', string="Commercial Registry", required=True)

    # deal_amount,Investments in millions
    # def rest_hdgh(self):
    #     heuh=self.env['sale.order'].search([])
    #     print('>>>>>>>>',heuh)
    #     # print('>>>>>>>>',filt)

    # def count_of_pepole(self):
    #     for rec in self:
    #         count =self.env['sale.order'].search_count([('state','=','sale')])
    #         rec.new_field = count
    #
    #         return {
    #             'type': 'ir.actions.act_window',
    #             'name': 'jooiwuqo',
    #             'view_mode': 'tree,form',
    #             'res_model': 'sale.order',
    #             'domain': [('state', '=', 'sale')],
    #             # 'context': "{'create': False}"
    #         }
    #

