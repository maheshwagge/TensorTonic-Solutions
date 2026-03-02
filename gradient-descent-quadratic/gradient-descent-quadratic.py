def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Minimize f(x) = ax^2 + bx + c using vanilla gradient descent.
    Return final x after 'steps' iterations.
    """
    
    x = x0
    
    for _ in range(steps):
        gradient = 2*a*x + b
        x = x - lr * gradient
        
    return x