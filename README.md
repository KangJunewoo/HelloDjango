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

### customizing user
- config는 마스터폴더같은거.
- 나머지는 application
  - application은 function들의 group
  - users에서 models와 admin을 커스터마이징할 수 있다.
- model은 fields로 이루어짐.
  - 다양한 종류의 필드들.
  - 유효성검사까지 장고가 알아서 다해줌.
  - 필드를 정의한 파이썬 코드는 django orm을 통해 sql로 만들어져 db에 들어감.
- 모델을 직접 보려면 admin 패널에서 가능했지.
  - admin.py에서 모델을 등록하려.면 register를 했어야 했음. 데코레이터 사용했던거!
  - admin 패널의 배치를 바꾸는 것도 파이썬을 만지면 됨. fieldsets 같은거!(그 파란색 소제목)
    - list_display도 있었고.
    - list_filter도 있었고
- AbstractUser 상속하는 부분은 일단 외우자.
- /config/settings에 등록해주기
  - users.apps.UsersConfig 등록했었지.
  - AUTH_USER_MODEL = "users.User" 넣어서 우리가 만든 User를 쓴다고 알려줬었어.
  - 일반 장고 유저모델도 대부분의 경우엔 충-분히 쓸만하다.
  - 
## tips
### user모델 변경하려고 할 때 migration 순서 오류
최대한 순수한 상태로 돌아가
```
python manage.py migrate admin zero
python manage.py migrate auth zero
python manage.py migrate contenttypes zero
python manage.py migrate sessions zero
```
로 싹 초기화해준 담에 진행.

### 데이터 비우는 방법
- db, pycache, migrations 모두 삭제한 뒤
- makemigrations, migrate 적용.
- migration은 최대한 적게 해주는게 좋다.