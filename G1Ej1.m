#Ejercicio 1
fm=100;
fs=3;
phi=pi;
A=1;
#1
[t,x]=senoidal(0,1,fm,fs,A,phi);
#2
#rand(a,b) a:filas b:columnas
a=-1;
b=1;
[t y] = fSinc(a,b,fm,fs,A,phi);
#3
a=0;
b=1;
[t y] = ondaCuadrada(a,b,fm,fs,A,phi);
plot(t,y)
#anda todo
