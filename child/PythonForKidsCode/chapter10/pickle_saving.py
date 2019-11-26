import pickle
"""
保存玩家的进度信息
"""

game_data = {
'player-position' : 'N23 E45',
'pockets' : [ 'keys', 'pocket knife', 'polished stone' ],
'backpack' : [ 'rope', 'hammer', 'apple' ],
'money' : 158.50
}

save_file = open('save.dat', 'wb')
pickle.dump(game_data, save_file)
save_file.close()

# 腌制食品
# 口袋:小折刀 抛光的石头 
# 背包: 绳子 锤
