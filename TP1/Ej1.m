#Ejercicio 1
#1
[t,x]=senoidal(0,1,100,3,2,0);
#2
#rand(a,b) a:filas b:columnas
fSinc=@(x) sin./x*(x~=0)+1.*(x==0);
fSinc(5)
sinc(5)



