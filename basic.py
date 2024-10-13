class Calculator:
    """
    기본 사칙연산을 수행하는 계산기 클래스입니다.
    
    Attributes:
    -----------
    default_precision : int or None
        결과값의 소수점 자릿수 (None일 경우 소수점 자릿수 조정 없음).
    default_return_float : bool
        True일 경우 결과값을 float 타입으로 반환합니다 (기본값: False).
    
    Methods:
    --------
    add(*args, **kwargs):
        여러 숫자를 더한 결과를 반환합니다.
    
    subtract(*args, **kwargs):
        여러 숫자에서 첫 번째 값을 기준으로 나머지 값을 차감한 결과를 반환합니다.
    
    multiply(*args, **kwargs):
        여러 숫자를 곱한 결과를 반환합니다.
    
    divide(*args, **kwargs):
        첫 번째 값을 기준으로 나머지 값으로 나눈 결과를 반환합니다.
    """
    
    def __init__(self, precision: int = None, return_float: bool = False):
        """
        Calculator 클래스의 생성자.
        
        Parameters:
        -----------
        precision : int, optional
            결과값의 소수점 자릿수 (기본값: None)
        return_float : bool, optional
            True일 경우 결과값을 float 타입으로 반환합니다 (기본값: False)
        """
        self.default_precision = precision
        self.default_return_float = return_float

    def add(self, *args, **kwargs):
        """
        여러 숫자를 더하는 메서드입니다.
        
        Parameters:
        -----------
        *args : float or int
            더할 값들.
        **kwargs : dict
            precision (int): 소수점 자릿수 (기본값: None).
            return_float (bool): True일 경우 결과를 float으로 반환합니다 (기본값: False).
        
        Returns:
        --------
        float or int
            더한 결과값.
        """
        result = sum(args)
        precision = kwargs.get('precision', None)
        return_float = kwargs.get('return_float', False)

        if return_float:
            result = float(result)

        if precision is not None and isinstance(precision, int):
            result = round(result, precision)

        return result

    def subtract(self, *args, **kwargs):
        """
        여러 숫자를 빼는 메서드입니다.
        
        Parameters:
        -----------
        *args : float or int
            빼야 할 값들 (첫 번째 값에서 나머지 값을 뺌).
        **kwargs : dict
            precision (int): 소수점 자릿수 (기본값: None).
            return_float (bool): True일 경우 결과를 float으로 반환합니다 (기본값: False).
        
        Returns:
        --------
        float or int
            뺀 결과값.
        """
        if len(args) < 2:
            return "Error: 두 개 이상의 값이 있어야 합니다."

        result = args[0]
        for num in args[1:]:
            result -= num

        precision = kwargs.get('precision', None)
        return_float = kwargs.get('return_float', False)

        if precision is not None:
            result = round(result, precision)

        if return_float:
            result = float(result)

        return result

    def multiply(self, *args, **kwargs):
        """
        여러 숫자를 곱하는 메서드입니다.
        
        Parameters:
        -----------
        *args : float or int
            곱할 값들.
        **kwargs : dict
            precision (int): 소수점 자릿수 (기본값: None).
            return_float (bool): True일 경우 결과를 float으로 반환합니다 (기본값: False).
        
        Returns:
        --------
        float or int
            곱한 결과값.
        """
        if len(args) < 1:
            return "Error: 두 개 이상의 값이 있어야 합니다."

        result = 1
        for num in args:
            result *= num

        precision = kwargs.get('precision', None)
        return_float = kwargs.get('return_float', False)

        if precision is not None:
            result = round(result, precision)

        if return_float:
            result = float(result)

        return result

    def divide(self, *args, **kwargs):
        """
        여러 숫자를 나누는 메서드입니다.
        
        Parameters:
        -----------
        *args : float or int
            나눌 값들 (첫 번째 값에서 나머지 값을 나눔).
        **kwargs : dict
            precision (int): 소수점 자릿수 (기본값: None).
            return_float (bool): True일 경우 결과를 float으로 반환합니다 (기본값: False).
        
        Returns:
        --------
        float or int
            나눈 결과값.
        """
        if len(args) < 2:
            return "Error: 두 개 이상의 값이 있어야 합니다."

        result = args[0]
        for num in args[1:]:
            if num == 0:
                return "Error: 0으로 나눌 수 없습니다."
            result /= num

        precision = kwargs.get('precision', None)
        return_float = kwargs.get('return_float', False)

        if precision is not None:
            result = round(result, precision)

        if return_float:
            result = float(result)

        return result


# 파일 직접 실행시 데모
if __name__ == "__main__":
    # 데모 코드
    calc = Calculator()
    print("Basic Calculator Demo:")
    print("calc = Calculator()")
    print("calc.add(10, 5.1264, 3, precision=2, return_float=True) #결과 : {0}".format(calc.add(10, 5.1264, 3, precision=2, return_float=True)))
    print("calc.subtract(10, 5.1264, 3, precision=2, return_float=True) #결과 : {0}".format(calc.subtract(10, 5.1264, 3, precision=2, return_float=True)))
    print("calc.multiply(10.1234, 5.5678, precision=2, return_float=True) #결과 : {0}".format(calc.multiply(10.1234, 5.5678, precision=2, return_float=True)))
    print("calc.divide(100.1234, 5.5678, precision=2, return_float=True) #결과 : {0}".format(calc.divide(100.1234, 5.5678, precision=2, return_float=True)))
