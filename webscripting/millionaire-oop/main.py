from bottle import route, run
from bottle import template, request
import app.InterestCharges as aIC


@route('')
@route('/')
def becomeAMillionaire():
    return template('app/millionaire', money=None, interestCharges=None,msg=None)


@route('/', method='post')
def becomeAMillionaire():
    """
    calculate the time in years for wanted to get the wanted money
    """
    #get formular data
    money = request.forms.get('money')
    interestCharges = request.forms.get('interestCharges')
    #create a new object from InterestCharges()
    IC = aIC.InterestCharges(money,interestCharges)
    interestRate = IC.calculateInterestRate(IC.getInterestCharges())
    IC.setInterestRate(interestRate)
    if IC.isCalcTimeInYearsPossible():
        IC.setMsg(IC.calcTimeInYears())
    else:
        IC.setMsg(IC.isCalcTimeInYearsPossibleProblemHandling())
    return template('app/millionaire', money = IC.getMoney(), interestCharges = IC.getInterestRate(), msg = IC.getMsg())


# #########     run     #####################
run(host='localhost', port=80, debug=True)