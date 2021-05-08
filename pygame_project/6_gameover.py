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
weapon_size = weapon.get_rect().size                                                                        # 이미지의 크기 구해옴
weapon_width = weapon_size[0]                                                                               # weapon 의 width
weapon_height = weapon_size[1]                                                                              # weapon 의 세로 크기

# balloon 불러오기
ball_images =[
    pygame.image.load(os.path.join(image_folder_path,"balloon1.png")),
    pygame.image.load(os.path.join(image_folder_path,"balloon2.png")),
    pygame.image.load(os.path.join(image_folder_path,"balloon3.png")),
    pygame.image.load(os.path.join(image_folder_path,"balloon4.png"))
]

# balloon spped
ball_speed_y = [-18,-15,-12,-9]                                         # index 0 , 1 , 2 , 3 해당하는 값

# balloons
balloons = []

balloons.append({
    "pos_x" : 50,                               # 공의 x 좌표
    "pos_y" : 50,                               # 공의 y 좌표
    "img_idx" : 0,                              # 공의 인덱스
    "to_x" : 3,                                 # x 축 이동방향 -3 좌측 이동 3 우측이동
    "to_y" : -6,                                # y 축 이동방향
    "init_spd_y" : ball_speed_y[0]              # y 최초 속도

})

# 사라질 무기, 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1



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

    # 공 위치 정의
    for ball_index , ball_val in enumerate(balloons):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        if ball_pos_x <= 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1


        # 세로 위치
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: # 그외의 모든 경우에는 속도를 줄여나감
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]




    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for idx,val in enumerate(balloons):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]


        # 공 rect 정보 업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        if character_rect.colliderect(ball_rect):
            running = False


        # 공과 무기들 충돌 처리
        for weapon_idx , weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y


            # 충돌 체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx
                ball_to_remove = idx
                

                # 가장 작은 크기의 공이 아니라면 다음 단계의 공으로 나눠주기
                if ball_img_idx < 3:

                    # 현재 공 크기 정보를 가지고 옴
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    # 나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    
                    # 왼쪽으로 튕겨 나가는 작은 공
                    balloons.append({
                        "pos_x" : ball_pos_x + (ball_width /2) - (small_ball_width / 2 ),                                 # 공의 x 좌표
                        "pos_y" : ball_pos_y + (ball_height /2) - (small_ball_height / 2 ),                               # 공의 y 좌표
                        "img_idx" : ball_img_idx + 1,                              # 공의 인덱스
                        "to_x" : -3,                                 # x 축 이동방향 -3 좌측 이동 3 우측이동
                        "to_y" : -6,                                # y 축 이동방향
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]              # y 최초 속도

                    })
                    
                    # 오른쪽으로 튕겨 나가는 작은 공
                    balloons.append({
                        "pos_x" : ball_pos_x + (ball_width /2) - (small_ball_width / 2 ),                                 # 공의 x 좌표
                        "pos_y" : ball_pos_y + (ball_height /2) - (small_ball_height / 2 ),                               # 공의 y 좌표
                        "img_idx" : ball_img_idx + 1,                              # 공의 인덱스
                        "to_x" : 3,                                 # x 축 이동방향 -3 좌측 이동 3 우측이동
                        "to_y" : -6,                                # y 축 이동방향
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]               # y 최초 속도

                    })
                    

        
        # 충돌된 공 or 무기 없애기
        if ball_to_remove > -1:
            del balloons[ball_to_remove]
            ball_to_remove = -1

        if weapon_to_remove > -1:
            del weapons[weapon_to_remove]
            weapon_to_remove = -1











    screen.blit(background,(0,0))                               # 배경 그리기

    for x_pos , y_pos in weapons:
        screen.blit(weapon,(x_pos,y_pos))

    for idx,val in enumerate(balloons):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x,ball_pos_y))


    screen.blit(stage,(stage_x_pos,stage_y_pos))                # stage 그리기
    screen.blit(character,(character_x_pos,character_y_pos))    # character 그리기


    



    pygame.display.update()                                     # 게임 화면 갱신


# pygame 종료 처리
pygame.time.delay(2000)

pygame.QUIT()
