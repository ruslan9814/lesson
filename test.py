def first_function(var_1, var_2, var_3):
 return var_1* 0.5 + var_2/3 + var_3 ** 4.3
function_res_1 = first_function(1, 2, 3)
print(function_res_1)
function_res_2 = first_function(var_1=1, var_3=3,
 var_2=2)
print(function_res_2)
function_res_3 = first_function(1, 2, var_3=3)
print(function_res_3)