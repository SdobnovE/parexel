def distance(x_a, y_a, x_b, y_b):
    return ((x_a - x_b) ** 2 + (y_a - y_b) ** 2) ** 0.5

def vec_len(x,y):
    return (x**2 + y**2)**0.5

def is_parallel(vec1_x, vec1_y, vec2_x, vec2_y):
    if abs(abs((vec1_x * vec2_x + vec1_y * vec2_y)
           / vec_len(vec1_x, vec1_y) / vec_len(vec2_x, vec2_y)) - 1) < 1e-6:
        return True
    return False

def is_orthogonal(vec1_x, vec1_y, vec2_x, vec2_y):
    if abs(vec1_x * vec2_x + vec1_y * vec2_y) < 1e-6:
        return True
    return False

n = int(input())

for i in range(n):
    a, x_a, y_a, b, x_b, y_b, c, x_c, y_c, d, x_d, y_d = input().split()
    x_a = int(x_a)
    y_a = int(y_a)
    x_b = int(x_b)
    y_b = int(y_b)
    x_c = int(x_c)
    y_c = int(y_c)
    x_d = int(x_d)
    y_d = int(y_d)
    
    l_ab = distance(x_a, y_a, x_b, y_b)
    l_bc = distance(x_b, y_b, x_c, y_c)
    l_cd = distance(x_c, y_c, x_d, y_d)
    l_da = distance(x_d, y_d, x_a, y_a)
    
    par_ab_cd = is_parallel(x_b-x_a, y_b-y_a, x_d-x_c, y_d-y_c)
    par_bc_da = is_parallel(x_c-x_b, y_c-y_b, x_d-x_a, y_d-y_a)
    
    orthogonal_ab_bc = is_orthogonal(x_b-x_a, y_b-y_a, x_c-x_b, y_c-y_b)
    orthogonal_bc_cd = is_orthogonal(x_c-x_b, y_c-y_b, x_d-x_c, y_d-y_c)
    orthogonal_cd_da = is_orthogonal(x_d-x_c, y_d-y_c, x_a-x_d, y_a-y_d)
    orthogonal_da_ab = is_orthogonal(x_a-x_d, y_a-y_d, x_b-x_a, y_b-y_a)
    
    rhombus = abs(l_ab - l_bc) < 1e-6 and abs(l_bc - l_cd) < 1e-6 and abs(l_cd - l_da) < 1e-6
    rectangle = orthogonal_ab_bc and orthogonal_bc_cd and orthogonal_cd_da and orthogonal_da_ab
    parallelogram = par_ab_cd and par_bc_da
    
    if rhombus and rectangle:
        print(a + b + c + d + " is a square.")
        continue
    
    if rectangle:
        print(a + b + c + d + " is a rectangle.")
        continue
        
    if rhombus:
        print(a + b + c + d + " is a rhombus.")
        continue
        
    if parallelogram:
        print(a + b + c + d + " is a parallelogram.")
        continue
        
    print(a + b + c + d + " is a quadrilateral.")	
