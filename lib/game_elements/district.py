class District(object):
    def __init__(self, blocks):
        self.blocks = blocks
        self.locations = self.__get_locations()

    def __get_locations(self):
      locations = []
      for block in self.blocks:
        locations.append(block.location)
      return locations

    def append(self, block):
      self.locations.append(block.location)
      return self.blocks.append(block)

    def inspect(self):
      return str(self.__get_locations()).strip('[]')
