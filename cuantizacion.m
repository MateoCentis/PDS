function [y]=cuantizacion(x,N,H)
  #N numero de niveles
  #H magnitud del paso
  #a la señal le sumamos un valor arbitrario para aplicar cuantizacion
  minimo = min(x);
  x = x - minimo; #resto minimo
  y= 0.*(x<0) + ...
     H.*fix(x./H).*(x >= 0 & x < (N-1).*H) + ...
     (N-1).*H .* (x >= (N-1).*H);
  y = y + minimo;#sumo minimo
  endfunction
