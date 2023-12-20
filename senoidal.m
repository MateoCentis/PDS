function [t,x]=senoidal(t_a,t_b,fm,fs,A,phi)
  T=1./fm;
  t= t_a : 1./fm : t_b-T;
  x=A.*sin(2*pi*fs*t+phi);
  endfunction

