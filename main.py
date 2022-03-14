c1_s_y=10
c2_s_y=-10
c2_2_x=0
x1=200
y1=200

x2=300
y2=300

while True:
    for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
        
y1=c1_s_y+y1
y2=c2_s_y+y2

if(y1>380 or y1<15):
    c1_s_y=c1_s_y *-1
if(y2>380 or y2<15):
    c2_s_y=c2_s_y *-1
    
clock.tick(30)

canvas.blit(bg,(0,0))
 pygame.draw.circle(canvas,blue,(x1,y1),15)
 pygame.draw.circle(canvas,green,(x2,y2),15)
 pygame.display.update()