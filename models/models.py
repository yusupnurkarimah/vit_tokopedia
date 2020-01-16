# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api
import csv
from odoo.modules import get_module_path
from odoo.exceptions import UserError
from xlrd import open_workbook
import copy
import pdb
import xlwt
import logging
from io import StringIO
import base64
_logger = logging.getLogger(__name__)

class Export(models.Model):
	_name = 'vit.export'

	import_file     = fields.Binary(string="Import File",  )
	name            = fields.Char(string="Nama Toko",)
	company_id      = fields.Many2one(comodel_name='res.company', string='Company')
	date_start      = fields.Date(string='Date Start', required=False,
						default=lambda self:time.strftime("%Y-%m-%d"))
	date_end        = fields.Date(string='Date End', required=False,
						default=lambda self:time.strftime("%Y-%m-%d"))

	@api.multi
	def import_excel(self):
		data = base64.b64decode(self.import_file)
		wb = open_workbook(file_contents=data)
		all_datas = []
		for s in wb.sheets():
			for row in range(s.nrows):
				data_row = []
				for col in range(s.ncols):
					value = (s.cell(row, col).value)
					data_row.append(value)
				all_datas.append(data_row)
		data = []
		for i in all_datas:
			data.append(i)
			line_partner = []
			# pdb.set_trace()
			for x in data:
				line = [x[10],
						x[14]]
				line_partner.append(line)