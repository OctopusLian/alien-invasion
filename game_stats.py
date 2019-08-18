class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        # 初始化统计信息
        self.ai_settings = ai_settings
        self.reset_stats()

        # 让游戏一开始处于非活动状态
        self.game_active = False
        
        # Start Alien Invasion in an active state.
        self.game_active = True
        
    def reset_stats(self):
        # 初始化随游戏进行可能变化的统计信息
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
