#게임월드 관리모듈

#게임월드의 표현

objects = []

#월드에 객체를 넣는 함수

def add(o):
    objects.append(o)

#월드를 업데이트하는 업데이트 하는 함수

def update():
    for o in objects:
        o.update()

#월드객체 모두 그리기 함수

def render():
    for o in objects:
        o.draw()


