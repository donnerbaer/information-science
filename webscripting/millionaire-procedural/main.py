from bottle import route, run
from bottle import template, request


@route('')
@route('/')
def index():
    return template('app/index', money=None, interestCharges=None, msg=None)

@route('/', method='post')
def index():
    msg = None      #output message result/error
    try:
        money = request.forms.get('money')
        money = money.replace(',','.')
        money = float(money)
    except:
        msg='Money is not a number'

    try:
        interestCharges = request.forms.get('interestCharges')
        interestCharges = interestCharges.replace(',','.')
        interestCharges = float(interestCharges)
    except:
        msg='Interest rate not specified or not a number'

    if msg == None and money <= 0:
        msg = 'money is <= 0'
    if msg == None and isinstance(money, float) and isinstance(interestCharges, float):
        interestCharges = interestCharges / 100.0 + 1.00
        calculatedMoney = money
        timeInYears = 0
        while(int(calculatedMoney) < 1000000):
            calculatedMoney = calculatedMoney * interestCharges
            timeInYears = timeInYears + 1
        msg = timeInYears
    return template('app/index', money=money, interestCharges=interestCharges, msg=msg)


# #########     run     #####################
run(host='localhost', port=80, debug=True)