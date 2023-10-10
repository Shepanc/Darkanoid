import pyray
import Managers


def main():
    fps = 0
    appManager = Managers.AppManager()

    appManager.Initialization()
    while not pyray.window_should_close():
        if fps % 60000 == 0:
            appManager.Update()
            appManager.Draw()
        fps += 1
    pyray.close_window()

if __name__ == '__main__':
    main()