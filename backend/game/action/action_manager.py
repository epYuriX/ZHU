# game/action/action_manager.py
class ActionManager:
    """
    动作分发
    """

    def __init__(self):
        self.actions = {}

    def select_role_cards(self, ident):
        """
        盖放[角色牌]
        :param ident:
        :return:
        """
        pass

    def get_available_role_cards(self, ident):
        """
        获取玩家可用[角色牌]
        :param ident:
        :return: 未在[角色牌弃牌区]中的[角色牌][]
        """
        return []
        pass
