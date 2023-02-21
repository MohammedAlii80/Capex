# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class jsonIntegrateController(http.Controller):
    # @http.route('/post-api',type='http', auth='none', methods=['POST'], csrf=False)
    # def post_api(self, **kwargs):
    #     if 'user' in kwargs and 'password' in kwargs:
    #         record_status = request.env['http_api'].sudo().create_record(kwargs)
    #         if record_status:
    #             return record_status
    #         return '{Status: Fail, Error: user or password may be wrong}'
    #     return '{Status: Fail, Error: Add user or password}'

    @http.route('/get_crm_api', type='json', auth='public', methods=['POST'], csrf=False)
    def get_api(self, **kwargs):
        try:
            print(kwargs)
            industry_obj= request.env['res.partner.industry'].sudo().search([('name','=',kwargs.get('industry_id'))])
            # print(industry_obj.id)
            if not industry_obj:

                industry_obj=request.env['res.partner.industry'].sudo().create({'name':str(kwargs.get('industry_id')),
                                                                   'active':True,
                                                                   'full_name':'F'+str(kwargs.get('industry_id')).upper()})

            area_obj = request.env['res.city'].sudo().search([('name', '=', kwargs.get('area_area'))])
            if not area_obj:
                area_obj = request.env['res.city'].sudo().create({'name':str(kwargs.get('area_area'))})
                

            country_obj = request.env['res.country'].sudo().search([('name', '=', kwargs.get('country_id'))])

            if not country_obj:
                country_obj = request.env['res.country'].sudo().create({'name':str(kwargs.get('country_id'))})


            state_obj= request.env['res.country.state'].sudo().search([('name','=',kwargs.get('state_id'))])


            data = {'contact_name': kwargs.get('contact_name'),
                    'name': kwargs.get('name'),
                    'mobile': kwargs.get('mobile'),
                    'email_from': kwargs.get('email_from'),
                    'company_type': kwargs.get('company_type'),
                    'year_business': kwargs.get('year_business'),
                    'sales_turn_over': kwargs.get('sales_turn_over'),
                    'partner_name': kwargs.get('partner_name'),
                    'function': kwargs.get('function'),
                    'tax_number': kwargs.get('tax_number'),
                    'industry_id': industry_obj.id,
                    'area_area': area_obj.id,
                    'country_id': country_obj.id,
                    'state_id': state_obj.id,
                    'type': 'lead',
                    }
            request.env['crm.lead'].sudo().create(data)



            data_helpdesk =  {'name': kwargs.get('name'),
                                'partner_email':kwargs.get('partner_email'),
                                'description': kwargs.get('description'),
                                }
            request.env['helpdesk.ticket'].sudo().create(data_helpdesk)


            return 'Status Succsfull'
        except Exception as e:
            print(e)
            return '{Status: Fail, Error: user or password may be wrong}'



