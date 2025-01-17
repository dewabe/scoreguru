from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.db.models import Q, OuterRef, Subquery
from scoreguru.models import Game, Prediction, TeamsInSeason

class IndexView(LoginRequiredMixin, ListView):
    model = Game
    login_url = 'login/'
    template_name = 'scoreguru/index.html'
    context_object_name = 'games'
    paginate_by = 10

    def get_queryset(self):
        queryset = Game.objects.all().order_by('start_datetime')

        # Hide past games by default
        show_past_games = self.request.GET.get('show_past_games', 'off') == 'on'
        if not show_past_games:
            queryset = queryset.filter(start_datetime__gte=timezone.now())

        # Team filter
        team_query = self.request.GET.get('team', '')
        if team_query:
            queryset = queryset.filter(
                Q(home_team__team__name__icontains=team_query) |
                Q(visitor_team__team__name__icontains=team_query)
            )

        # Get player's predictions
        user_predictions = Prediction.objects.filter(
            user=self.request.user,
            game=OuterRef('pk')
        ).values('predicted_home_goals', 'predicted_visitor_goals', 'total_points')

        queryset = queryset.annotate(
            predicted_home_goals=Subquery(user_predictions.values('predicted_home_goals')[:1]),
            predicted_visitor_goals=Subquery(user_predictions.values('predicted_visitor_goals')[:1]),
            total_points=Subquery(user_predictions.values('total_points')[:1])
        )

        # Filter out games where the player has already made a prediction
        hide_predicted = self.request.GET.get('hide_predicted', 'off') == 'on'
        if hide_predicted:
            queryset = queryset.filter(predicted_home_goals__isnull=True)
    
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()  # Hae queryset
        paginator = Paginator(queryset, self.paginate_by)  # Luo Paginator
        page_number = self.request.GET.get('page')  # Hae nykyinen sivunumero
        page_obj = paginator.get_page(page_number)  # Hae sivuobjekti
        context['games'] = page_obj  # Päivitä sivutettu queryset contextiin

        # Fetch all teams that have upcoming games
        teams = TeamsInSeason.objects.filter(
            Q(home_games__start_datetime__gte=timezone.now()) |
            Q(visitor_games__start_datetime__gte=timezone.now())
        ).distinct().order_by('team__name')
        context['teams'] = teams

        # Create a dictionary of the player's predictions {game.id: prediction}
        predictions = Prediction.objects.filter(user=self.request.user).select_related('game')
        prediction_dict = {prediction.game_id: prediction for prediction in predictions}
        context['predictions'] = prediction_dict
        context['now'] = timezone.now()
        context['MEDIA_URL'] = settings.MEDIA_URL

        return context

    def post(self, request, *args, **kwargs):
        game_id = request.POST.get('game_id')
        predicted_home_goals = request.POST.get('predicted_home_goals')
        predicted_visitor_goals = request.POST.get('predicted_visitor_goals')

        # Fetch the game instance
        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            messages.error(request, "The game does not exist.")
            return redirect('index')

        # Check if the game has already started
        if game.start_datetime <= timezone.now():
            messages.error(request, "You cannot update the prediction after the game has started.")
            return redirect('index')

        # Update or save the prediction if the game hasn't started
        prediction, created = Prediction.objects.update_or_create(
            user=request.user,
            game=game,
            defaults={
                'predicted_home_goals': predicted_home_goals,
                'predicted_visitor_goals': predicted_visitor_goals,
            }
        )

        if created:
            messages.success(request, "Prediction saved successfully!")
        else:
            messages.success(request, "Prediction updated successfully!")

        return redirect('index')
