from django.test import TestCase, Client


class CalendarListTest(TestCase):

	def setUp(self):
		self.c = Client()

	def test_HelloWorld(self):
		self.assertEqual(1, 1)


# class GetDayEntryTest(TestCase):
#
# 	def setUp(self):
# 		self.c = Client()
#
# 		carlos = User.objects.create(username='jose')
#
# 		dateISO = '2016-02-09T23:48:14.297Z'
# 		date = getDatetimeFromISO(dateISO)
# 		setUpEntry = Day.objects.create(user=carlos,
# 			                  sleepingQuality='bad',
# 			                  tirednessFeeling='good',
# 			                  date=date,
# 			                  )
# 		self.setUpEntry = Day.objects.get(date=date)
#
#
#
# 	def test_retrieve_entries(self):
# 		response = self.c.get('/calendar/year/2016')
# 		print('Respone from get ', response.content)
# 		self.assertEqual(response.status_code, 200)
#
# 	def test_retrieve_wrong_method(self):
# 		response = self.c.post('/calendar/year/2016')
# 		self.assertEqual(response.status_code, 405)
#
#
# class InsertDayEntryTest(TestCase):
#
# 	def setUp(self):
# 		self.c = Client()
#
# 		carlos = User.objects.create(username='carlos')
#
# 	def test_entries_inserted_correctly(self):
# 		data = {'user': '1',
# 				'sleepingQuality': 'good',
# 				'tirednessFeeling': 'bad',
# 				'date': '2016-02-09T23:48:14.297Z'
# 				}
# 		request = HttpRequest()
# 		request.url = '/calendar'
# 		request.data = data
# 		response = self.c.post('/calendar', data=data)
#
# 		event = Day.objects.all()
#
# 		self.assertEqual(len(event), 1)
#
# 	def test_wrong_method(self):
# 		response = self.c.get('/calendar')
# 		self.assertEqual(response.status_code, 405)
#
#
# class UpdateDayEntryTest(TestCase):
#
# 	def setUp(self):
# 		self.c = Client()
#
# 		carlos = User.objects.create(username='carlos')
#
# 		dateISO = '2016-02-09T23:48:14.297Z'
# 		date = getDatetimeFromISO(dateISO)
# 		setUpEntry = Day.objects.create(user=carlos,
# 			                  sleepingQuality='bad',
# 			                  tirednessFeeling='good',
# 			                  date=date
# 			                  )
# 		self.setUpEntry = Day.objects.get(date=date)
#
# 	def test_update_day_entry(self):
# 		data = {'user': 1,
# 				'sleepingQuality': 'good',
# 				'tirednessFeeling': 'bad',
# 				'date': '2016-02-09T23:48:14.297Z',
# 				'uuid': self.setUpEntry.uuid
# 				}
# 		dataJSON = json.dumps(data)
#
#
# 		serializer = DaySerializer(data=data)
# 		serializer.initial_data['date'] = dateutil.parser.parse(serializer.initial_data['date'])
# 		values = {key: value for key, value in serializer.initial_data.items() if key != 'uuid'}
# 		dbEntry = Day.objects.get(uuid=serializer.initial_data['uuid'])
# 		newSerializer = DaySerializer(dbEntry, data=values)
# 		print(newSerializer)
# 		if newSerializer.is_valid():
# 			print('Hey, well done!')
# 		else:
# 			print('Houston! We have got a problem!')
#
#
# 		response = self.c.put('/calendar',
# 						content_type='application/json',
# 						data=dataJSON)
# 		dbEntry = Day.objects.get(uuid=self.setUpEntry.uuid)
# 		self.assertEqual(dbEntry.sleepingQuality, 'good')
# 		self.assertEqual(dbEntry.tirednessFeeling, 'bad')
#
#
# class DeleteDayEntry(TestCase):
#
# 	def setUp(self):
# 		self.c = Client()
#
# 		carlos = User.objects.create(username='carlos')
#
# 		dateISO = '2016-02-09T23:48:14.297Z'
# 		date = getDatetimeFromISO(dateISO)
# 		setUpEntry = Day.objects.create(user=carlos,
# 			                  sleepingQuality='bad',
# 			                  tirednessFeeling='good',
# 			                  date=date
# 			                  )
# 		self.setUpEntry = Day.objects.get(date=date)
#
# 	def test_delete_day_entry(self):
# 		data = {'user': 1,
# 				'uuid': self.setUpEntry.uuid
# 				}
# 		dataJSON = json.dumps(data)
# 		request = HttpRequest()
# 		request.url = '/calendar'
# 		request.data = dataJSON
# 		response = self.c.delete('/calendar',
# 						content_type='application/json',
# 						data=dataJSON)
#
# 		self.assertEqual(len(Day.objects.all()), 0)
#
# class TestSerializers(TestCase):
#
# 	def setUp(self):
# 		self.c = Client()
# 		carlos = User.objects.create(username='carlos', email='j@j.com')
# 		self.day = Day.objects.create(sleepingQuality='bad', tirednessFeeling='good', date=timezone.now(), user=carlos)
# 		#time.sleep(5)
# 		self.day2 = Day.objects.create(sleepingQuality='regular', tirednessFeeling='bad', date=timezone.now(), user=carlos)
#
# 	def test_serializer_day(self):
# 		serializer = DaySerializer(Day.objects.all(), many=True)
# 		content = JSONRenderer().render(serializer.data)
#
# 	def test_get_calendar_entries(self):
# 		response = self.c.get('/api/1/calendar/year/2016')









