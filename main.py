import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from bot import AglBot


run_game(maps.get("CatalystLE_NOAI"), [
    Bot(Race.Terran, AglBot()),
    Computer(Race.Random, Difficulty.VeryEasy)
], realtime=False)
