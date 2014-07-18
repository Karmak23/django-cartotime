from django.views.generic import ListView
from timelinejs.models import Timeline
from timelinejs.views import TimelineView

class TimelineList(ListView):
	template_name = 'timeline_list.html'
	model = Timeline

class CartoTimeView(TimelineView):
	template_name = "cartotime.html"
