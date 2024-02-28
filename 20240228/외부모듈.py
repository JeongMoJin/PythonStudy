# 외부 모듈의 이용
# 1. 패키지
# 모듈의 상위 개념. 모듈의 집합을 의미
# 파이썬에서 기본적으로 제공하지 않더라도 외부에서 만들어진 패키지를 이용하면
# 패키지에 포함된 모듈을 사용할 수 있음

# 2. 패키지 관리자
# 외부 모듈을 사용하기 위해서는 우선 모듈이 포함된 패키지를 추가로 설치
# pip라고 불리는 패키지 관리자를 사용해서 패키지를 추가나 삭제

# 3. 패키지 설치
# 1) 터미널 창에
# pip install packge

# 2)
# 메뉴 File > Setting > Python Interpreter > +
# > numpy 검색 > 설치

# numpy 패키지는 수치해석과 통계에서 많이 사용
# pip install numpy

import numpy as np
print(np.sum([1,2,3,4,5])) # 15

# 4. 패키지 삭제
# pip uninstall package
# 예) pip uninstall numpy