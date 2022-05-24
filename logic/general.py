from items import itemlist


class node:
    def __init__(self, name, form, address, requirements):
        self.checkname = name                                 # the long name of the check
        self.form = form                                      # whether it's an item, an entrance, an event
        self.address = address                                # where it's memory address exists
         # may need to add address somehow else,
         # since not every node has a relevant address
        self.requirements = []                                # logical requirements to resolve/obtiain/pass through node


# Forms:
# "item-free"     - Freestanding, mainly the flowers
# "item-chest"    - Items found in a chest.  May include chest gems in the future.
# "item-npc"      - Given from an NPC conversation, sans moneybags. 
# "item-money"    - Purchased from moneybags.
# "item-fight"    - Found after a boss fight (FL worm, Ripto, Fast Eddie (?))
# "item-mini"     - Found after a minigame (Sgt. Byrd, Agent 9, bombing run, whack-a-mole, etc)

# "entrance"      - An entrance
# "event"         - A task that opens up more of the world



for self in itemlist:
    if self.itemtype == "ability":
        print(self.short)