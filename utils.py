class Settings:
    def __init__(self):
        self.width = 1200
        self.height = 600
        self.bg_color = (250,250,250)
        self.heart_limit = 3

class GameStats:
    """Track statistics (e.g. points, hearts remaining)"""
    def __init__(self, dr_game):
        self.settings = dr_game.settings
        self.reset_stats()

    def reset_stats(self):
        self.hearts_left = self.settings.heart_limit


