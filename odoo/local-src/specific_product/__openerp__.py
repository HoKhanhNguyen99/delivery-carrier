# -*- coding: utf-8 -*-
# © 2016 Yannick Vaucher (Camptocamp)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{'name': 'Specific - Product',
 'version': '9.0.1.1.0',
 'author': 'Camptocamp',
 'license': 'AGPL-3',
 'category': 'Swisslux Modules',
 'website': 'http://www.swisslux.ch',
 'images': [],
 'depends': [
     'purchase',
     'product',
     'stock'
     ],
 'data': [
     'data/product_product_sequence.xml',
     'views/product.xml',
     'views/product_class.xml',
     'views/product_color_code.xml',
     'views/product_harmsys_code.xml',
     'views/product_manual_code.xml',
     'views/product_supplierinfo.xml',
     'views/purchase_order.xml',
     'security/ir.model.access.csv',
     ],
 'test': [],
 'installable': True,
 'auto_install': False,
 }
