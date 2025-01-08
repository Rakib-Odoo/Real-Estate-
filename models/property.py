from odoo import fields, models, api


class Property(models.Model):
    _name = 'real_estate.property'
    _description = 'Property Details'

    name = fields.Char(string='Property Name', required=True)
    state = fields.Selection([
        ('new','New'),
        ('received','Offer Received'),
        ('accepted','Offer Accepted'),
        ('sold','Sold'),
        ('canceled','Canceled'),
    ], string='Status', default='new')
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_available = fields.Date(string='Available From')
    expected_price = fields.Float(string='Expected Price')
    best_offer = fields.Float(string='Best Offer', compute='_compute_best_offer')
    selling_price = fields.Float(string='Selling Price', readonly=True)
    bedroom = fields.Integer(string='Bedrooms')
    living_area = fields.Float(string='Living Area (sqm)')
    bathroom = fields.Integer(string='Bathrooms')
    garage = fields.Boolean(string='Garages', default=False)
    garden = fields.Boolean(string='Garden', default=False)
    garden_area = fields.Float(string='Garden Area (sqm)')
    gardem_orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West'),
    ], string='Garden Orientation')