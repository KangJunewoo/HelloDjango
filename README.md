# HelloDjango
장고 이번엔 제대로 배우고 끝내자 with nomad challenge

## 1일차
퀴즈풀고 끝

## 2일차
### pipenv 설치해야 하는 이유
파이썬의 pip는 npm --global과 같다. 다 전역으로 설치되는 게 싫어서 pipenv를 설치함.
```
% brew pipenv
```
로 설치하고

```
% pipenv --three
```
로 가상환경을 만들며


```
% pipenv shell
```
로 활성화한 뒤

```
% pipenv install django
```
식으로 설치한다~  
linter는 flake8 formatter는 black을 쓰고 있구나.  
처음 써봐서 좋은 지는 잘 모르겠다.  
또한 장고 공홈을 보는 습관을 들이자.  

## 에러고치면서 배우기
### user모델 변경하려고 할 때 migration 순서 오류
최대한 순수한 상태로 돌아가
```
python manage.py migrate admin zero
python manage.py migrate auth zero
python manage.py migrate contenttypes zero
python manage.py migrate sessions zero
```
로 싹 초기화해준 담에 진행.