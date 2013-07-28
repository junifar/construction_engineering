from osv import osv, fields

class RAB(osv.osv):
	_name='construction.engineering.rab'
	_description = 'Construction Engineering RAB Module' 
	_columns = {
			'rab_number' : fields.char('Nomor RAB', 300 , required = True),
			'name' : fields.char('Site Name', 300 , required = True),
		}
RAB()