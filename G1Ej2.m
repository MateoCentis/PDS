#Ejercicio 2
#Prueba con los datos de una de las señales del ejercicio 1
fm=100;
fs=3;
phi=pi;
A=1;
[t,x]=senoidal(0,1,fm,fs,A,phi);
figure(1)
y = inversion(x)
plot(t,y,'k')
title('Inversion')
grid on
grid minor
hold on

figure(2)
y = rectificacion(x);
plot(t,y,'b')
title('Rectificación')
grid on
grid minor
hold on

figure(3)
plot(t,x,'r')
title('Cuantizacion')
grid on
grid minor
hold on
N=8;
H=0.25;
y = cuantizacion(x,N,H);
plot(t,y,'b-')
legend('Señal sin cuantizar','Señal cuantizada')

#Hecho

