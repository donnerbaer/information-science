
class InterestCharges():
    """
        establishes methods for calculating interest
        @author
        @date 2022-05-26  
    """

    # time need to reach 
    __timeInYears:int = 0

    # message / result will return
    __msg:str = None

    # money to start with
    __money:float = None

    # interest charges 
    __interestCharges:float = None

    #interest rate 1.01 = +1%
    __interestRate:float = None

    # the default value for interestRate, if failed to convert or something else 
    __defaultInterestRate:float = 1.01

    # old separator that will be replaced by __separatorNewValue
    __separatorOldValue:str = ','

    # new separator that will replace __separatorOldValue
    __separatorNewValue:str = '.'

    #minimum start value for money
    __moneyMinimumValue:int|float = 0

    #money target value you want to have
    __moneyTargetValue:int|float = 1000000
    
    
    def __init__(self, money:str , interestCharges:str) -> None:
        """ 
            constructor convert param to float an set them as class attributes
            @param money you will start with
            @param interestCharges interest charge
        """
        self.__money = self.convertMoneyToFloat(money)
        self.__interestCharges = self.convertInterestChargesToFloat(interestCharges)
  
    
    def calcTimeInYears(self) -> str:
        """ 
            calculate the time in years for wanted to get the wanted money
            @return timeInYears : str
        """
        result = self.__money
        while(float(result) <= float(self.__moneyTargetValue)):
            result = result * self.__interestRate
            self.__timeInYears = self.__timeInYears + 1
        return str(self.__timeInYears)


    def isCalcTimeInYearsPossible(self) -> bool:
        """
            check if calc __timeInYears is possible
            @return True if possible
        """
        if not isinstance(self.__money, float):
            return False
        if not isinstance(self.__interestRate, float):
            return False
        if self.__money <= float(self.__moneyMinimumValue):
            return False
        return True


    def isCalcTimeInYearsPossibleProblemHandling(self) -> str:
        """
            @return message : str with the problem
        """
        if not isinstance(self.__money, float):
            return 'money is not a number'
        if not isinstance(self.__interestRate, float):
            return 'interest charges is not number'
        if self.__money <= float(self.__moneyMinimumValue):
            return 'money is less or equal zero (money<=0)'


    def calculateInterestRate(self, interestCharges:float) -> float:
        """
            \n@param interestCharges:float 
            \n@return interestCharges:float
            \nNote: !attention: with 0 {Zero} you will run into an endless loop
            \n-1 -> 0.99
            \n0 -> 1.00 
            \n1 -> 1.01
            \nif interestCharges not a float it will return __defaultInterestRate
            \ncalculation (interestCharges / 100 + 1)
        """
        if not isinstance(interestCharges, float):
            return self.__defaultInterestRate
        return (interestCharges / 100 + 1)


    def convertMoneyToFloat(self, money:str) -> float:
        """ 
            \ncovert attribute "money" to a float attribute
            \n@param money:str you want to convert to a float
            \n@return money:float 
            
            \ntrim param spaces at start and end
            \nmethod will replace string __separatorOldValue with __separatorNewValue
            \nif convert will fail, return 0
        """
        try:
            if isinstance(money, float):
                return money
            if isinstance(money, int):
                return float(money)
            if isinstance(money, str):
                money = money.strip()
                money = money.replace(self.__separatorOldValue,self.__separatorNewValue)
                return float(money)
        except:
            self.__msg = 'please enter a number'


    def convertInterestChargesToFloat(self, interestCharges:str) -> float:
        """ 
            \nconvert attribute "interestCharges" to float attribute
            \n@param interestCharges : str
            \n@return interestCharges : float
            \ncalculation (interest / 100 + 1)
            \ninput "1" = output 1.01
            \ntrim param spaces at start and end
            \nmethod will replace string __separatorOldValue with __separatorNewValue
            \nif convert will fail, return __defaultInterestRate
        """
        try:
            if isinstance(interestCharges, float):
                return interestCharges
            if isinstance(interestCharges, str):
                interestCharges = interestCharges.strip()
                interestCharges = interestCharges.replace(self.__separatorOldValue,self.__separatorNewValue)
            if interestCharges == '' or interestCharges == None:
                self.__msg == 'interestCharges is not set or empty'
                return self.__defaultInterestRate
            interestCharges = float(interestCharges)
            if not isinstance(interestCharges,float):
                self.__msg = 'interestCharges is not a number'
                return self.__defaultInterestRate
            return interestCharges
        except:
            self.__msg = 'interestCharges not specified or not a number'
            return self.__defaultInterestRate


    def setTimeInYears(self,timeInYears:int) -> None:
        self.__timeInYears = timeInYears


    def getTimeInYears(self) -> int:
        return self.__timeInYears


    def setMsg(self,msg:str) -> None:
        self.__msg = msg


    def getMsg(self) -> str:
        return self.__msg


    def setMoney(self,money:float) -> None:
        self.__money = money


    def getMoney(self) -> float:
        return self.__money


    def setInterestRate(self, interestRate:float) -> None:
        self.__interestRate = interestRate


    def getInterestRate(self) -> float:
        return self.__interestRate


    def setInterestCharges(self, interestCharges:float) -> None:
        self.__interestCharges = interestCharges


    def getInterestCharges(self) -> float:
        return self.__interestCharges


    def setSeparatorOldValue(self, separatorOldValue:str) -> None:
        self.__separatorOldValue = separatorOldValue


    def getSeparatorOldValue(self) -> str:
        return self.__separatorOldValue


    def setSeparatorNewValue(self, separatorNewValue:str) -> None:
        self.__separatorNewValue = separatorNewValue


    def getSeparatorNewValue(self) -> str:
        return self.__separatorNewValue


    def setMoneyTargetValue(self, moneyTargetValue:int|float) -> None:
        """
            set moneyTargetValue : int|float as __moneyTargetValue : float
            @param moneyTargetValue:int|float
        """
        if isinstance(moneyTargetValue,int):
            self.__moneyTargetValue = float(moneyTargetValue)
        elif isinstance(moneyTargetValue,float):
            self.__moneyTargetValue = moneyTargetValue


    def getMoneyTargetValue(self) -> float:
        return self.__moneyTargetValue


    def setMoneyMinimumValue(self,moneyMinimumValue:int|float) -> None:
        """
            set moneyMinimumValue : int|float as __moneyMinimumValue : float
            @param moneyMinimumValue:int|float
        """
        if isinstance(moneyMinimumValue,int):
            self.__moneyMinimumValue = float(moneyMinimumValue)
        elif isinstance(moneyMinimumValue,float):
            self.__moneyMinimumValue = moneyMinimumValue


    def getMoneyMinimumValue(self) -> int|float:
        return self.__moneyMinimumValue


    def setDefaultInterestRate(self, interestRate:float) -> None:
        self.__defaultInterestRate = interestRate


    def getDefaultInterestRate(self) -> float:
        return self.__defaultInterestRate


    def printAll(self) -> None:
        """ 
            print all attributes from class InterestCharges in console
        """
        print('\t__timeInYears='+str(self.__timeInYears))
        print('\t__money='+str(self.__money))
        print('\t__interestCharges='+str(self.__interestCharges))
        print('\__interestRate='+str(self.__interestRate))
        print('\t__msg='+str(self.__msg))
        print('\t__separatorOldValue='+str(self.__separatorOldValue))
        print('\t__separatorNewValue='+str(self.__separatorNewValue))
        print('\t__moneyMinimumValue='+str(self.__moneyMinimumValue))
        print('\t__moneyTargetValue='+str(self.__moneyTargetValue))


