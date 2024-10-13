# calculator 패키지
기본 계산기 및 공학용 계산기 기능을 제공하는 Python 패키지입니다.

## 목차

* [기능](#기능)
* [사용법](#사용법)
  * [패키지 임포트](#패키지-임포트)
  * [일반 계산기](#일반-계산기)
  * [공학용 계산기](#공학용-계산기)
  * [유틸리티 함수](#유틸리티-함수)
* [라이선스](#라이선스)

## 기능

- **Calculator**: 기본 사칙연산이 가능한 계산기.
- **EngineeringCalculator**: 기본 사칙연산과 거듭제곱, 삼각함수 등 고급 수학 계산이 가능한 공학용 계산기.
- **Utils**: 반올림 함수와 각도를 라디안으로 변환하는 함수 등을 포함하는 유틸리티 함수.

## 사용법
### 패키지 임포트
```python
from calculator import (
    Calculator,
    EngineeringCalculator,
    round_result,
    convert_to_radians
)
```

### 일반 계산기
```python
calc = Calculator(precision=2, return_float=True)
sum_result = calc.add(10, 5)
difference = calc.subtract(10, 5)
product = calc.multiply(10, 5)
quotient = calc.divide(10, 2)

print(sum_result)    # 15.0
print(difference)    # 5.0
print(product)       # 50.0
print(quotient)      # 5.0
```

### 공학용 계산기
```python
import math
from calculator import EngineeringCalculator, DivisionByZeroError

eng_calc = EngineeringCalculator(precision=4, return_float=True)

# divide
try:
    result = eng_calc.divide(10, 2)
    print(result)  # 5.0

    eng_calc.divide(10, 0)
except DivisionByZeroError as e:
    print(e)  # 0으로 나눌 수 없습니다.

# 제곱근
sqrt_result = eng_calc.square_root(16)
print(sqrt_result)  # 4.0

# 제곱
power_result = eng_calc.power(2, 3)
print(power_result)  # 8.0

# 로그
log_result = eng_calc.log(100, base=10)
print(log_result)  # 2.0

# 자연로그
ln_result = eng_calc.ln(math.e)
print(ln_result)  # 1.0

# 사인
sin_result = eng_calc.sin(math.pi / 2)
print(sin_result)  # 1.0

# 코사인
cos_result = eng_calc.cos(180, angle_unit='degree')
print(cos_result)  # -1.0

# 탄젠트
tan_result = eng_calc.tan(45, angle_unit='degree')
print(tan_result)  # 1.0
```

### 유틸리티 함수
```python
from calculator import round_result, convert_to_radians

# 반올림
rounded_value = round_result(3.14159, 2)
print(rounded_value)  # 3.14

# degree 또는 gradian을 radian으로 변환
radians_deg = convert_to_radians(180, 'degree')
print(radians_deg)  # 3.141592653589793
radians_grad = convert_to_radians(200, 'gradian')
print(radians_grad)  # 3.141592653589793
```

## 라이선스
This project is licensed under the MIT License.







