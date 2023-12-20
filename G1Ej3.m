Tm = 0.1/80;#8 muestras cada 0.01 segundos
fs = 2/0.1; #2 ciclos en 0.1 s
t1 = 5*Tm;
phi = -2*pi*fs*t1;   #phi=2 pi fs t1 donde t1 es el retardo en segundos (tiempo que tarda en hacer en cruzar cero)
t = 0:Tm:0.1-Tm; #periodo de muestreo
arg = 2.*pi.*fs.*t+phi;
A = 3;
x = A*sin(arg);
plot(t,x,'-o')
grid on
grid minor
title('Señal senoidal discreta')
#no anda del todo
