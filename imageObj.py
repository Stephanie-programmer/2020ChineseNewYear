class ImageObj:
    rotation_offset = 20
    position_offset = 30
    angle = 0
    direction = "l"

    def __init__(self, image, pos, hidden=False):
        self.hidden = hidden
        self.originalImage = image
        self.image = image
        self.pos = pos
