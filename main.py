import pyray

fps = 0

def main():
    w, h = 800, 600
    pyray.init_window(w, h, 'test1')

    while not pyray.window_should_close():
        pyray.begin_drawing()
        pyray.end_drawing()
    pyray.close_window()

if __name__ == '__main__':
    main()