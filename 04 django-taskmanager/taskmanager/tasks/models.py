from django.db import models
import datetime

statuses = (
	("T", "To Do"),
	("P", "In Progress"),
	("R", "Review"),
	("D", "Done"),
)

class Task(models.Model):
	txt = models.CharField(max_length=140)
	#text = models.TextField()
	time_given = models.DateTimeField(default=datetime.datetime.today)
	deadline = models.DateTimeField(blank=True, null=True,
		default=datetime.datetime.today)
	status = models.CharField(max_length=1, choices=statuses,
		default='T')
	priority = models.IntegerField(default=5)

	def __unicode__(self):
		return "%s : %s : %s" % (self.txt, self.priority, self.get_status_display())
