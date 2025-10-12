class Diamond:

    def __init__(self, side_a: int, angle_a: int):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == 'side_a':
            if not (isinstance(value, int) and value > 0):
                raise ValueError("Side must be a positive int")
            super().__setattr__('side_a', value)
            super().__setattr__('side_b', value)

        elif key == "angle_a":
            if not (isinstance(value, int) and 0 < value < 180):
                raise ValueError("Angle should be in range 0 < angle < 180")
            super().__setattr__('angle_a', value)
            super().__setattr__('angle_b', 180 - value)

        elif key == "angle_b":
            if not (isinstance(value, int) and 0 < value < 180):
                raise ValueError("Angle should be in range 0 < angle < 180")
            super().__setattr__('angle_b', value)
            super().__setattr__('angle_a', 180 - value)

        else:
            super().__setattr__(key, value)

    def __repr__(self):
        return (f"Diamond(side_a={self.side_a}, side_b={self.side_b}, "
                f"angle_a={self.angle_a}, angle_b={self.angle_b})")


def set_the_diamond():
    side = int(input("📏 Enter the side_a size:\n"))
    angle = int(input("📐 Enter the angle_a:\n"))
    print(Diamond(side_a=side, angle_a=angle))

def main():
    set_the_diamond()

if __name__ == "__main__":
    main()