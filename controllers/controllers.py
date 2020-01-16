# -*- coding: utf-8 -*-
from odoo import http

# class VitStockOpname(http.Controller):
#     @http.route('/vit_stock_opname/vit_stock_opname/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_stock_opname/vit_stock_opname/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_stock_opname.listing', {
#             'root': '/vit_stock_opname/vit_stock_opname',
#             'objects': http.request.env['vit_stock_opname.vit_stock_opname'].search([]),
#         })

#     @http.route('/vit_stock_opname/vit_stock_opname/objects/<model("vit_stock_opname.vit_stock_opname"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_stock_opname.object', {
#             'object': obj
#         })