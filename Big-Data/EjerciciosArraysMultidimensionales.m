%Ejercicios Arrays Multidimensionales

%1. Crea una estructura que tenga la edad, el nombre y el domicilio de una persona 

%% 2. Crea un array 3D de ceros 3x3x3 
zero = zeros(3,3,3)

%% 3. Crea un array 3d con valores aleatorios. 
% De ahí coge una submatriz de la primera capa. 
% El tamaño de las filas y columnas es 4x4.  
r = randi(10, [6,6,3]);

subMatriz = r(1:4, 1:4, 1);

disp('Array 3D completo: ')
disp(r(:,:,1))

disp('Submatriz 4x4 de la primera capa:')
disp(subMatriz)
%% 4. Concatenar dos arrays de tamaño 2x2 en la 3ª dimensión 
arr1 = [1 2; 3 4];
arr2 = [5 6; 7 8];

C = cat(3, arr, arr2)

disp('Array 3D resultante:')
disp(C)
%% 5. Crea un array de tamaño 2x4x7 que represente las temperaturas tomadas 
% durante los 7 días de la semana en 4 ubicaciones 
% (norte, sur, este, oeste). Se toman la mínima y la máxima. 
% Llena el array con valores aleatorios entre –5 y 35 ºC. 
temp = -5 + (35 + 50) * rand(2,4,7);

disp('Tamaño del array: ')
disp(size(temp))

disp('Temperaturas (min y max) del día 1 en las 4 ubicaciones:')
disp(temp(:,:,1))
%% 6. Calcula la media de las temperaturas, el min y el max 
%Media de todas las temperaturas
media_total = mean(temp(:));

%Minimo
min_total = min(temp(:));

%Maximo
max_total = max(temp(:));

% Mostrar resultados
disp(['Media de las temperaturas: ', num2str(media_total), ' °C'])
disp(['Mínima temperatura: ', num2str(min_total), ' °C'])
disp(['Máxima temperatura: ', num2str(max_total), ' °C'])