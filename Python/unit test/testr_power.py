from powerr import square
from powerr import cube
def main():
    testr_power()

def testr_power():
        assert square(2) == 4
def testr_power2():
        assert cube(2) == 8

if __name__ == "__main__":
    main()