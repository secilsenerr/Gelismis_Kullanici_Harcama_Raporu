""" Bu uygulamada mantiksal hatalari yakalamak icin Exception sinifi turetilerek bir BudgetBaseException olusturulmustur. 
    Eger bekledigimiz (orn. butce limitinin asilmasi) bir uyari kullaniciya verilmek isteniyorsa asagida belirtilen uyari siniflari kullanilabilir.

    Test fonksiyonunda bu exception'lar yakalandiginda kullaniciya uyari vererek cikabiliriz.

    
"""

class BudgetBaseException(Exception):
    pass

class BudgetLimitExceededError(BudgetBaseException):
    pass

class CategoryMismatchError(BudgetBaseException):
    pass