from odoo import api, fields, models, _
import time
import csv
from odoo.modules import get_module_path
from odoo.exceptions import UserError
import copy
import logging
from io import StringIO
import base64
_logger = logging.getLogger(__name__)

class export_product_wizard(models.TransientModel):
    _name = 'vit.export_product'
    
    export_file = fields.Binary(string="Export File",  )
    export_filename = fields.Char(string="Export File",  )

    @api.multi
    def confirm_button(self):
        """
        export product yang is_exported = False
        update setelah export
        :return: 
        """
        cr = self.env.cr

        headers = [
            "Nama Produk*",
            "SKU",
            "Kategory*",
            "Deskripsi Produk",
            "Harga*(Rp)",
            "Berat*(Gram)",
            "Pemesanan Minimum*",
            "Status*",
            "Jumlah Stok*",
            "Etalase",
            "Preorder",
            "Waktu Proses Preorder",
            "Kondisi*",
            "Gambar 1",
            "Gambar 2",
            "Gambar 3",
            "Gambar 4",
            "Gambar 5",
            "URL Video Produk 1",
            "URL Video Produk 2",
            "URL Video Produk 3",
        ]

        mpath = get_module_path('vit_export')

        # csvfile = open(mpath + '/static/product.csv', 'wb')
        csvfile = StringIO()
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow([h.upper() for h in headers])

        product = self.env['product.template']
        products = product.search([('is_exported','=',False)])
        i=0
        
        for prod in products:
            data = {
                "Nama Produk*"          : prod.name,
                "SKU"                   : prod.default_code,
                "Kategory*"             : prod.categ_id.name,
                "Deskripsi Produk"      : prod.name,
                "Harga*(Rp)"            : prod.lst_price,
                "Berat*(Gram)"          : prod.berat,
                "Pemesanan Minimum*"    : prod.pesan,
                "Status*"               : prod.status,
                "Jumlah Stok*"          : prod.jumlah,
                "Etalase"               : prod.etalase,
                "Preorder"              : prod.preorder,
                "Waktu Proses Preorder" : prod.waktu_preorder,
                "Kondisi*"              : prod.kondisi,
                "Gambar 1"              : prod.gambar_1,
                "Gambar 2"              : prod.gambar_2,
                "Gambar 3"              : prod.gambar_3,
                "Gambar 4"              : prod.gambar_4,
                "Gambar 5"              : prod.gambar_5,
                "URL Video Produk 1"    : prod.url_1,
                "URL Video Produk 2"    : prod.url_2,
                "URL Video Produk 3"    : prod.url_3,
            }
            csvwriter.writerow([data[v] for v in headers])

            prod.is_exported=True
            prod.date_exported=time.strftime("%Y-%m-%d %H:%M:%S")
            i+=1

        cr.commit()
        # csvfile.close()

        # raise UserError("Export %s record(s) Done!" % i)

        self.export_file = base64.b64encode(csvfile.getvalue().encode())
        self.export_filename = 'Export-%s.csv' % time.strftime("%Y%m%d_%H%M%S")
        return {
            'name': "Export Complete, total %s records" % i,
            'type': 'ir.actions.act_window',
            'res_model': 'vit.export_product',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'views': [(False, 'form')],
            'target': 'new',
        }