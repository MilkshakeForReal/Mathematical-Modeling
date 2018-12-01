function[D,R] = funFloyd(a)

n = size(a,1);
k = 0
D = a
R = zeros(n ,n);
for i = 1:n
    for j = 1:n
        if (a(i,j) ~= Inf && a(i,j)~= 0)
            R(i,j) = i;
        else
            R(i ,j) = 0;
        end
    end
end
R

for k = 1:n
    for i = 1:n
        for j = 1:n
            if (D(i,k)+D(k,j)<D(i,j))
                D(i,j) = D(i,k)+D(k,j);
                R(i,j) = R(k,j);
            end
        end
    end
    k
    D
    R
end
