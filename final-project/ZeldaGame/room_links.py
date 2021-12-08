class RoomLinks:
    opposites = {'left':'right','right':'left','up':'down','down':'up'}
    def __init__(self,room_id):
        self.links = {'left':None,'right':None,'up':None,'down':None}
        self.room_id = room_id
    def link_room(self,d,room):
        self.links[d] = room
        room.links[self.opposites[d]] = self