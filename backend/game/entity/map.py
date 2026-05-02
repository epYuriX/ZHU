# game/entity/map.py
# 4人地图
NODE_DATAILS_4 = [
    {
        "id": 1,  # node id
        "type": "node",  # node - 资源点, link - 通道
        "lv": 1,  # node lv
        "name": "A-01",  # node name
        "area": "A",  # 所属区块
        "color": "#007BFF",  # 所属区颜色
        "resource": "null",  # 资源类型
        "resource_c": 0,  # 资源乘数
        "parking": "null",  # 存在玩家所属方
        "inf_c": 2,  # 影响力棋子容量
        "inf_1": "null",  # 影响力1所属方
        "inf_2": "null",  # 影响力2所属方
    },
    {
        "id": 2,
        "type": "node",
        "lv": 1,
        "name": "A-02",
        "area": "A",
        "color": "#007BFF",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 3,
        "type": "node",
        "lv": 2,
        "name": "A-03",
        "area": "A",
        "color": "#007BFF",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 4,
        "type": "node",
        "lv": 1,
        "name": "B-01",
        "area": "B",
        "color": "#FEA443",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 5,
        "type": "node",
        "lv": 1,
        "name": "B-02",
        "area": "B",
        "color": "#FEA443",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 6,
        "type": "node",
        "lv": 2,
        "name": "B-03",
        "area": "B",
        "color": "#FEA443",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 7,
        "type": "node",
        "lv": 1,
        "name": "C-01",
        "area": "C",
        "color": "#32C4BF",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 8,
        "type": "node",
        "lv": 2,
        "name": "C-02",
        "area": "C",
        "color": "#32C4BF",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 9,
        "type": "node",
        "lv": 2,
        "name": "C-03",
        "area": "C",
        "color": "#32C4BF",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 10,
        "type": "node",
        "lv": 2,
        "name": "D-01",
        "area": "D",
        "color": "#4508AC",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 11,
        "type": "node",
        "lv": 2,
        "name": "D-02",
        "area": "D",
        "color": "#4508AC",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 12,
        "type": "node",
        "lv": 2,
        "name": "D-03",
        "area": "D",
        "color": "#4508AC",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 13,
        "type": "node",
        "lv": 2,
        "name": "E-01",
        "area": "E",
        "color": "#F3FEB0",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 14,
        "type": "node",
        "lv": 3,
        "name": "E-02",
        "area": "E",
        "color": "#F3FEB0",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 15,
        "type": "node",
        "lv": 3,
        "name": "E-03",
        "area": "E",
        "color": "#F3FEB0",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 16,
        "type": "node",
        "lv": 3,
        "name": "F-01",
        "area": "F",
        "color": "#FF0000",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 17,
        "type": "node",
        "lv": 3,
        "name": "F-02",
        "area": "F",
        "color": "#FF0000",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 18,
        "type": "node",
        "lv": 3,
        "name": "F-03",
        "area": "F",
        "color": "#FF0000",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 19,
        "type": "node",
        "lv": 1,
        "name": "G-01",
        "area": "G",
        "color": "#236349",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 20,
        "type": "node",
        "lv": 2,
        "name": "G-02",
        "area": "G",
        "color": "#236349",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 21,
        "type": "node",
        "lv": 2,
        "name": "G-03",
        "area": "G",
        "color": "#236349",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 22,
        "type": "node",
        "lv": 3,
        "name": "G-04",
        "area": "G",
        "color": "#236349",
        "resource": "null",
        "resource_c": 0,
        "parking": "null",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        # A 区右侧通道节点
        "id": 23,
        "type": "link",
        "name": "A",
        "area": "A",
        "color": "#007BFF",
        "inf_c": 1,
        "inf_1": "null",
    },
    {
        # A 区左侧通道节点
        "id": 24,
        "type": "link",
        "name": "A",
        "area": "A",
        "color": "#007BFF",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        # B 区右侧通道节点
        "id": 25,
        "type": "link",
        "name": "B",
        "area": "B",
        "color": "#FEA443",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        # B 区左侧通道节点
        "id": 26,
        "type": "link",
        "name": "B",
        "area": "B",
        "color": "#FEA443",
        "inf_c": 1,
        "inf_1": "null",
    },
    {
        "id": 27,
        "type": "link",
        "name": "C",
        "area": "C",
        "color": "#32C4BF",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 28,
        "type": "link",
        "name": "C",
        "area": "C",
        "color": "#32C4BF",
        "inf_c": 1,
        "inf_1": "null",
    },

    {
        "id": 29,
        "type": "link",
        "name": "D",
        "area": "D",
        "color": "#4508AC",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 30,
        "type": "link",
        "name": "D",
        "area": "D",
        "color": "#4508AC",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },

    {
        "id": 31,
        "type": "link",
        "name": "E",
        "area": "E",
        "color": "#F3FEB0",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 32,
        "type": "link",
        "name": "E",
        "area": "E",
        "color": "#F3FEB0",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },

    {
        "id": 33,
        "type": "link",
        "name": "F",
        "area": "F",
        "color": "#FF0000",
        "inf_c": 1,
        "inf_1": "null",
    },
    {
        "id": 34,
        "type": "link",
        "name": "F",
        "area": "F",
        "color": "#FF0000",
        "inf_c": 1,
        "inf_1": "null",
    },
    {
        "id": 35,
        "type": "link",
        "name": "F",
        "area": "F",
        "color": "#FF0000",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },

    {
        "id": 36,
        "type": "link",
        "name": "G",
        "area": "G",
        "color": "#236349",
        "inf_c": 1,
        "inf_1": "null",
    },
    {
        "id": 37,
        "type": "link",
        "name": "G",
        "area": "G",
        "color": "#236349",
        "inf_c": 1,
        "inf_1": "null",
    },
    {
        "id": 38,
        "type": "link",
        "name": "F",
        "area": "F",
        "color": "#DEDEDE",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 39,
        "type": "link",
        "name": "F",
        "area": "F",
        "color": "#DEDEDE",
        "inf_c": 1,
        "inf_1": "null",
    },
    {
        "id": 40,
        "type": "link",
        "name": "F",
        "area": "F",
        "color": "#DEDEDE",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 41,
        "type": "link",
        "name": "F",
        "area": "F",
        "color": "#DEDEDE",
        "inf_c": 2,
        "inf_1": "null",
        "inf_2": "null",
    },
    {
        "id": 42,
        "type": "link",
        "name": "F",
        "area": "F",
        "color": "#DEDEDE",
        "inf_c": 1,
        "inf_1": "null",
    },
    {
        "id": 43,
        "type": "link",
        "name": "F",
        "area": "F",
        "color": "#DEDEDE",
        "inf_c": 1,
        "inf_1": "null",
    },
    {
        "id": 44,
        "type": "link",
        "name": "F",
        "area": "F",
        "color": "#DEDEDE",
        "inf_c": 1,
        "inf_1": "null",
    }
]
# 可选初始位置
OPTIONAL_4 = [1, 2, 4, 5, 7, 19]

# 4人资源点邻接表
ADJACENCY_LIST_4 = [
    [
        # 0
        # node id 从 1 开始
    ],
    [
        # 1
        {"id": 2, "by": 23},
        {"id": 4, "by": 38},
        {"id": 10, "by": 40},
        {"id": 19, "by": 38},
        {"id": 19, "by": 40},
        {"id": 20, "by": 40},
    ],
    [
        # 2
        {"id": 1, "by": 23},
        {"id": 3, "by": 24},
        {"id": 4, "by": 39},
        {"id": 5, "by": 26},
        {"id": 6, "by": 24},
    ],
    [
        # 3
        {"id": 2, "by": 24},
        {"id": 6, "by": 24},
        {"id": 10, "by": 29},
        {"id": 11, "by": 29},
        {"id": 12, "by": 29},
    ],
    [
        # 4
        {"id": 1, "by": 38},
        {"id": 2, "by": 39},
        {"id": 5, "by": 25},
        {"id": 7, "by": 25},
        {"id": 19, "by": 38},
    ],
    [
        # 5
        {"id": 2, "by": 26},
        {"id": 4, "by": 25},
        {"id": 6, "by": 27},
        {"id": 7, "by": 25},
        {"id": 7, "by": 27},
        {"id": 8, "by": 27},
    ],
    [
        # 6
        {"id": 2, "by": 24},
        {"id": 3, "by": 24},
        {"id": 5, "by": 27},
        {"id": 7, "by": 27},
        {"id": 8, "by": 27},
        {"id": 12, "by": 41},
        {"id": 13, "by": 41},
    ],
    [
        # 7
        {"id": 4, "by": 25},
        {"id": 5, "by": 25},
        {"id": 5, "by": 27},
        {"id": 6, "by": 27},
        {"id": 8, "by": 27},
    ],
    [
        # 8
        {"id": 5, "by": 27},
        {"id": 6, "by": 27},
        {"id": 7, "by": 27},
        {"id": 9, "by": 28},
    ],
    [
        # 9
        {"id": 8, "by": 28},
    ],
    [
        # 10
        {"id": 1, "by": 40},
        {"id": 3, "by": 29},
        {"id": 11, "by": 29},
        {"id": 12, "by": 29},
        {"id": 19, "by": 40},
        {"id": 20, "by": 40},
    ],
    [
        # 11
        {"id": 3, "by": 29},
        {"id": 10, "by": 29},
        {"id": 12, "by": 29},
        {"id": 12, "by": 30},
    ],
    [
        # 12
        {"id": 3, "by": 29},
        {"id": 6, "by": 41},
        {"id": 10, "by": 29},
        {"id": 11, "by": 29},
        {"id": 11, "by": 30},
        {"id": 13, "by": 41},
    ],
    [
        # 13
        {"id": 6, "by": 41},
        {"id": 12, "by": 41},
    ],
    [
        # 14
    ],
    [
        # 15
    ],
    [
        # 16
    ],
    [
        # 17
    ],
    [
        # 18
    ],
    [
        # 19
        {"id": 1, "by": 38},
        {"id": 1, "by": 40},
        {"id": 4, "by": 38},
        {"id": 10, "by": 40},
        {"id": 20, "by": 40},
    ],
    [
        # 20
        {"id": 1, "by": 40},
        {"id": 10, "by": 40},
        {"id": 19, "by": 40},
        {"id": 21, "by": 36},
    ],
    [
        # 21
        {"id": 20, "by": 36},
    ],
    [
        # 22
    ]
]
# 4人邻接表（第4回合时追加, 改用此表）
ADJACENCY_LIST_APPEND_4 = [
    [
        # 0
        # node id 从 1 开始
    ],
    [
        # 1
        {"id": 2, "by": 23},
        {"id": 4, "by": 38},
        {"id": 10, "by": 40},
        {"id": 19, "by": 38},
        {"id": 19, "by": 40},
        {"id": 20, "by": 40},
    ],
    [
        # 2
        {"id": 1, "by": 23},
        {"id": 3, "by": 24},
        {"id": 4, "by": 39},
        {"id": 5, "by": 26},
        {"id": 6, "by": 24},
    ],
    [
        # 3
        {"id": 2, "by": 24},
        {"id": 6, "by": 24},
        {"id": 10, "by": 29},
        {"id": 11, "by": 29},
        {"id": 12, "by": 29},
    ],
    [
        # 4
        {"id": 1, "by": 38},
        {"id": 2, "by": 39},
        {"id": 5, "by": 25},
        {"id": 7, "by": 25},
        {"id": 19, "by": 38},
    ],
    [
        # 5
        {"id": 2, "by": 26},
        {"id": 4, "by": 25},
        {"id": 6, "by": 27},
        {"id": 7, "by": 25},
        {"id": 7, "by": 27},
        {"id": 8, "by": 27},
    ],
    [
        # 6
        {"id": 2, "by": 24},
        {"id": 3, "by": 24},
        {"id": 5, "by": 27},
        {"id": 7, "by": 27},
        {"id": 8, "by": 27},
        {"id": 12, "by": 41},
        {"id": 13, "by": 41},
    ],
    [
        # 7
        {"id": 4, "by": 25},
        {"id": 5, "by": 25},
        {"id": 5, "by": 27},
        {"id": 6, "by": 27},
        {"id": 8, "by": 27},
    ],
    [
        # 8
        {"id": 5, "by": 27},
        {"id": 6, "by": 27},
        {"id": 7, "by": 27},
        {"id": 9, "by": 28},
    ],
    [
        # 9
        {"id": 8, "by": 28},
        {"id": 14, "by": 32},
        {"id": 15, "by": 32},
        {"id": 21, "by": 44},
    ],
    [
        # 10
        {"id": 1, "by": 40},
        {"id": 3, "by": 29},
        {"id": 11, "by": 29},
        {"id": 12, "by": 29},
        {"id": 19, "by": 40},
        {"id": 20, "by": 40},
    ],
    [
        # 11
        {"id": 3, "by": 29},
        {"id": 10, "by": 29},
        {"id": 12, "by": 29},
        {"id": 12, "by": 30},
        {"id": 16, "by": 33},
        {"id": 17, "by": 30},
    ],
    [
        # 12
        {"id": 3, "by": 29},
        {"id": 6, "by": 41},
        {"id": 10, "by": 29},
        {"id": 11, "by": 29},
        {"id": 11, "by": 30},
        {"id": 13, "by": 41},
        {"id": 17, "by": 30},
    ],
    [
        # 13
        {"id": 6, "by": 41},
        {"id": 12, "by": 41},
        {"id": 14, "by": 31},
        {"id": 17, "by": 31},
    ],
    [
        # 14
        {"id": 9, "by": 32},
        {"id": 13, "by": 31},
        {"id": 15, "by": 33},
        {"id": 17, "by": 31},
    ],
    [
        # 15
        {"id": 9, "by": 32},
        {"id": 14, "by": 31},
        {"id": 17, "by": 42},
        {"id": 18, "by": 43},
    ],
    [
        # 16
        {"id": 11, "by": 33},
        {"id": 17, "by": 34},
        {"id": 18, "by": 35},
        {"id": 22, "by": 35},
    ],
    [
        # 17
        {"id": 11, "by": 30},
        {"id": 12, "by": 30},
        {"id": 13, "by": 31},
        {"id": 14, "by": 31},
        {"id": 15, "by": 42},
        {"id": 16, "by": 34},
    ],
    [
        # 18
        {"id": 15, "by": 43},
        {"id": 16, "by": 35},
        {"id": 22, "by": 35},
    ],
    [
        # 19
        {"id": 1, "by": 38},
        {"id": 1, "by": 40},
        {"id": 4, "by": 38},
        {"id": 10, "by": 40},
        {"id": 20, "by": 40},
    ],
    [
        # 20
        {"id": 1, "by": 40},
        {"id": 10, "by": 40},
        {"id": 19, "by": 40},
        {"id": 21, "by": 36},
    ],
    [
        # 21
        {"id": 9, "by": 44},
        {"id": 20, "by": 36},
        {"id": 22, "by": 37},
    ],
    [
        # 22
        {"id": 16, "by": 35},
        {"id": 18, "by": 35},
        {"id": 21, "by": 37},
    ]
]

MAP_4 = {
    1: [23, 38, 40],
    2: [23, 24, 26, 39],
    3: [24, 29],
    4: [25, 38, 39],
    5: [25, 26, 27],
    6: [24, 27, 41],
    7: [25, 27],
    8: [27, 28],
    9: [28],
    10: [29, 40],
    11: [29, 30],
    12: [29, 30, 41],
    13: [41],
    19: [38, 40],
    20: [36, 40],
    21: [36],
    23: [1, 2],
    24: [2, 3, 6],
    25: [4, 5, 7],
    26: [2, 5],
    27: [5, 6, 7, 8],
    28: [8, 9],
    29: [3, 10, 11, 12],
    30: [11, 12],
    36: [20, 21],
    38: [1, 4, 19],
    39: [2, 4],
    40: [1, 10, 19, 20],
    41: [6, 12, 13],
}

MAP_APPEND_4 = {
    1: [23, 38, 40],
    2: [23, 24, 26, 39],
    3: [24, 29],
    4: [25, 38, 39],
    5: [25, 26, 27],
    6: [24, 27, 41],
    7: [25, 27],
    8: [27, 28],
    9: [28, 32, 44],
    10: [29, 40],
    11: [29, 30, 33],
    12: [29, 30, 41],
    13: [31, 41],
    14: [31, 32, 33],
    15: [31, 32, 42, 43],
    16: [33, 34, 35],
    17: [30, 31, 34, 42],
    18: [35, 43],
    19: [38, 40],
    20: [36, 40],
    21: [36, 37, 44],
    22: [35, 37],
    23: [1, 2],
    24: [2, 3, 6],
    25: [4, 5, 7],
    26: [2, 5],
    27: [5, 6, 7, 8],
    28: [8, 9],
    29: [3, 10, 11, 12],
    30: [11, 12, 17],
    31: [13, 14, 15, 17],
    32: [9, 14, 15],
    33: [11, 14, 16],
    34: [16, 17],
    35: [16, 18, 22],
    36: [20, 21],
    37: [21, 22],
    38: [1, 4, 19],
    39: [2, 4],
    40: [1, 10, 19, 20],
    41: [6, 12, 13],
    42: [15, 17],
    43: [15, 18],
    44: [9, 21]
}

# 3人模式没人玩所以先不做
# 3人地图
NODE_DATAILS_3 = [
    # 懒得做
]
ADJACENCY_MATRIX_3 = [

]
ADJACENCY_LIST_3 = [

]
ADJACENCY_LIST_APPEND_3 = [

]
