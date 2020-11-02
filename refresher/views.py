from django.http import JsonResponse
from django.shortcuts import redirect
from background_task import background


def start(request):
    refresher(repeat=300, repeat_until=None)
    redirect(to="http://www.mainchimaill.ir/cron_isopen.php")
    return JsonResponse({'hey': 'there'}, status=405)


@background(schedule=120, queue='refresher-queue')
def refresher():
    print("0\n")
    redirect(to="http://www.mainchimaill.ir/cron_isopen.php")
    print("1\n")
