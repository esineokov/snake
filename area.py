class Area:
    def __init__(self, width: int = 700, height: int = 600, cell_size: int = 50):

        assert width % cell_size == 0 and height % cell_size == 0, "can't calc square size"

        self.width = width
        self.height = height
        self.cell_size = cell_size
