#-*-coding:UTF-8-*-
import pygame, os, sys, random, time
from pygame.locals import*
pygame.init()



pygame.mixer.music.load("ievan polka miku hatsune ver197.mp3")

ventana=pygame.display.set_mode((900,550))
pygame.display.set_caption("ABC")
ventana.fill((128,0,255))

correcta=0


fondito=pygame.image.load("3.jpg")
pantalla_base=fondito.copy()
ventana.blit(fondito,(0,0))

res=pygame.image.load("res.jpg")
ventana.blit(res,(0,450))
pantalla_res=res.copy()

tien=pygame.image.load("tien.jpg")
ventana.blit(tien,(700,0))
pantalla_tien=tien.copy()

imagenes=["arbol.jpg","barco.jpg","casa.jpg","dado.jpg","elefante.jpg","flor.jpg","gato.jpg","helado.jpg","isla.jpg","jirafa.jpg","koala.jpg","luna.jpg","mono.jpg","naranja.jpg","oso.jpg","pelota.jpg","queso.jpg","raton.jpg","sol.jpg","tortuga.jpg","uva.jpg","vaca.jpg","wally.jpg","xilofon.jpg","yoyo.jpg","zanahoria.jpg"]
i=random.randrange(1,26)
imageneleg=pygame.image.load(imagenes[i])
rtacorrecta=imagenes[i][0:-4]

tiempo=-1

puntos=(00)
x=250
y=0
pal=""
pygame.mixer.music.play(2)
pygame.display.update()
sigo=True
cantImag=0
while sigo==True:
	
	tiempo=tiempo+1
	tl=pygame.font.SysFont("arial black",36)
	texinic=tl.render(str(tiempo),True,(255,255,255),(128,0,255))
	ventana.blit(texinic,(810,160))
	print texinic.get_rect()
	
	
	if (imageneleg,(x,y))>=(imageneleg,(200,295)):
		i=random.randrange(1,26)
		imageneleg=pygame.image.load(imagenes[i])
		rtacorrecta=imagenes[i][0:-4]
		x=200
		y=0
		pal=""
		pygame.display.update()	
		
	#muestro la imagen 
	ventana.blit(imageneleg,(x,y))
	y=y+5
	pygame.display.update()
	ventana.blit(pantalla_base,(0,0))
	time.sleep(0.5)
	eventos=pygame.event.get()
	
	

	for evento in eventos:
		if evento.type==QUIT:
			pygame.quit()
			sys.exit()	
		elif evento.type==KEYDOWN:
			if evento.key>=K_a and evento.key <=K_z:
				
				pal=pal+chr(evento.key)
				tipoLetra2=pygame.font.SysFont("arial black",48)
				textoInicial2=tipoLetra2.render(pal,True,(255,255,255),(128,0,255))
				ventana.blit(textoInicial2,(300,470))
				print textoInicial2.get_rect()	
				
			elif evento.key==8:
				pal=pal[0:-1]
				tipoLetra2=pygame.font.SysFont("arial black",48)
				textoInicial2=tipoLetra2.render(pal,True,(255,255,255),(128,0,255))
				ventana.blit(pantalla_res,(0,450))
				pygame.display.update()
				ventana.blit(textoInicial2,(300,470))
								
				
				
			elif evento.key==13:
				if pal == rtacorrecta:
					correcta=correcta+1
					#MUESTRO texto si acerto
					acertaste=pygame.font.SysFont("arial",26).render("Acertaste",True,(255,255,255),(128,0,255))
					print acertaste.get_rect()
					ventana.blit(pantalla_tien,(700,0))
					ventana.blit(acertaste,(700,230))
					#sumar ptos ymostrzar
					puntos=puntos+10
					sumopuntos=pygame.font.SysFont("arial black",36).render(str(puntos),True,(255,255,255),(128,0,255))
					ventana.blit(sumopuntos,(800,60))	
					pygame.display.update()
				else:
					correcta=correcta+1
					#muestro texto si fallo
					ventana.blit(pantalla_base,(0,0))
					fallaste=pygame.font.SysFont("arial",26).render("Fallaste",True,(255,255,255),(128,0,255))
					print fallaste.get_rect()
					ventana.blit(pantalla_tien,(700,0))
					ventana.blit(fallaste,(700,230))
					#resto puntos
					puntos=puntos-10
					restopuntos=pygame.font.SysFont("arial black",36).render(str(puntos),True,(255,255,255),(128,0,255))
					ventana.blit(restopuntos,(800,60))
					
				
				if cantImag<9:
					#elegir la prox imagen
					i=random.randrange(1,26)
					imageneleg=pygame.image.load(imagenes[i])			
					rtacorrecta=imagenes[i][0:-4]
					x=250
					y=0
					pal=""
					ventana.blit(pantalla_res,(0,450))
					#pygame.display.update()
					cantImag=cantImag +1
				else:
					sigo=False


imgenfinal=pygame.image.load("final.jpg")
ventana.blit(imgenfinal,(0,0))
puntaje=pygame.font.SysFont("Impact",60).render(str(puntos),True,(0,0,0),(253,216,110))
ventana.blit(puntaje,(550,5))	
if puntos>=70:
	bien=pygame.font.SysFont("Impact",60).render("LO HICISTE BIEN",True,(0,0,0),(253,216,110))
	ventana.blit(bien,(300,70))
elif puntos>0 and puntos<70:
	maso=pygame.font.SysFont("Impact",60).render("SIGUE PRACTICANDO",True,(0,0,0),(253,216,110))
	ventana.blit(maso,(300,70))
elif puntos<0:
	mal=pygame.font.SysFont("Impact",60).render("MAS SUERTE LA PROXIMA",True,(0,0,0),(253,216,110))
	ventana.blit(mal,(200,70))
pygame.display.update()

time.sleep(10)
	
		
			



	


				
						
				
