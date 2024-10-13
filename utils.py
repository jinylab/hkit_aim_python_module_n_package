import math


def round_result(value, precision):
    """
    지정된 정밀도로 값을 반올림하는 함수입니다.
    
    Parameters:
    -----------
    value : float or int
        반올림할 값.
    precision : int
        소수점 이하 자릿수.
    
    Returns:
    --------
    float or int
        지정된 자릿수로 반올림된 값.
    """
    return round(value, precision)


def convert_to_radians(angle, unit="degree"):
    """
    주어진 단위의 각도를 라디안으로 변환하는 함수입니다.
    
    Parameters:
    -----------
    angle : float or int
        변환할 각도 값.
    unit : str, optional
        각도의 단위 ('degree' 또는 'gradian'). 기본값은 'degree'.
    
    Returns:
    --------
    float
        라디안 값.
    """
    if unit == 'degree':
        return math.radians(angle)  # degree를 radian으로 변환
    elif unit == 'gradian':
        return angle * (math.pi / 200)  # gradian을 radian으로 변환
    else:
        raise ValueError("unit must be 'degree' or 'gradian'")

# 파일 직접 실행시 데모
if __name__ == "__main__":
    print("round_result(3.14159, 2) #결과 : {0}".format(round_result(3.14159, 2)))  # 3.14 출력
    print("convert_to_radians(180, 'degree') #결과 : {0}".format(convert_to_radians(180, 'degree')))  # 3.14 출력
	