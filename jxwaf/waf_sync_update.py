from django.http import JsonResponse
import json
from jxwaf.models import *
from django.db.models import Q
import requests

def waf_sync_update_get_jxcheck_list(request):
    return_result = {}
    data = []
    try:
        user_id = request.session['user_id']
        try:
            r = requests.get('https://api.jxwaf.com/open/waf_get_open_jxcheck' )
            result = r.json()
            if result['result'] == True:
                return_result['result'] = True
                return_result['message'] = result['message']
                return JsonResponse(return_result, safe=False)
            else:
                return_result['result'] = False
                return_result['message'] = "error"
                return JsonResponse(return_result, safe=False)
        except:
            return_result['result'] = False
            return_result['message'] = "error"
            return JsonResponse(return_result, safe=False)
    except Exception, e:
        return_result['result'] = False
        return_result['message'] = str(e)
        return_result['errCode'] = 108
        return JsonResponse(return_result, safe=False)

def waf_sync_update_get_jxcheck_update(request):
    return_result = {}
    data = []
    try:
        user_id = request.session['user_id']
        json_data = json.loads(request.body)
        jxcheck_code = json_data['jxcheck_code']
        try:
            waf_jxcheck.objects.create(user_id='jxwaf',jxcheck_code=jxcheck_code)
        except:
            waf_jxcheck.objects.filter(user_id='jxwaf').update(jxcheck_code=jxcheck_code)
    except Exception, e:
        return_result['result'] = False
        return_result['message'] = str(e)
        return_result['errCode'] = 108
        return JsonResponse(return_result, safe=False)

def waf_sync_update_get_botcheck_list(request):
    return_result = {}
    data = []
    try:
        user_id = request.session['user_id']
        try:
            r = requests.get('https://api.jxwaf.com/open/waf_get_open_botcheck' )
            result = r.json()
            if result['result'] == True:
                return_result['result'] = True
                return_result['message'] = result['message']
                return JsonResponse(return_result, safe=False)
            else:
                return_result['result'] = False
                return_result['message'] = "error"
                return JsonResponse(return_result, safe=False)
        except:
            return_result['result'] = False
            return_result['message'] = "error"
            return JsonResponse(return_result, safe=False)
    except Exception, e:
        return_result['result'] = False
        return_result['message'] = str(e)
        return_result['errCode'] = 108
        return JsonResponse(return_result, safe=False)

def waf_sync_update_get_botcheck_update(request):
    return_result = {}
    data = []
    try:
        user_id = request.session['user_id']
        json_data = json.loads(request.body)
        botcheck_code = json_data['botcheck_code']
        version = json_data['version']
        try:
            waf_botcheck.objects.create(user_id=version,botcheck_code=botcheck_code)
        except:
            waf_botcheck.objects.filter(user_id='jxwaf').update(jxcheck_code=botcheck_code)
    except Exception, e:
        return_result['result'] = False
        return_result['message'] = str(e)
        return_result['errCode'] = 108
        return JsonResponse(return_result, safe=False)

def waf_sync_update_get_botcheck_key_update(request):
    return_result = {}
    data = []
    try:
        user_id = request.session['user_id']
        try:
            r = requests.get('https://api.jxwaf.com/open/waf_get_open_botcheck_key' )
            result = r.json()
            if result['result'] == True:
                for bot_key in result['message']:
                    print bot_key
                    uuid = bot_key['uuid']
                    key = bot_key['key']
                    bot_check_mode = bot_key['bot_check_mode']
                    try:
                        waf_cc_bot_html_key.objects.get(Q(key=key) & Q(uuid=uuid))
                    except:
                        waf_cc_bot_html_key.objects.create(user_id="jxwaf", uuid=uuid, key=key,
                                                           bot_check_mode=bot_check_mode)
                return_result['result'] = True
                return_result['message'] = len(result['message'])
                return JsonResponse(return_result, safe=False)
            else:
                return_result['result'] = False
                return_result['message'] = "error"
                return JsonResponse(return_result, safe=False)
        except Exception, e:
            return_result['result'] = False
            return_result['message'] = str(e)
            return JsonResponse(return_result, safe=False)
    except Exception, e:
        return_result['result'] = False
        return_result['message'] = str(e)
        return_result['errCode'] = 108
        return JsonResponse(return_result, safe=False)