# Context Global
from nomencladores.models import departamentos

def get_depas(request):
    depas = departamentos.objects.all()
    return {
        'departamentos_list':depas
    }