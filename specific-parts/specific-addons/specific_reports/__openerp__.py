# -*- coding: utf-8 -*-
#
#
#    Author: Yannick Vaucher
#    Copyright 2016 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
{'name': 'Swisslux Reports Customization',
 'summary': 'Layouts',
 'version': '9.0.1.0.0',
 'author': 'Camptocamp',
 'maintainer': 'Camptocamp',
 'category': 'Reports',
 'complexity': "normal",  # easy, normal, expert
 'depends': ['base',
             'report',
             'sale',
             'account',
             'stock',
             ],
 'website': 'http://www.camptocamp.com',
 'data': [
     'views/layouts.xml',
     'views/invoice.xml',
     'views/sale.xml',
     'views/product.xml',
     'views/templates.xml',
     'views/company.xml'],
 'demo_xml': [],
 'test': [],
 'installable': True,
 'auto_install': False,
 'license': 'AGPL-3',
 'application': False,
 }
