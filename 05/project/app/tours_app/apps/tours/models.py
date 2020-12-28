from django.db import models

class Tour(models.Model):
	# tour_id    = models.PositiveSmallIntegerField('ід походу') # only 0,1, ... ,32767
	name       = models.CharField('назва походу',max_length = 100)
	photo_url  = models.URLField('посилання на фото походу',max_length = 1000) # maxlen 200 (default) 
	regione    = models.CharField('територія де відбуватиметься похід',max_length = 50)
	month      = models.PositiveSmallIntegerField('звичний місяць для проведення')
	days_len   = models.PositiveSmallIntegerField('тривалість походу в днях')
	difficulty = models.PositiveSmallIntegerField('складність')
	tour_len   = models.PositiveSmallIntegerField('довжина маршруту в км')

	def __str__(self):
		return f'{self.id}_{self.name}'

	class Meta:
		verbose_name = 'Похід'
		verbose_name_plural = 'Походи'



class Tour_event(models.Model):
	date = models.DateTimeField('дата створення події')
	start_date = models.DateTimeField('запланована дата початку походу')
	tour = models.OneToOneField(Tour,on_delete = models.CASCADE)

	def __str__(self):
		return f'{self.id}. {self.start_date}_{self.tour.name}'

	class Meta:
		verbose_name = 'Подія походу'
		verbose_name_plural = 'Події походу'



class Person(models.Model):
	nickname   = models.CharField('нік',max_length = 30)
	password   = models.CharField('пароль',max_length = 40)
	name       = models.CharField('ім`я',max_length = 30)
	age        = models.PositiveSmallIntegerField('вік')
	phone      = models.CharField('мобільний номер',max_length = 30)
	email      = models.EmailField('email',max_length = 30)
	condition  = models.PositiveSmallIntegerField('фізичний стан')
	tour_event = models.ForeignKey(Tour_event,on_delete = models.SET_NULL,blank=True,null=True) # одна людина не може бути записана одночасно в 2 походи (тому такий зв`язок є коректним)

	def __str__(self):
		return f'{self.id}. {self.name}({self.nickname})'

	class Meta:
		verbose_name = 'Учасник'
		verbose_name_plural = 'Учасники'