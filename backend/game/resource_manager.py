# game / resource_manager.py
from .data import RESOURCE_CARDS
import random


class ResourceManager:
    """
    抽取资源卡
    """

    def __init__(self):
        self.pools = {
            "lv1": list(RESOURCE_CARDS["lv1"]),
            "lv2": list(RESOURCE_CARDS["lv2"]),
            "lv3": list(RESOURCE_CARDS["lv3"])
        }
        for lv in self.pools:
            random.shuffle(self.pools[lv])

    def draw_resource_card(self, lv: str):
        """
        抽卡
        :param lv:
        :return:
        """
        pool = self.pools.get(lv)
        if pool and len(pool) > 0:
            return pool.pop()
        return None
