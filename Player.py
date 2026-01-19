import pygame

class player():
    def __init__(self, stats, pos, screen):
        self.stats = stats
        self.pos = pos       #pos = pelvis
        self.screen = screen

        self.neck = [self.pos[0], self.pos[1] - 15]
        self.right_knee = [pos[0] - 5, pos[1] + 12]
        self.right_foot = [self.right_knee[0], self.right_knee[1] + 7]
        self.left_knee = [pos[0] + 5, pos[1] + 12]
        self.left_foot = [self.left_knee[0], self.left_knee[1] + 7]
        
        
    
    #def step(self):
        

    def draw(self):
        pygame.draw.line(self.screen, (0, 0, 0), self.pos, self.neck, width=1)
        pygame.draw.line(self.screen, (0, 0, 0), self.pos, self.right_knee, width=1)
        pygame.draw.line(self.screen, (0, 0, 0), self.left_foot, self.left_knee, width=1)
        pygame.draw.line(self.screen, (0, 0, 0), self.pos, self.left_knee, width=1)
        pygame.draw.line(self.screen, (0, 0, 0), self.right_foot, self.right_knee, width=1)
        
