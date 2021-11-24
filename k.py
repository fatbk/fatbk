import pygame
print("nhap ngay sinh:")
player1=input()
print("nhap thang sinh:")
player=input()

if player==3:
   player="sinh nhat ba"
if player==6:
   player="sinh nhat em gai"
if player==11:
   player="sinh nhat me"


if player1=="4":
	if player=="3":
		print("chuc ba sinh nhat vui ve")
	else:
		if player=="11":
			print("chuc me sinh nhat vui ve")

if player1=="27":
	if player=="6":
		print("chuc em gai sinh nhat vui ve")


