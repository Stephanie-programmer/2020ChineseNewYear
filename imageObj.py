class ImageObj:
    rotation_offset = 20
    position_offset = 30

    def __init__(self, image, pos, rotation, direction, hidden=False):
        self.hidden = hidden
        self.image = image
        self.pos = pos
        self.rotation = rotation
        self.direction = direction
