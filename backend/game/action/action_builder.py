# game/engine/action_builder.py
class Action:
    """
    玩家行动类
        action_cnt: 主要行动使用次数
        skill_cnt: 角色技能使用次数
        skill_1_cnt: 策略使用次数
        skill_2_cnt: 计谋使用次数
    玩家行动说明
        主要行动 (6选1)
            部署: [放置影响力]
            调度: [移动自己的一个影响力] * 2
            探索: 支付路费, 结算事件, 在目标资源点放置一个影响力
            城市移动: 支付[源石] * 3, 移动玩家至相邻资源点
            建设: 支付费用, 放置设施牌, 结算分数, 结算设施牌入场效果
            特殊行动: 使用已宣告的城市样式牌所解锁的特殊行动
        快速行动 (主要行动前后，任意次数)
            使用角色牌: 翻开自己盖放的角色牌, 选择牌上的效果发动
            宣告城市样式: 用已建设的设施满足宣告条件, 每个设施只能用 1 次
    """

    def __init__(self):
        self.action_cnt = 0
        self.skill_cnt = 0
        self.skill_1_cnt = 0
        self.skill_2_cnt = 0
        pass

    def deploy(self):
        """
        部署
        :return:
        """
        self.action_cnt += 1
        pass

    def dispatch(self):
        """
        调度
        :return:
        """
        self.action_cnt += 1
        pass

    def explore(self):
        """
        探索
        :return:
        """
        self.action_cnt += 1
        pass

    def move(self):
        """
        移动
        :return:
        """
        self.action_cnt += 1
        pass

    def build(self):
        """
        建设
        :return:
        """
        self.action_cnt += 1
        pass

    def special(self):
        """
        特殊行动
        :return:
        """
        self.action_cnt += 1
        pass

    def skill(self):
        """
        使用角色牌
        :return:
        """
        self.skill_cnt += 1
        pass

    def declare(self):
        """
        宣告城市样式
        :return:
        """
        pass
