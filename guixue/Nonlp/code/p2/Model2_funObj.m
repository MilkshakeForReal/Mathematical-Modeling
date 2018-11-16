function f = funObjYard(x)
a = [1.25 8.75 0.5 5.75 3 7.25];
b = [1.25 0.75 4.75 5 6.5 7.75];
% x=[A到各场地输送量, B到.. ,A坐标, B坐标]
A_loc = x(13:14);
B_loc = x(15:16);
%先算A
f1 = sqrt((a-A_loc(1)).^2+(b-A_loc(2)).^2) * x(1:6);
f2 = sqrt((a-B_loc(1)).^2+(b-B_loc(2)).^2) * x(7:12);
f = f1+f2;

