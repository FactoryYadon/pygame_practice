import pygame
import os
import random

########################################################################

# 기본 초기화 반드시 해야하는 것들

pygame.init()                               # 초기화 반드시 필요

# 파일 경로 설정
sourceFileDir = os.path.dirname(os.path.abspath(__file__))
image_folder_path = os.path.join(sourceFileDir,"images")

# 화면크기 설정
screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("avoid shit game")

# FPS
clock = pygame.time.Clock()

########################################################################

# 1.  사용자 게임 초기화 ( 배경화면 , 게임 이미지 , 좌표 ,  폰트 등 )

# 배경 이미지 불러오기
background = pygame.image.load(os.path.join(image_folder_path,"background.png"))

# stage 불러오기
stage = pygame.image.load(os.path.join(image_folder_path,"stage.png"))
stage_size = stage.get_rect().size                                                                          # 이미지의 크기 구해옴
stage_width = stage_size[0]                                                                                 # stage 의 width
stage_height = stage_size[1]                                                                                # stage 의 세로 크기
stage_x_pos = 0                                                                                             # stage 의 가로 위치
stage_y_pos = screen_height - stage_height                                                                  # stage 의 세로 위치

# character 불러오기
character = pygame.image.load(os.path.join(image_folder_path,"character.png"))
character_size = character.get_rect().size                                                                  # 이미지의 크기 구해옴
character_width = character_size[0]                                                                         # character 의 width
character_height = character_size[1]                                                                        # character 의 세로 크기
character_x_pos = (screen_width/2) - (character_width/2)                                                    # character 의 가로 위치
character_y_pos = screen_height - stage_height - character_height                                           # character 의 세로 위치

# weapon 불러오기
weapon = pygame.image.load(os.path.join(image_folder_path,"weapon.png"))
weapon_size = weapon.get_rect().size                                                                  # 이미지의 크기 구해옴
weapon_width = weapon_size[0]                                                                         # weapon 의 width
weapon_height = weapon_size[1]                                                                        # weapon 의 세로 크기


# 무기는 한번에 여러 발 발사 가능
weapons = []

# 무기 이동속도
weapon_speed = 3.0



# 이동할 좌표
character_to_x = 0 

# 이동 속도
character_speed = 0.3

# 이벤트 루프
running = True
while running:
    dt = clock.tick(60)

    # 2. 이벤트 처리 (키보드 , 마우스 등)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width /2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos]) 


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

                
    character_x_pos += character_to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width


    # 무기 위치 조정
    weapons = [[w[0] , w[1]-weapon_speed] for w in weapons]

    # 천장에 닿은 무기 없애기
    weapons = [[w[0] , w[1]] for w in weapons if w[1] > 0]


    





    screen.blit(background,(0,0))                               # 배경 그리기

    for x_pos , y_pos in weapons:
        screen.blit(weapon,(x_pos,y_pos))

    screen.blit(stage,(stage_x_pos,stage_y_pos))                # stage 그리기
    screen.blit(character,(character_x_pos,character_y_pos))    # character 그리기

    



    pygame.display.update()                                     # 게임 화면 갱신


# pygame 종료 처리
pygame.time.delay(2000)

pygame.QUIT()
