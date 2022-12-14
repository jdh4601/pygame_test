import pygame
import os
import random

# 모든 라이브러리 초기화
pygame.init()

# global constant
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1300
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("game.Dino", "DinoRun1.png")), pygame.image.load(os.path.join("game.Dino", "DinoRun2.png"))]

JUMPING = [pygame.image.load(os.path.join("game/Dino", "DinoJump.png"))]

DUCKING = [pygame.image.load(os.path.join("game.Dino", "DinoDuck1.png")), pygame.image.load(os.path.join("game.Dino", "DinoDuck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("game/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("game/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("game/Cactus", "SmallCactus3.png"))]

LARGE_CACTUS = [pygame.image.load(os.path.join("game/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("game/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("game/Cactus", "LargeCactus3.pngame"))]

BIRD = [pygame.image.load(os.path.join("game/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("game/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("game/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("game/Other", "Track.png"))

class Dinosaur:
    X_POS = 80
    Y_POS = 310

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, user_input):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        # 0부터 9까지 계속 반복
        if self.step_index >= 10:
            self.step_index = 0

        # 공룡이 동작됨 테스트
        # 키보드 제어와 공룡의 현 상태와 관련한 동작들에 대한 코드
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        pass

    def run(self):
        self.image = self.run_img[self.step_index // 5] # 0,1 계속 반복
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        pass

    # 화면에 그리기 함수
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        # run = false가 되는 경우로 바꾸는 로직
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill(255, 255, 255)
        userinput = pygame.key.gert_pressed()

        player.draw(SCREEN)
        player.update(userinput)

        clock.tick(30)

main()
