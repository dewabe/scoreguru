from django.views.generic import ListView
from django.db.models import Sum, Count, Q
from scoreguru.models import Scoreboard, Prediction, Season

class ScoreboardView(ListView):
    model = Scoreboard
    template_name = 'scoreguru/scoreboard.html'
    context_object_name = 'scoreboard'
    paginate_by = 10

    def get_queryset(self):
        season = self.request.GET.get('season', None)
        queryset = Scoreboard.objects.all()
        prediction_filter = Q()
        
        if season:
            queryset = queryset.filter(season__name=season)
            prediction_filter = Q(user__prediction__game__season__name=season)

        queryset = queryset.annotate(
            bets=Count('user__prediction', filter=prediction_filter)
        )

        return queryset.order_by('-total_points')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seasons'] = Season.objects.all().order_by('-start_date')
        context['selected_season'] = self.request.GET.get('season', None)
        return context
