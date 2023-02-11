# -*- coding: utf-8 -*-
# from odoo import http


# class CapexStages/home/mohamedAli/odoo15C/custom(http.Controller):
#     @http.route('/capex_stages/home/mohamed_ali/odoo15_c/custom/capex_stages/home/mohamed_ali/odoo15_c/custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/capex_stages/home/mohamed_ali/odoo15_c/custom/capex_stages/home/mohamed_ali/odoo15_c/custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('capex_stages/home/mohamed_ali/odoo15_c/custom.listing', {
#             'root': '/capex_stages/home/mohamed_ali/odoo15_c/custom/capex_stages/home/mohamed_ali/odoo15_c/custom',
#             'objects': http.request.env['capex_stages/home/mohamed_ali/odoo15_c/custom.capex_stages/home/mohamed_ali/odoo15_c/custom'].search([]),
#         })

#     @http.route('/capex_stages/home/mohamed_ali/odoo15_c/custom/capex_stages/home/mohamed_ali/odoo15_c/custom/objects/<model("capex_stages/home/mohamed_ali/odoo15_c/custom.capex_stages/home/mohamed_ali/odoo15_c/custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('capex_stages/home/mohamed_ali/odoo15_c/custom.object', {
#             'object': obj
#         })
