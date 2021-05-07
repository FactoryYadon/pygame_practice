import pygame
import os

########################################################################

# 기본 초기화 반드시 해야하는 것들

pygame.init()                               # 초기화 반드시 필요

# 파일 경로 설정
sourceFileDir = os.path.dirname(os.path.abspath(__file__))

# 화면크기 설정
screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# FPS
clock = pygame.time.Clock()

########################################################################

# 1.  사용자 게임 초기화 ( 배경화면 , 게임 이미지 , 좌표 ,  폰트 등 )


# 배경 이미지 불러오기
background = pygame.image.load(os.path.join(sourceFileDir,"background.png"))

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(os.path.join(sourceFileDir,"character.png"))
character_size = character.get_rect().size                                                                  # 이미지의 크기 구해옴
character_width = character_size[0]                                                                         # 캐릭터의 width
character_height = character_size[1]                                                                        # 캐릭터의 세로 크기
character_x_pos = screen_width/2 -(character_width/2)                                                       # 캐릭터의 가로 위치
character_y_pos = screen_height - character_height                                                          # 캐릭터의 세로 위치





# 이동할 좌표
to_x = 0 
to_y = 0


# 이동 속도

character_speed = 0.3

# 적 enemy 캐릭터
enemy = pygame.image.load(os.path.join(sourceFileDir,"enemy.png"))
enemy_size = enemy.get_rect().size                                                                  # 이미지의 크기 구해옴
enemy_width = enemy_size[0]                                                                         # enemy의 width
enemy_height = enemy_size[1]                                                                        # enemy의 세로 크기
enemy_x_pos = screen_width/2 -(enemy_width/2)                                                       # enemy의 가로 위치
enemy_y_pos = (screen_height/2) - (enemy_height/2)                                                          # enemy의 세로 위치


# 폰트 정의
game_font = pygame.font.Font(None,40)                       # 폰트 객체 생성

# 게임 시간 
total_time = 10

# 시간 계산
start_ticks = pygame.time.get_ticks()                       # 시작 tick을 받아옴




# 이벤트 루프
running = True
while running:
    dt = clock.tick(60)

    print("fps = {0}".format(clock.get_fps()))
    
    # 2. 이벤트 처리 (키보드 , 마우스 등)

    # 2. 이벤트 처리 (키보드 , 마우스 등)

    # 4. 충돌 처리 (키보드 , 마우스 등)

    # 5. 화면에 그리기 (키보드 , 마우스 등)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0



    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    
    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    

    # 충돌 체크

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False



    screen.blit(background,(0,0))                               # 배경 그리기
    screen.blit(character,(character_x_pos,character_y_pos))    # 캐릭터 그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))                # enemy 그리기

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000           # 경과시간을 1000으로 나누어서 초단위로 표시
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10,10))

    # 시간 도달시 게임 종료
    if total_time - elapsed_time < 0:

        print("타임아웃")
        running = False
    
    
    pygame.display.update()                                     # 게임 화면 갱신


# pygame 종료 처리
pygame.time.delay(2000)

pygame.QUIT()
