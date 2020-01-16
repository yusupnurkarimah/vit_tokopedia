from odoo import api, fields, models, _
import time
import datetime
import logging
from io import BytesIO
import xlsxwriter
import base64
from odoo.exceptions import Warning
_logger = logging.getLogger(__name__)

class product(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    berat       = fields.Char(string='Berat')
    pesan       = fields.Char(string='Pemesanan Minimum')
    status      = fields.Char(string='Status')
    jumlah      = fields.Char(string='Jumlah Stok')
    etalase     = fields.Char(string='Etalase')
    preorder    = fields.Char(string='Preorder')
    waktu_preorder    = fields.Char(string='Waktu Proses Preorder')
    kondisi     = fields.Char(string='Kondisi')
    gambar_1    = fields.Char(string='Gambar 1')
    gambar_2    = fields.Char(string='Gambar 2')
    gambar_3    = fields.Char(string='Gambar 3')
    gambar_4    = fields.Char(string='Gambar 4')
    gambar_5    = fields.Char(string='Gambar 5')
    url_1       = fields.Char(string='URL Video Produk 1')
    url_2       = fields.Char(string='URL Video Produk 2')
    url_3       = fields.Char(string='URL Video Produk 3')
    is_exported = fields.Boolean(string="Is Exported",  )
    date_exported = fields.Datetime(string="Exported Date", required=False, )