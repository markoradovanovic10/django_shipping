from django.views.generic import DetailView
from ..models import Profile
from ..models import VehicleLog
from django.utils import timezone
from ..forms import VehicleLogForm
from django.shortcuts import redirect
from ..services import VehicleLogService


class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'data'

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        state = VehicleLogService.get_state(self.request.user)

        if state is None:
            context['has_vehicle'] = False
            return context

        context['already_logged'] = state['already_logged']

        if not state['already_logged']:
            context['form'] = VehicleLogForm()

        return context

    def post(self, request, *args, **kwargs):
        state = VehicleLogService.get_state(self.request.user)

        if state['vehicle'] is None:
            return redirect('profile')

        if state['already_logged']:
            return redirect('profile')

        form = VehicleLogForm(request.POST)

        if form.is_valid():
            VehicleLogService.create_log(
                user=request.user,
                mileage=form.cleaned_data['mileage']
            )
        return redirect('profile')
