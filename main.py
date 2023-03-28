from get_screen import get_screen_data
import cv2
import time

for i in range(5):
    print(i)
    time.sleep(1)

images = 600
iamges = 5
x = 0
while x<images:
    data = get_screen_data("firefox")
    cv2.imwrite(f"games/game1/{x}.jpg", cv2.cvtColor(data, cv2.COLOR_BGR2RGB))
    x += 1
    print(x)
    
# cv2.imshow('window',cv2.cvtColor(data, cv2.COLOR_BGR2RGB))

# cv2.waitKey(0)
