# -*- coding: utf-8 -*-
# Copyright (C) 2016-Today: La Louve (<http://www.lalouve.net/>)
# @author: Antoine Beloeuvre (antoine@lance-requete.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


{
    'name': 'Louve Badge Print',
    'version': '9.0.0.0.0',
    'category': 'Custom',
    'summary': 'Allow to print La Louve member badges',
    'author': 'Antoine Beloeuvre',
    'website': 'http://www.lalouve.net',
    'depends': [
        'base',
        'louve_membership',
    ],
    'data': [
        'security/ir_module_category.xml',
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'data/report_paperformat.xml',
    ],
    'installable': True,
}
