# game / resource_manager.py
from .data import RESOURCE_CARDS
import random


class ResourceManager:
    def __init__(self):
        self.pools = {
            "lv1": RESOURCE_CARDS["lv1"].copy(),
            "lv2": RESOURCE_CARDS["lv2"].copy(),
            "lv3": RESOURCE_CARDS["lv3"].copy(),
        }
        for level in self.pools:
            random.shuffle(self.pools[level])

    def draw_resource_card(self, level: str):
        """
        抽卡
        :param level:
        :return:
        """
        if self.pools.get(level):
            return self.pools[level].pop()
        return None
