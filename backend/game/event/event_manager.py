# game/event/event_manager.py
from .events import EVENTS
import random


class EventManager:
    """
    抽取事件牌
    """

    def __init__(self):
        # 保存每个等级未抽过的事件列表
        self.unused_events = {
            lv: events.copy() for lv, events in EVENTS.items()
        }
        # 已抽取的事件记录
        self.used_events = {
            lv: [] for lv in EVENTS.keys()
        }

    def draw_event(self, lv: str, nid: str):
        """
        抽取一个事件
        :param lv: 事件等级
        :param nid: 节点id
        :return:
        """
        if lv not in self.unused_events:
            raise ValueError(f"事件等级 {lv} 不存在")
        if not self.unused_events[level]:
            print(f"等级 {lv} 的事件已全部抽完")
        event = random.choice(self.unused_events[lv])
        self.unused_events[lv].remove(event)
        self.used_events[lv].append(event)
        