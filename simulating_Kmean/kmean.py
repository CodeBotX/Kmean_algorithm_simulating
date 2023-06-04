import pygame
from random import randint
import math
from sklearn.cluster import KMeans
pygame.init()
screen = pygame.display.set_mode((1250,700))
pygame.display.set_caption("Kmean with pygame")

Red= (255, 0, 0)
Green= (0, 255, 0)
Blue= (0, 0, 255)
Cyan= (0, 255, 255)
Magenta= (255, 0, 255)
Yellow =(255, 255, 0)
Orange= (255, 165, 0)
Purple= (128, 0, 128)
Pink= (255, 192, 203)
Teal =(0, 128, 128)
Lime =(0, 255, 0)
Brown= (165, 42, 42)
Gray =(128, 128, 128)
Navy= (0, 0, 128)
Olive= (128, 128, 0)
def Distance (p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
def draw_text_box(x, y, text):
    lines = text.split('\n')
    line_height = font.get_linesize()
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, (0, 0, 0))
        screen.blit(text_surface, (x + 10, y + 10 + i * line_height))

running = True
BACKGROUND = (204,153,255)
Bac_color = (192,192,192)
black_color = (0,0,0)
white_color = (255,255,255)
tim_color = (128,0,128)
backrgound_panel = white_color

font= pygame.font.SysFont('Latin Modern Math',40)
font_smal = pygame.font.SysFont('Latin Modern Math',20)
text_plus = font.render('+',True,white_color)
text_minus = font.render('-',True,white_color)
text_run = font.render('Run',True,white_color)
text_random = font.render('Random',True,white_color)
text_algorthm = font.render('Algorthm',True,white_color)
text_reset = font.render('Reset',True,white_color)
font_logo = pygame.font.SysFont('Bebas Neue',50)
text_logo = font_logo.render('Minh Tien',True,(176,196,222))
text_logo_0 = 'Mo Hinh Phan Cum\nDu Lieu\nBang Thuat Toan Kmean'

K=0
points=[]
clusters=[]
color_names = ['Red', 'Green', 'Blue', 'Cyan', 'Magenta', 'Yellow', 'Orange', 'Purple', 'Pink', 'Teal', 'Lime', 'Brown', 'Gray', 'Navy', 'Olive']
labels=[]

size = 4

while running == True:
    screen.fill(BACKGROUND)
    # ve panel
    pygame.draw.rect(screen,black_color,(45,45,760,610))
    pygame.draw.rect(screen,white_color,(50,50,750,600))
    pygame.draw.rect(screen,(64,64,64),(830,0,470,700))
    pygame.draw.rect(screen,(192,192,192),(840,10,400,680))
    # vẽ trường hiển thị K và text ans
    # logo
    pygame.draw.rect(screen,black_color,(1040,585,180,75))
    # vẽ các nút
    # nút chỉnh k
    pygame.draw.rect(screen,black_color,(850,20,380,260))
    pygame.draw.rect(screen,white_color,(860,80,360,180))
    # run
    pygame.draw.rect(screen,black_color,(850,300,150,50))
    # random
    pygame.draw.rect(screen,black_color,(850,400,150,50))
    # alforthm
    pygame.draw.rect(screen,black_color,(850,500,150,50))
    # reset
    pygame.draw.rect(screen,black_color,(850,600,150,50))
    # vẽ text trên các nút
    screen.blit(text_plus,(870,40))
    screen.blit(text_minus,(970,40))
    screen.blit(text_run,(860,310))
    screen.blit(text_random,(860,410))
    screen.blit(text_algorthm,(860,510))
    screen.blit(text_reset,(860,610))
    screen.blit(text_logo,(1050,610))

    draw_text_box(865,90,text_logo_0)

    # lấy tọa độ chuột
    mouse_x, mouse_y = pygame.mouse.get_pos()
    text_mouse = font.render(f"({mouse_x}, {mouse_y})", True, white_color)
    screen.blit(text_mouse,(500,10))
    if 50< mouse_x < 800 and 50 < mouse_y < 650:
        text_mouse = font_smal.render(f"({mouse_x-50}, {mouse_y-50})", True, black_color)
        screen.blit(text_mouse,(mouse_x+10,mouse_y-10))


    # text K
    text_K = font.render(str(K),True,white_color)
    screen.blit(text_K,(1130,40))

    # size
    pygame.draw.rect(screen,black_color,(1040,450,180,80))
    pygame.draw.rect(screen,white_color,(1045,485,170,40))
    #  size_F la logo
    text_size_F = font_smal.render("SIZE",True,white_color) 
    text_size = font.render(str(size),True,black_color)
    screen.blit(text_size,(1055,495))
    screen.blit(text_size_F,(1110,460))

    # ERROR
    pygame.draw.rect(screen,black_color,(1040,300,180,80))
    pygame.draw.rect(screen,white_color,(1045,330,170,40))
    text_error_F = font_smal.render("ERROR",True,white_color)
    screen.blit(text_error_F,(1100,310))

    # xử lý các sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            # Bam k+,- button
            if 850 < mouse_x < 920 and 20< mouse_y < 80:
                if K < 15:
                    K +=1
            if 920 < mouse_x < 1020 and 20< mouse_y < 80:
                if K > 0:
                    K -=1
            # Bam Run button
            if 850 < mouse_x < 1000 and 300< mouse_y < 350:
                # gán điểm vào cụm gần nhất
                labels=[]
                if clusters == []:
                    continue
                for p in points:
                    distances_form_point_to_cluster = []
                    for c in clusters:
                        distane = Distance(p,c)
                        distances_form_point_to_cluster.append(distane)
                    min_distance = min(distances_form_point_to_cluster)
                    label = distances_form_point_to_cluster.index(min_distance)
                    labels.append(label) 
                # update điểm sinh ngẫu nhiên vào chính giữa cụm
                for i in range(K):
                    sum_x = 0
                    sum_y = 0
                    count = 0
                    for j in range(len(points)):
                        if labels[j]==i:
                            sum_x += points[j][0]
                            sum_y += points[j][1]
                            count +=1
                    if count != 0:
                        new_cluster_x = int(sum_x/count)
                        new_cluster_y = int(sum_y/count)
                        clusters[i]=[new_cluster_x,new_cluster_y]
            # Bam Random button
            if 850 < mouse_x < 1000 and 400< mouse_y < 450:
                clusters=[]
                labels=[]
                for i in range(K):
                    random_point = [randint(0,700),randint(0,600)]
                    clusters.append(random_point)
            # Bam algorthm button
            if 850 < mouse_x < 1000 and 500< mouse_y < 550:
                # khởi tạo thuật toán kmean
                kmeans=KMeans(n_clusters=K).fit(points)
                # predict trả về nhãn cho các điểm
                labels=kmeans.predict(points)
                # cluster trả về các điểm là trung tâm của cụm
                clusters = kmeans.cluster_centers_
            # Bam reset button
            if 850 < mouse_x < 1000 and 600< mouse_y < 650:
                points=[]
                clusters=[]
                error=0
                labels=[]
            # Bam vẽ điểm 
            if 50< mouse_x < 800 and 50 < mouse_y < 650:
                labels=[]
                x=[mouse_x-50,mouse_y-50]
                points.append(x)
            # size button
            if 1040< mouse_x < 1125 and 450 < mouse_y < 485:
                if size>4:
                    size -=1
            if 1125< mouse_x < 1220 and 450 < mouse_y < 485:
                if size<12:
                    size +=1

    # muốn vẽ liên tục thì vẽ trong vòng lặp while
    # vẽ điểm lên màn hình
    for i in range(len(points)):
        pygame.draw.circle(screen,black_color,(points[i][0]+50,points[i][1]+50),size)
        if labels==[]:
            pygame.draw.circle(screen,white_color,(points[i][0]+50,points[i][1]+50),size-1)
        else:
            pygame.draw.circle(screen,color_names[labels[i]],(points[i][0]+50,points[i][1]+50),size-1)
    for i in range(len(clusters)):
        pygame.draw.circle(screen,color_names[i],(clusters[i][0]+50,clusters[i][1]+50),5)
    # Tinh ERROR
    error = 0
    if clusters!=[] and labels!=[]:
        for i in range(len(points)):
            error += int(Distance(points[i],clusters[labels[i]]))
    text_error = font.render(str(error),True,black_color)
    screen.blit(text_error,(1055,340))
    pygame.display.flip()
pygame.quit()
