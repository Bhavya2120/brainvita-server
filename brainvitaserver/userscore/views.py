from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import UserScores
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST
def form_submit(request):
    userName = request.POST.get('userName')
    score = request.POST.get('score')

    if userName and score:
        form_data = UserScores(userName=userName, score=score)
        form_data.save()
        return JsonResponse({'message': 'Form data saved successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid form data'}, status=400)
