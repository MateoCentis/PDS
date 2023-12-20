function [t,y]=ondaCuadrada(t_a,t_b,fm,fs,A,phi)
  T=1/fm;
  t= t_a : T : t_b-T;
  x=2*pi*fs*t+phi;
  y= -1.*(mod(x,2*pi)>=pi)+ 1.*(mod(x,2*pi)<pi);
  endfunction
