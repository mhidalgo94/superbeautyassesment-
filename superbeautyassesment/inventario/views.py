from django.http import JsonResponse
from django.views import View
from .models import EquipoModel
from django.forms import model_to_dict

# Create your views here.

def list_equipos(request):
    if request.method== 'GET':
        query = EquipoModel.objects.all()
        data = []
        for m in query:
            to_json = model_to_dict(m)
            data.append(to_json)

        return JsonResponse(data, safe=False)

class ListEquipoGenericView(View):

    def get(self, request, *args, **kwargs):
        query = EquipoModel.objects.all()
        data = []
        for m in query:
            to_json = model_to_dict(m)
            data.append(to_json)
        return JsonResponse(data, safe=False)

