# -*- encoding: utf-8 -*-

import netsvc
import pooler, tools
import math

from tools.translate import _

from osv import fields, osv

class product_template(osv.osv):
  _inherit="product.template"
  
  _columns = {
              'type': fields.selection([('product','Stockable Product'),('consu', 'Consumable'),('service','Service'),('des','Description')], 'Product Type', required=True, help="Will change the way procurements are processed. Consumables are stockable products with infinite stock, or for use when you have no inventory management in the system."),
              }
  _defaults = {
                'type' : lambda *a: 'product',
                'procure_method': lambda *a: 'make_to_order',
                }


   

product_template()

