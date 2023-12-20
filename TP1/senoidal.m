function x=senoidal(t_a,t_b,fm,fs,A,phi)
  T=1./fm;
  t= t_a : 1./fm : t_b-T;
  X=A.*sin(2*pi*fs*t+phi);
  return X;
  endfunction
