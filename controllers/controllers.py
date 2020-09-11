# -*- coding: utf-8 -*-
# from odoo import http


# class Parc(http.Controller):
#     @http.route('/parc/parc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parc/parc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('parc.listing', {
#             'root': '/parc/parc',
#             'objects': http.request.env['parc.parc'].search([]),
#         })

#     @http.route('/parc/parc/objects/<model("parc.parc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parc.object', {
#             'object': obj
#         })
