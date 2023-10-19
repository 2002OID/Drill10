#게임월드 관리모듈

#게임월드의 표현

objects = [[],[]]

#월드에 객체를 넣는 함수

def add_object(o, depth=0):
    objects[depth].append(o)


def add_objects(ol, depth=1):
    objects[depth] += ol
#월드를 업데이트하는 업데이트 하는 함수

def update():
    for layer in objects:
        for o in layer:
            o.update()


#월드객체 모두 그리기 함수

def render():
    for layer in objects:
        for o in layer:
            o.draw()
#객체 삭제
def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('Cannot delete non existing object')
