from django.shortcuts import render
import datetime
import pytz
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from .models import User, Wish
from ebaysdk.finding import Connection as Finding

def index(request):
    if request.user.is_authenticated():
        context = {'logged_in': True}
    else:
        context = {'logged_in': False}
    return render(request, 'iWant/index.html', context)

def sign_up(request):
    return render(request, 'iWant/login.html')

def sign_in(request):
    return render(request, 'iWant/login.html')

def username_exists(username):
    if User.objects.filter(username=username).count():
        return True
    else:
        return False

def email_exists(email):
    if User.objects.filter(email=email).count():
        return True
    else:
        return False

def password_valid(password):
    one_letter = False
    one_number = False
    for char in password:
        # Check for number.
        if char.isdigit():
            one_number = True
        # Check for letter.
        if char.isalpha():
            one_letter = True
    if one_letter and one_number:
        return True
    else:
        return False

def create_account(request):
    if request.method == "GET":
        return render(request, 'iWant/login.html')
    if request.method == "POST":
        fName = request.POST.get('firstname', '')
        lName = request.POST.get('lastname', '')
        userEmail = request.POST.get('email', '')
        uName = request.POST.get('username', '')
        uPwd = request.POST.get('password', '')
        uPwdConfirm = request.POST.get('confirm-password', '')
    if username_exists(uName):
        context = {'error_usernameTaken': True}
        return render(request, 'iWant/login.html', context)
    if email_exists(userEmail):
        context = {'error_emailExists': True}
        return render(request, 'iWant/login.html', context)
    # if not password_valid(uPwd):
    #     context = {'error_passwordStructure': True}
    #     return render(request, 'iWant/login.html', context)
    if (fName == '' or lName == '' or userEmail == '' or uName == '' or 
        uPwd == '' or uPwdConfirm == ''):
        context = {'incomplete_fields': True}
        return render(request, 'iWant/login.html', context)
    if (uPwd) != (uPwdConfirm):
        context = {'password_mismatch': True}
        return render(request, 'iWant/login.html', context)
    new_user = User.objects.create_user(username=uName, email=userEmail, 
        password=uPwd, first_name=fName, last_name=lName)
    # Customize login screen to include user information (i.e. full name).
    user = request.user
    all_wishes = user.wish_set.all()
    context = {'user': user, 'wishes': all_wishes}
    return render(request, 'iWant/profile.html', context)

def profile(request):
    if not request.user.is_authenticated():
        # Never crashes if there is no POST data. Will revert to empty string.
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                # Creates a user session.
                login(request, user)
                # Create context to customize profile with welcome text using 
                #the user's information (i.e. full name).
                user = User.objects.get(username=username)
                wishes = user.wish_set.all()
                context = {'wishes': wishes}
                context['just_logged_in'] = True
                return render(request, 'iWant/profile.html', context)
            else:
                # Create provision for disabled accounts that violated terms of 
                # use.
                context = {'disabled': True}
                return render(request, 'iWant/login-page.html', context)
        else:
            # Redirect back to the login page if username and/or password
            # credentials are incorrect.
            context = {'incorrect_creds': True}
            return render(request, 'iWant/login.html', context)
    # If the user is already logged in, allow him/her to access the profile
    # page directly without further authentication processes.
    else:
        user = request.user
        all_wishes = user.wish_set.all()
        context = {'user': user, 'wishes': all_wishes}
        return render(request, 'iWant/profile.html', context)

def new_wish(request):
    context = {}
    return render(request, 'iWant/new-wish.html', context)

def add_wish(request):
    if request.method == "POST":
        user = request.user
        full_name = user.get_full_name()
        item = request.POST.get('item', '')
        brand = request.POST.get('brand', '')
        condition = request.POST.get('condition', '')
        created_date = datetime.datetime.now(pytz.utc)
        details = request.POST.get('details', '')
        # Perform form validation, and send the user back to the Create Zuppl
        # page if there were any missing fields.
        if (item == ''):
            context = {'missed_field': True}
            return render(request, 'iWant/new-wish.html', context)
        else:
            new_wish = Wish(creator=user, item=item, 
                brand=brand, condition=condition, created_date=created_date,
                details=details)
            new_wish.save()
    wish_list = user.wish_set.all()
    context = {'wishes': wish_list}
    return render(request, 'iWant/profile.html', context)

def getDetails(name):
  time1Start = '2015-09-19T00:00:00.000Z'
  time1End = '2015-09-19T23:59:59.999Z'
  time2Start = '2015-09-20T00:00:00.000Z'
  time2End = '2015-09-20T23:59:59.999Z'
  time3Start = '2015-09-21T00:00:00.000Z'
  time3End = '2015-09-21T23:59:59.999Z'
  time4Start = '2015-09-22T00:00:00.000Z'
  time4End = '2015-09-22T23:59:59.999Z'
  time5Start = '2015-09-23T00:00:00.000Z'
  time5End = '2015-09-23T23:59:59.999Z'
  time6Start = '2015-09-24T00:00:00.000Z'
  time6End = '2015-09-24T23:59:59.999Z'
  time7Start = '2015-09-25T00:00:00.000Z'
  time7End = '2015-09-25T23:59:59.999Z'
  time8Start = '2015-09-26T00:00:00.000Z'
  time8End = '2015-09-26T14:40:00.000Z'
  d1 = findItem(name, time1Start, time1End)
  d2 = findItem(name, time2Start, time2End)
  d3 = findItem(name, time3Start, time3End)
  d4 = findItem(name, time4Start, time4End)
  d5 = findItem(name, time5Start, time5End)
  d6 = findItem(name, time6Start, time6End)
  d7 = findItem(name, time7Start, time7End)
  d8 = findItem(name, time8Start, time8End)
  l = []
  l.append(findAvgPriceForOneDay(d1))
  l.append(findAvgPriceForOneDay(d2))
  l.append(findAvgPriceForOneDay(d3))
  l.append(findAvgPriceForOneDay(d4))
  l.append(findAvgPriceForOneDay(d5))
  l.append(findAvgPriceForOneDay(d6))
  l.append(findAvgPriceForOneDay(d7))

  today = findAvgPriceForOneDay(d8)
  avg = round(average(l),2)
  return (l, today, avg)

def findItem(name, timeStart, timeEnd):
  api = Finding(appid='VarunRam-29e8-46c1-87ef-dbcf272585f7', 
                config_file =None)
  api_request = {
      'keywords': name,
      'sortOrder': 'EndTimeSoonest',
      'itemFilter': {
        'name': 'SoldItemsOnly',
        'value': 'true',
        'name':'EndTimeFrom',
        'value':timeStart,
        'name':'EndTimeTo',
        'value':timeEnd
      }
  }
  response = api.execute('findCompletedItems', api_request)

  assert(response.reply.ack == 'Success')
  return response.dict()

def average(l):
  if l == []:
    return 0
  return sum(l) / len(l)

def findAvgPriceForOneDay(d):
  itemList = d['searchResult']['item']
  priceList = []
  for item in itemList:
    priceList.append(round(float(item['sellingStatus']['convertedCurrentPrice']['value']),2))
  #print
  pListLength = len(priceList)
  priceList.sort()
  priceList = priceList[pListLength//4 : 3*pListLength//4]
  #print(priceList)
  return round(average(priceList),2)

def findCurrentItem(name):
  api = Finding(appid='VarunRam-29e8-46c1-87ef-dbcf272585f7', 
                config_file =None)
  api_request = {
      'keywords': name,
      'sortOrder': 'CurrentPriceHighest',
  }
  response = api.execute('findCompletedItems', api_request)

  assert(response.reply.ack == 'Success')
  return response.dict()

def sortFinalList(finalList, avg, name):
  finalList.sort(key = lambda x: abs(x[0] - avg))

def getBestThree(name, avg):
  d = findCurrentItem(name)
  itemList = d['searchResult']['item']
  item1Url = itemList[0]['viewItemURL']
  item1Price = round(float(itemList[0]['sellingStatus']['convertedCurrentPrice']['value']),2)
  item1Name = itemList[0]['title']
  item2Url = itemList[1]['viewItemURL']
  item2Name = itemList[1]['title']
  item2Price = round(float(itemList[1]['sellingStatus']['convertedCurrentPrice']['value']),2)
  item3Url = itemList[2]['viewItemURL']
  item3Name = itemList[2]['title']
  item3Price = round(float(itemList[2]['sellingStatus']['convertedCurrentPrice']['value']),2)
  maxDifference = max(abs(item1Price- avg), abs(item2Price- avg), abs(item3Price- avg))
  finalList = []
  finalList.append((item1Price,item1Url, item1Name))
  finalList.append((item2Price,item2Url, item2Name))
  finalList.append((item3Price,item3Url, item3Name))
  sortFinalList(finalList, avg, name)
  for i in range(3, len(itemList)):
    url = itemList[i]['viewItemURL']
    price = round(float(itemList[i]['sellingStatus']['convertedCurrentPrice']['value']),2)
    name = itemList[i]['title']
    diff = abs(price - avg)
    if diff < abs(finalList[2][0] - avg):
      finalList[2] = (price, url, name)
      sortFinalList(finalList, avg, name)
  return finalList

def detail(request, wish_id):
    wish = Wish.objects.get(id=wish_id)
    queryStr = wish.brand + ' ' + wish.item + ' ' + wish.details
    returnData = getDetails(queryStr)
    aggregateData, averageToday, averageWeek = returnData
    buy = averageToday <= averageWeek
    diff = round(abs(averageToday - averageWeek), 2)
    bestThree = getBestThree(queryStr, averageWeek)
    itemOne, itemOneURL, itemOneName = bestThree[0][0], bestThree[0][1], bestThree[0][2]
    itemTwo, itemTwoURL, itemTwoName = bestThree[1][0], bestThree[1][1], bestThree[1][2]
    itemThree, itemThreeURL, itemThreeName = bestThree[2][0], bestThree[2][1], bestThree[2][2]
    context = {'wish': wish, 'aggregateData': aggregateData, 'averageToday': averageToday, 
      'averageWeek': averageWeek, 'buy': buy, 'diff': diff, 'itemOne': itemOne, 
      'itemOneURL': itemOneURL, 'itemTwo': itemTwo, 'itemTwoURL': itemTwoURL, 
      'itemThree': itemThree, 'itemThreeURL': itemThreeURL, 'itemOneName': itemOneName, 
      'itemTwoName': itemTwoName, 'itemThreeName': itemThreeName}
    return render(request, 'iWant/details.html', context)


def sign_out(request):
    logout(request)
    context = {}
    return render(request, 'iWant/index.html', context)



