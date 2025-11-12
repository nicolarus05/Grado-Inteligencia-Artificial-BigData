%Ejercicios Graficos 3D
%% 1. Crea una espiral en 3D usando las ecuaciones paramétricas 
% x=t·cos(t), y=t·sin(t), z=t Usa plot3 para visualizar la curva. 

 t = 0:0.1:10*pi;

 x = t .* cos(t);
 y = t .* sin(t);
 z = t;

figure
plot3(x, y, z, 'LineWidth', 2)
grid on
xlabel('X')
ylabel('Y')
zlabel('Z')
title('Espiral 3D usando plot3')