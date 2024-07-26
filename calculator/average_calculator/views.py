import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response 

winsize = 10
cur_win = []

@api_view(['GET'])
def avg_calculator(request, qualifier):
    qualifier_urls = {
        'p': "http://20.244.56.144/test/prime",
        'f': "http://20.244.56.144/test/fibonacci",
        'e': "http://20.244.56.144/test/even",
        'r': "http://20.244.56.144/test/random",
    }
    response = requests.get(qualifier_urls.get(qualifier, ''), timeout=0.5)
    new_no = response.json().get('numbers', [])
    before_state = cur_win.copy()

    for num in new_no:
        if num not in cur_win:
            cur_win.append(num)

    if len(cur_win) > winsize:
        cur_win = cur_win[-winsize:]
    if len(cur_win) > 0:
        avg = sum(cur_win) / len(cur_win)
    else:
        avg = 0
    return Response({
        "numbers": new_no,
        "window_PrevState": before_state,
        "window_CurrState": cur_win,
        "avg": f"{avg:.2f}"
    })
