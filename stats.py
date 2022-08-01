class Stats():
    """статистика"""

    def __init__(self):
        """ініціалізує статистику"""
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """статистика яка міняється під час гри"""
        self.guns_left = 2
        self.score = 0