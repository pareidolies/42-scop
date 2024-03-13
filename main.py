import sys

class OpenGLApp:
    def __init__(self):
        pass

    def run(self, path):
        pass

def main():
    if len(sys.argv) != 2:
        print("Usage: {} \"path/to/file.obj\"".format(sys.argv[0]))
        return 1

    app = OpenGLApp()

    try:
        app.run(sys.argv[1])
    except Exception as e:
        print(e)
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
