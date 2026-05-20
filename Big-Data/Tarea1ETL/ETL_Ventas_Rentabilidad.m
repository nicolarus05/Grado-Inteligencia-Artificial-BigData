%% Análisis de rentabilidad de producto y método de pago.
% Limpiamos, indicadores y exportes.
clear; clc;

%1) Cargamos el archivo csv.
opts = detectImportOptions('ventas_online_2.csv', 'NumHeaderLines', 0);

% lee el archivo csv usando las opciones detectadas.
T = readtable('ventas_online_2.csv', opts);

%% 2) Normalizar nombres de columnas
% Convierte los nombres de columnas en nombres válidos de variables de MATLAB
% (sin espacios, caracteres especiales, etc.)
T.Properties.VariableNames = matlab.lang.makeValidName(T.Properties.VariableNames);

%% 3) Convertir campos numéricos
% Guarda los nombres de las columnas en una variable.
cols = T.Properties.VariableNames;

% Conversion de precio_unitario.
% Compruebo si existe una columna que se llama precio_unitario.
if any(strcmpi(cols, 'precio_unitario'))
    % Convierto los valores a texto, las comas por puntos y convierto a
    % numero
    T.precio_unitario = str2double(strrep(string(T.precio_unitario),',','.'));
end

% Conversion de unidades.
% Compruebo si existe la columna unidades.
if any(strcmpi(cols, 'unidades'))
    % Convierto a numero redondeando al entero mas cercano.
    T.unidades = round(str2double(string(T.unidades)));
    % Si hay valores NaN (vacios), se reemplazaran por 1.
    T.unidades(isnan(T.unidades)) = 1;
end

% Conversion de descuento.
% Compruebo si existe la columna descuento.
if any(strcmpi(cols, 'descuento'))
    % Convierto a numero y normalizo a formato decimal.
    T.descuento = str2double(strrep(string(T.descuento),',','.'));
    % Sustituyo valores vacios por 0.
    T.descuento(isnan(T.descuento)) = 0;
    % Si el numero en masyor que 1, se asume que esta en porcentaje.
    T.descuento(T.descuento > 1) = T.descuento(T.descuento > 1) / 100;
end

% Conversion de valoracion.
% Compruebo si la columna validacion existe.
if any(strcmpi(cols,'valoracion'))
    % Convierto los datos a número
    T.valoracion = str2double(strrep(string(T.valoracion),',','.'));
    % Calculo la media de las valoraciones no nulas
    mediaVal = mean(T.valoracion(~isnan(T.valoracion)));
    % Sustituyo los valores vacíos por la media
    T.valoracion(isnan(T.valoracion)) = mediaVal;
end

%% 4) Calcular importe_total, aplicar descuento y precio_final.
% Verificamos si existen las columnas precio_unitario y unidades.
if all(ismember({'precio_unitario', 'unidades'}, T.Properties.VariableNames))
    % Calculo el importe total como precio_unitario * unidades.
    T.importe_total = T.precio_unitario .* T.unidades;
else
    % Si alguna columna no exite, la crea vacia.
    T.importe_total = NaN(hright(T), 1);
end

% Calculo le precio final tras aplicar el descuento.
T.precio_final = T.importe_total .* (1 - T.descuento);

% Defino el ingreso como el precio final.
T.ingreso = T.precio_final;

%% 5) Calcular margen bruto.
% Compruebo si existe la columna 'coste_unitario'
if any(strcmpi(cols,'coste_unitario'))
    % Convierto los valores a numérico
    T.coste_unitario = str2double(strrep(string(T.coste_unitario),',','.'));
    % Calculo el margen bruto: (precio - coste) * unidades
    T.margen_bruto = (T.precio_unitario - T.coste_unitario) .* T.unidades;
else
    % Si no existe, crea una columna vacía
    T.margen_bruto = NaN(height(T),1);
end

%% 6) Agrupar por producto y metodo de pago.
% Agrupacion por producto.
if any(strcmpi(cols, 'producto'))
    % Calculo suma y media de ingreso y precio_unitario agrupado por producto
    gp = groupsummary(T, 'producto', {'sum', 'mean'}, {'ingreso', 'precio_unitario'});
    % Exporto la tabla a un archivo excel.
    writetable(gp, 'resumen_productos.xlsx', 'sheet', 'resumen_productos');
end

% Agrupacion por metodo de pago.
if any(strcmpi(cols, 'metodo_pago'))
    % Calculo la suma y media de ingreso y precio_unitario agrupados por el
    % metodo de pago.
    gm = groupsummary(T, 'metodo_pago', {'sum', 'mean'}, {'ingreso', 'precio_unitario'});
    % Exporto la tabla a un archivo excel.
    writetable(gp, 'resumen_metodo_pago.xlsx', 'sheet', 'resumen_metodo_pago');
end

%% 7) Agrupar por ciudad y categoría
% Compruebo si existen ambas columnas
if all(ismember({'ciudad','categoria'}, T.Properties.VariableNames))
    % Calculo las ventas totales agrupadas por ciudad y categoria
    gc = groupsummary(T,{'ciudad','categoria'},{'sum'},{'ingreso'});
    % Exporto el resumen a un Excel
    writetable(gc,'resumen_ciudad_categoria.xlsx','Sheet','resumen');
end

%% 8) Guardo las graficas.
% Grafica 1: Top 10 productos por ventas
if exist('gp','var')
    figure; % Creo una nueva figura
    % Ordeno los productos por ingreso descendente
    [~,idx] = sort(gp.sum_ingreso,'descend');
    % Selecciono los 10 primeros productos
    top = gp(idx(1:min(10,end)),:);
    % Creo un gráfico de barras con las ventas
    bar(top.sum_ingreso);
    % Asigno las etiquetas del eje X con los nombres de producto
    set(gca,'XTickLabel',top.producto,'XTickLabelRotation',45);
    % Añado título y etiqueta al eje Y
    title('Top 10 productos por ventas (ingresos)');
    ylabel('Ingresos (€)');
    % Guardo el gráfico en formato PNG
    saveas(gcf,'grafico_resumen_productos.png');
end

% Grafica 2: Distribución de ventas por método de pago
if exist('gm','var')
    figure; % Creo una nueva figura
    % Creo un gráfico circular (pie chart) con los ingresos por método de pago
    pie(gm.sum_ingreso, gm.metodo_pago);
    % Añado título
    title('Distribución de ventas por método de pago');
    % Guardo el gráfico en formato PNG
    saveas(gcf,'grafico_resumen_metodo_pago.png');
end

%% 9) Detectar errores y valores vacíos
% Calculo el número de valores vacios por columna
missing = sum(ismissing(T));

% Muestro por pantalla una tabla con los nombres de columnas y su conteo de valores vacíos
disp('Valores faltantes por columna:');
disp(table(T.Properties.VariableNames', missing', ...
    'VariableNames', {'Columna','MissingCount'}));

%% 10) Preguntas finales.
% ¿Qué producto genera más ingresos?
% El producto que mas ingresos genera es el raton.

% ¿Qué método de pago es más popular?
% El metodo de pago mas popular es el bizum.

% ¿Qué producto tiene menor rentabilidad?
% El producto menos rentable es la taza.