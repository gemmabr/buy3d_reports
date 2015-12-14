# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "Buy3d - Reports",
    "version": "1.0",
    "depends": [
        "sale",
	"stock",
        "purchase",
	"account",
    ],
    "author": "OdooMRP team,"
              "AvanzOSC,"
              "Gemma Bochaca",

    "category": "Custom Module",
    "website": "http://www.odoomrp.com",
    "summary": "Customized reports for Buy3d company",
    "description": """

    """,
    "data": [
        "views/report_sale_buy3d.xml",
	"views/report_deliverynote_buy3d.xml",
        "views/report_purchase_buy3d.xml",
        "views/report_saleinvoice_buy3d.xml",
		"views/report_saleinvoice_buy3d_printable.xml"
        "buy3d_reports_report.xml",
    ],
    "installable": True,
}
