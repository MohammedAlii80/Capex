from odoo import api, fields, models


class crmstagee(models.Model):
    _inherit = 'crm.lead'

    state_stages = fields.Selection(string="", selection=[('capex stage', 'Capex Stage'),
                                                   ('financial institution', 'Financial Institution'),
                                                   ('investigation', 'Investigation'),
                                                   ('credit', 'Credit'),
                                                   ('risk', 'Risk'),
                                                   ('committee', 'Committee'),
                                                   ('capex approval', 'Capex Approval'),
                                                   ], required=False, )

    attachment_att_id = fields.Binary(string="Attachment",)
    attachment_attachment_id = fields.Binary(string="Attachment")
    new_field_date = fields.Date(string="Expiry Date", required=False,)

    state_status = fields.Selection(string="Status", selection=[('approved', 'Approved'), ('declined', 'Declined'), ], required=False, )
    date_da = fields.Date(string="Date", required=False, )
    field_text = fields.Text(string="Text", required=False, )

    attachment_att_capex_id = fields.Binary(string="Attachment")
    new_field_capex = fields.Date(string="Date", required=False, )

    new_field_capex_text = fields.Text(string="Text", required=False, )
    investigation_forms_date = fields.Date(string="Date", required=False, )
    investigation_forms_id = fields.Binary(string="Attachment")
    date_inquires = fields.Date(string="Date", required=False, )
    date_visit = fields.Date(string="Date", required=False, )
    credit_date = fields.Date(string="Date", required=False, )
    inq_date = fields.Date(string="Date", required=False, )
    risk_app_date = fields.Date(string="Date", required=False, )
    risk_app_id = fields.Binary(string="Attachment")
    risk_inq_id = fields.Binary(string="Attachment")
    risk_inq_date = fields.Date(string="Date", required=False, )
    risk_decine_date = fields.Date(string="Date", required=False, )
    new_fidecline = fields.Text(string="Text", required=False, )
    meeting_date = fields.Date(string="Meeting Date", required=False, )
    decision_se = fields.Selection(string="Decision Status", selection=[('approved', 'Approved'), ('declined', 'Declined'), ], required=False, )
    decision = fields.Date(string="Date", required=False, )
    decision_id = fields.Binary(string="Attachment")
    new_decision_text = fields.Text(string="Text", required=False, )

    capex_status = fields.Selection(string="Capex Status", selection=[('approved', 'Approved'),('hold','Hold') ,('declined', 'Declined'), ], required=False, )
    approval_date = fields.Date(string="Date", required=False, )
    new_approval_text = fields.Text(string="Text", required=False, )










