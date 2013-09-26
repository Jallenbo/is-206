import rooms

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n--------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
			
class Map(object):

    scenes = {
        'galtvang': rooms.Galtvang(),
        'bokhandel': rooms.Bokhandel(),
        'bank': rooms.Bank(),
        'galtvort': rooms.Galtvort()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)
		
a_map = Map('galtvang')
a_game = Engine(a_map)
a_game.play()