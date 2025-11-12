%Ejercicios de graficas 2D
%% 1. Un coche registra su velocidad cada minuto durante un viaje 
% de 60 minutos. Genera un vector aleatorio de velocidades 
% entre 0 y 120 km/h y crea una gráfica de líneas que muestre 
% la velocidad en función del tiempo. Ponle título y nombre a los ejes.
tiempo = 1:60;
velocidad = 120 * rand(1,60);

figure
plot(tiempo, velocidad)
grid on

title('Velocidad del coche durante 60 minutos')
xlabel('Tiempo (min)')
ylabel('Velocidad (km/h)')
%% 2. Genera dos vectores con 12 valores cada uno que representen 
% las ventas mensuales de dos productos durante un año. 
% Representa los datos en una gráfica de barras donde cada grupo de barras 
% representa un mes. Las ventas van desde 50 a 200 €. 
meses = (1:12)';
pr1 = 50 + (200 - 50) * rand(1,12);
pr2 = 50 + (200 - 50) * rand(1,12);
ventas = [pr1' pr2'];

figure
bar(meses, ventas, 'grouped')
grid on

title('Ventas mensuales de dos productos')
xlabel('Meses')
ylabel('Ventas (€)')
legend('Producto 1', 'Producto 2')
%% 3. Simula el ciclo de vida de un proyecto mostrando la proporción 
% de tiempo dedicado a 4 fases: planificación(20%), desarrollo(50%), 
% pruebas(20%), y despliegue(10%). Usa una gráfica de pastel para 
% representar las proporciones.
fases = {'Planificacion', 'Desarrollo', 'Pruebas', 'Despliegue'};
proporcion = [20 50 20 10];

figure
pie(proporcion, fases)
title('Ciclo de vida de un proyecto')

%% 4. Genera un vector de edades de 100 personas con valores entre 18 y 70 
% y muestra la distribución en un histograma con intervalos de 5 años. 
edades = randi([18,70], 1, 100);

figure
histogram(edades, 18:5:70)
grid on

% Añadir título y etiquetas
title('Distribución de edades de 100 personas')
xlabel('Edad')
ylabel('Número de personas')