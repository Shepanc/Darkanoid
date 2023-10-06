import pyray

# Глобальные поля
fps = 0
items = []


def update():
    pass

def draw():
    pyray.begin_drawing()
    pyray.end_drawing()

def main():
    w, h = 800, 600
    pyray.init_window(w, h, 'test1')

    while not pyray.window_should_close():
        if fps % 60 == 0:
            update()
            draw()
    pyray.close_window()

if __name__ == '__main__':
    main()