def SPDxy(x_lis, y_lis):
    mult_lis = [x_lis[i]*y_lis[i] for i in range(len(x_lis))]
    return sum(mult_lis) - (sum(x_lis)*sum(y_lis))/len(x_lis)

def SQDx(x_lis):
    mult_lis = [i*i for i in x_lis]
    return sum(mult_lis) - ((sum(x_lis))**2)/len(x_lis)

def beta_1(x_lis, y_lis):
    return SPDxy(x_lis, y_lis)/SQDx(x_lis)

def avg(lis):
    return sum(lis)/len(lis)

def Beta_0(x_lis, y_lis):
    return avg(y_lis) - beta_1(x_lis, y_lis)*avg(x_lis)

def f(x, y, x_lis, y_lis):
    a =  beta_1(x_lis, y_lis)*x + Beta_0(x_lis, y_lis)
    print(x, y, a)
    print("Erro aprox: ", (y - a))
    return a
