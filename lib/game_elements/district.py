class District(object):
    def __init__(self, blocks):
        self.blocks = blocks
        self.locations = self.__getLocations()

    def __getLocations(self):
      locations = []
      for block in self.blocks:
        location.append(block.location)
      self.locations = locations
