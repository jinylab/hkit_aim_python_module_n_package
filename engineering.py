import math
from basic import Calculator

# 사용자예외
class DivisionByZeroError(Exception):
    '''예외 : 0으로 나누기'''
    pass

# 공학용 계산기
class EngineeringCalculator(Calculator):
    """
    고급연산 수행을 휘한 공학용 계산기 클래스 입니다.
    
    Attributes:
    -----------
    default_precision : int or None
        결과값의 소수점 자릿수 (None일 경우 소수점 자릿수 조정 없음).
    default_return_float : bool
        True일 경우 결과값을 float 타입으로 반환합니다 (기본값: False).
    
    Methods:
    --------
    square_root(x, **kwargs):
        주어진 수의 제곱근을 계산합니다.
    
    power(x, y, **kwargs):
        x의 y제곱을 계산합니다.
    
    log(x, base=10, **kwargs):
        주어진 밑(base)에 대한 로그를 계산합니다.
    
    ln(x, **kwargs):
        자연 로그를 계산합니다.
    
    sin(x, **kwargs):
        주어진 각도의 사인 값을 계산합니다.
    
    cos(x, **kwargs):
        주어진 각도의 코사인 값을 계산합니다.
    
    tan(x, **kwargs):
        주어진 각도의 탄젠트 값을 계산합니다.
    """
    
    def __init__(self, precision: int = None, return_float: bool = False):
        """
        EngineeringCalculator 클래스의 생성자.
        
        Parameters:
        -----------
        precision : int, optional
            결과값의 소수점 자릿수 (기본값: None)
        return_float : bool, optional
            True일 경우 결과값을 float 타입으로 반환합니다 (기본값: False)
        """
        super().__init__(precision, return_float)
    
    def divide(self, *args, **kwargs):
        """
        여러 숫자를 나누는 메서드입니다. 0으로 나눌 경우 예외를 발생시킵니다.
        
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
            raise ValueError("Error: 2개 이상의 값을 입력해야 합니다.")
    
        precision = kwargs.get('precision', self.default_precision)
        return_float = kwargs.get('return_float', self.default_return_float)
    
        result = args[0]
        for num in args[1:]:
            if num == 0:
                raise DivisionByZeroError("Error: 0으로 나눌 수 없습니다.")
            result /= num
    
        if precision is not None and isinstance(precision, int):
            result = round(result, precision)
    
        if return_float:
            result = float(result)
    
        return result
    
    def square_root(self, x, **kwargs):
        """
        주어진 수의 제곱근을 계산하는 메서드입니다.
        
        Parameters:
        -----------
        x : float or int
            제곱근을 계산할 값.
        **kwargs : dict
            precision (int): 소수점 자릿수 (기본값: None).
            return_float (bool): True일 경우 결과를 float으로 반환합니다 (기본값: False).
        
        Returns:
        --------
        float or int
            제곱근 결과값.
        """
        if x < 0:
            raise ValueError("Error: 입력값은 0보다 커야합니다.")
    
        precision = kwargs.get('precision', self.default_precision)
        return_float = kwargs.get('return_float', self.default_return_float)
    
        result = math.sqrt(x)
    
        if precision is not None and isinstance(precision, int):
            result = round(result, precision)
    
        if return_float:
            result = float(result)
    
        return result
    
    def power(self, x, y, **kwargs):
        """
        x의 y제곱을 계산하는 메서드입니다.
        
        Parameters:
        -----------
        x : float or int
            밑값.
        y : float or int
            지수값.
        **kwargs : dict
            precision (int): 소수점 자릿수 (기본값: None).
            return_float (bool): True일 경우 결과를 float으로 반환합니다 (기본값: False).
        
        Returns:
        --------
        float or int
            제곱 결과값.
        """
        precision = kwargs.get('precision', self.default_precision)
        return_float = kwargs.get('return_float', self.default_return_float)
    
        result = math.pow(x, y)
    
        if precision is not None and isinstance(precision, int):
            result = round(result, precision)
    
        if return_float:
            result = float(result)
    
        return result
    
    def log(self, x, base=10, **kwargs):
        """
        주어진 밑(base)에 대한 로그를 계산하는 메서드입니다.
        
        Parameters:
        -----------
        x : float or int
            로그를 계산할 값.
        base : float or int, optional
            로그의 밑 (기본값: 10).
        **kwargs : dict
            precision (int): 소수점 자릿수 (기본값: None).
            return_float (bool): True일 경우 결과를 float으로 반환합니다 (기본값: False).
        
        Returns:
        --------
        float or int
            로그 결과값.
        """
        if x <= 0:
            raise ValueError("Error: 입력값은 0보다 커야합니다.")
    
        precision = kwargs.get('precision', self.default_precision)
        return_float = kwargs.get('return_float', self.default_return_float)
    
        result = math.log(x, base)
    
        if precision is not None and isinstance(precision, int):
            result = round(result, precision)
    
        if return_float:
            result = float(result)
    
        return result
    
    def ln(self, x, **kwargs):
        """
        자연 로그(밑이 e인 로그)를 계산하는 메서드입니다.
        
        Parameters:
        -----------
        x : float or int
            자연 로그를 계산할 값.
        **kwargs : dict
            precision (int): 소수점 자릿수 (기본값: None).
            return_float (bool): True일 경우 결과를 float으로 반환합니다 (기본값: False).
        
        Returns:
        --------
        float or int
            자연 로그 결과값.
        """
        if x <= 0:
            raise ValueError("Error: 입력값은 0보다 커야합니다.")
    
        precision = kwargs.get('precision', self.default_precision)
        return_float = kwargs.get('return_float', self.default_return_float)
    
        result = math.log(x)  # 자연로그는 base가 e입니다.
    
        if precision is not None and isinstance(precision, int):
            result = round(result, precision)
    
        if return_float:
            result = float(result)
    
        return result
    
    def sin(self, x, **kwargs):
        """
        주어진 각도의 사인 값을 계산하는 메서드입니다.
        
        Parameters:
        -----------
        x : float or int
            사인을 계산할 각도.
        **kwargs : dict
            precision (int): 소수점 자릿수 (기본값: None).
            return_float (bool): True일 경우 결과를 float으로 반환합니다 (기본값: False).
            angle_unit (str): 각도의 단위 ('radian' 또는 'degree', 기본값: 'radian').
        
        Returns:
        --------
        float or int
            사인 결과값.
        """
        precision = kwargs.get('precision', self.default_precision)
        return_float = kwargs.get('return_float', self.default_return_float)
        angle_unit = kwargs.get('angle_unit', 'radian')
    
        if angle_unit == 'degree':
            x = math.radians(x)
    
        result = math.sin(x)
    
        if precision is not None and isinstance(precision, int):
            result = round(result, precision)
    
        if return_float:
            result = float(result)
    
        return result
    
    def cos(self, x, **kwargs):
        """
        주어진 각도의 코사인 값을 계산하는 메서드입니다.
        
        Parameters:
        -----------
        x : float or int
            코사인을 계산할 각도.
        **kwargs : dict
            precision (int): 소수점 자릿수 (기본값: None).
            return_float (bool): True일 경우 결과를 float으로 반환합니다 (기본값: False).
            angle_unit (str): 각도의 단위 ('radian' 또는 'degree', 기본값: 'radian').
        
        Returns:
        --------
        float or int
            코사인 결과값.
        """
        precision = kwargs.get('precision', self.default_precision)
        return_float = kwargs.get('return_float', self.default_return_float)
        angle_unit = kwargs.get('angle_unit', 'radian')
    
        if angle_unit == 'degree':
            x = math.radians(x)
    
        result = math.cos(x)
    
        if precision is not None and isinstance(precision, int):
            result = round(result, precision)
    
        if return_float:
            result = float(result)
    
        return result
    
    def tan(self, x, **kwargs):
        """
        주어진 각도의 탄젠트 값을 계산하는 메서드입니다.
        
        Parameters:
        -----------
        x : float or int
            탄젠트를 계산할 각도.
        **kwargs : dict
            precision (int): 소수점 자릿수 (기본값: None).
            return_float (bool): True일 경우 결과를 float으로 반환합니다 (기본값: False).
            angle_unit (str): 각도의 단위 ('radian' 또는 'degree', 기본값: 'radian').
        
        Returns:
        --------
        float or int
            탄젠트 결과값.
        """
        precision = kwargs.get('precision', self.default_precision)
        return_float = kwargs.get('return_float', self.default_return_float)
        angle_unit = kwargs.get('angle_unit', 'radian')
    
        if angle_unit == 'degree':
            x = math.radians(x)
    
        result = math.tan(x)
    
        if precision is not None and isinstance(precision, int):
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

    eng_calc = EngineeringCalculator()
    print("\nEngineering Calculator Demo:")
    print("eng_calc = EngineeringCalculator()")
    print("eng_calc.square_root(16) #결과 : {0}".format(eng_calc.square_root(16)))
    print("eng_calc.power(2, 3) #결과 : {0}".format(eng_calc.power(2, 3)))
    print("eng_calc.log(8, base=2) #결과 : {0}".format(eng_calc.log(8, base=2)))
    print("eng_calc.ln(1) #결과 : {0}".format(eng_calc.ln(1)))
    print("eng_calc.sin(30) #결과 : {0}".format(eng_calc.sin(30)))
    print("eng_calc.cos(60) #결과 : {0}".format(eng_calc.cos(60)))
    print("eng_calc.tan(45) #결과 : {0}".format(eng_calc.tan(45)))

    print("\nDivisionByZeroError 예외 처리 예제")
    print_str = """
try:
    print(eng_calc.divide(100, 5, 0))
except DivisionByZeroError as e:
    print(e)  # "Error: 0으로 나눌 수 없습니다.."
"""
    print(f"{print_str}")