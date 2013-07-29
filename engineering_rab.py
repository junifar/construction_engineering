from osv import osv, fields

class RAB(osv.osv):
	
	STATE_SELECTION = [
		('new', 'New'),
		('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ]

	_name='construction.engineering.rab'
	_description = 'Construction Engineering RAB Module' 
	_columns = {
			'rab_number' : fields.char('Nomor RAB', 300 , required = True),
			'name' : fields.char('Site Name', 300 , required = True),
			'state': fields.selection(STATE_SELECTION, 'Status', readonly=True, help="No help for this time", select=True),
		}
RAB()