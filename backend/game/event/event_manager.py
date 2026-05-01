# game/event/event_manager.py
from .events import EVENTS
import random


class EventManager:
    """
    抽取资源卡
    """

    def __init__(self):
        self.pools = {
            "lv1": list(EVENTS["lv1"]),
            "lv2": list(EVENTS["lv2"]),
            "lv3": list(EVENTS["lv3"])
        }
        for lv in self.pools:
            random.shuffle(self.pools[lv])

    def draw_resource_card(self, lv: str):
        """
        抽卡，抽完不放回
        :param lv:
        :return:
        """
        pool = self.pools.get(lv)
        if pool and len(pool) > 0:
            return pool.pop()
        return None
