function [t,y]=fSinc(t_a,t_b,fm,fs,A,phi)
  T=1/fm;
  t= t_a : T : t_b-T;
  x=2*pi*fs*t+phi;
  y= (A.*sin(x)./x).*(x=~0)+ 1.*(x==0);
  endfunction

