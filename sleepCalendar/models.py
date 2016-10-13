from django.db import models
from django.utils import timezone
from authtools.models import User
import uuid
import datetime


def generateUUID(userId=None, date=None):
	'''
	Returns an md5 hash using string which combines the user id plus the calendar date of the event
	as a way to generate a unique value. Not sure yet, though, if this is the best approach...
	'''
	currentMilliseconds = datetime.datetime.now().timestamp()
	uuidValue = uuid.uuid3(uuid.NAMESPACE_DNS, str(userId) + str(date) + str(currentMilliseconds))
	return str(uuidValue)

class Day(models.Model):
	# Specify which values are available for the sleepingQuality and
	# the tirednessFeeling attributes. This is useful for validation.
	good = 'good'
	bad = 'bad'
	regular = 'regular'
	choices = (
		(good, 'good'),
		(bad, 'bad'),
		(regular, 'regular')
	)

	sleepingQuality = models.CharField(max_length=7, choices=choices)
	tirednessFeeling = models.CharField(max_length=7, choices=choices)
	date = models.DateTimeField(default=timezone.now)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	uuid = models.CharField(max_length=64, default='', blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		'''
		Customizes the save method for this model. It checks whether a uuid value has already been assigned
		to the entry, and if not (meaning it's a new entry), creates one for it. It also updates the date_modified
		field with every call to the save method, i.e. every time a change is made on the entry.
		'''
		if self.uuid == '':
			uuid = generateUUID(self.user_id, self.date)
			self.uuid = str(uuid)
		self.date_modified = timezone.now()
		super(Day, self).save(*args, **kwargs)

	def __str__(self):
		'''Returns a string representation of the object following its constructor syntax'''
		return 'Calendar(user={}, date={}, sleepingQuality={}, tirednessFeeling={}, uuid={})'.format(
			self.user, self.date, self.sleepingQuality, self.tirednessFeeling, self.uuid)

	class Meta:
		# Order results by date of creation
		ordering = ('date_created',)

	def getDict(self):
		'''
		Some of the class attributes are instances of other classes, so they are not serializable into Json.
		This method provides a dictionary representation of all class' attributes for those cases in which
		they must be serialized.
		'''
		return {'sleepingQuality': self.sleepingQuality,
				'tirednessFeeling': self.tirednessFeeling,
				'date': str(self.date),
				'userId': str(self.user),
				'date_created': str(self.date_created),
				'date_modified': str(self.date_modified)
				}
