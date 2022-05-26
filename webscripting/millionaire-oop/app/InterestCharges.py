
class InterestCharges():
    """
        @date 2022-05-26
        @author
    """

    # time need to reach 
    __timeInYears:int = 0

    # message / result will return
    __msg:str = None

    # money to start with
    __money:float = None

    # interest charges 
    __interestCharges:float = None

    #
    __interestRate:float = None
    # the default value for interestRate if failed to convert or something else 
    __defaultInterestRate:float = 1.01

    # old separator 
    __separatorOldValue:str = ','

    # new separator 
    __separatorNewValue:str = '.'

    __moneyMinimumValue:int|float = 0
    __moneyTargetValue:int|float = 1000000
    
    
    def __init__(self, money:str , interestCharges:str) -> None:
        """ constructor convert param to float an set them as class attributes
        """
        self.__money = self.convertMoneyToFloat(money)
        self.__interestCharges = self.convertInterestChargesToFloat(interestCharges)
  
    
    def calcTimeInYears(self) -> str:
        """ calculate the time in years for wanted to get the wanted money
        """
        #self.calculateInterestRate(self.__interestCharges)
        if not isinstance(self.__money, float):
            return 'money is not a float'
        if not isinstance(self.__interestRate, float):
            return 'interest charges is not float'
        if self.__money <= float(self.__moneyMinimumValue):
            return 'money is less or equal zero (money<=0)'
        result = self.__money
        while(float(result) <= float(self.__moneyTargetValue)):
            result = result * self.__interestRate
            self.__timeInYears = self.__timeInYears + 1
        return str(self.__timeInYears)


    def calculateInterestRate(self, interestCharges:float) -> float:
        """
        return default 1.01
        """
        if not isinstance(interestCharges, float):
            return self.__defaultInterestRate
        return (interestCharges / 100 + 1)


    def convertMoneyAndInterestChargesToFloat(self) -> None:
        """ call the methodes/functions: 
        \n  convertMoneyToFloat()
        \n  convertInterestChargesToFloat()
        """
        self.convertMoneyToFloat()
        self.convertInterestChargesToFloat()


    def convertMoneyToFloat(self, money:str) -> float:
        """ covert attribute "money" to a float attribute
        """
        try:
            if isinstance(money, str):
                money = money.replace(self.getSeparatorOldValue(),self.getSeparatorNewValue())
                return float(money)
            return 0
        except:
            self.setMsg('please enter a number')


    def convertInterestChargesToFloat(self, interestCharges:str) -> float:
        """ convert attribute "interestCharges" to float attribute,
            and calculate (interest / 100 + 1)
            except = set __interestCharges = None
            input "1" = output 1.01
        """
        try:
            if isinstance(interestCharges, float):
                return interestCharges
            if isinstance(interestCharges, str):
                self.__msg = 'interestCharges is a string'
                interestCharges = interestCharges.replace(self.getSeparatorOldValue(),self.getSeparatorNewValue())
            if interestCharges == '' or interestCharges == None:
                self.__msg == 'interestCharges is not set'
                return self.__defaultInterestRate
            interestCharges = float(interestCharges)
            if not isinstance(interestCharges,float):
                self.__msg = 'interestCharges is not a number'
                return self.__defaultInterestRate
            return interestCharges
            #self.__interestCharges = self.__interestCharges / 100 + 1
        except:
            self.setMsg('Interest charges not specified or not a number')
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
        if isinstance(moneyTargetValue,int):
            self.__moneyTargetValue = float(moneyTargetValue)
        elif isinstance(moneyTargetValue,float):
            self.__moneyTargetValue = moneyTargetValue


    def getMoneyTargetValue(self) -> float:
        return self.__moneyTargetValue

    def setMoneyMinimumValue(self,moneyMinimumValue:int|float) -> None:
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
        """ print all attributes from class InterestCharges
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


