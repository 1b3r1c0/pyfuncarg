# define a function that uses '**' in its parameters
def kwarg2dict(**my_name):
    print("\n-----")
    print("### kwarg2dict\n")

    ctr=1
    # Access the passed args from the dictionary
    for k,v in  my_name.items():
        print(f'kwarg {ctr}: {k}=\'{v}\'')
        ctr = ctr + 1

# define a function that will use keyword args (formal, normal)
def dict2kwarg(arg1, arg2, argN):
    print("\n-----")
    print("### kdict2kwarg\n")
    # Access the passed args like normal (foral keyword arguments)
    print(f"arg1=\'{arg1}\', arg2=\'{arg2}\',argN=\'{argN}\'")

def examples():

    # call a function that uses '**' in its parameters
    kwarg2dict(arg1='val1', arg2='val3', argN='valN')

    # use '**dict' in a call to a function with formal parameters
    # Create a dictionary of the kwargs to pass
    arg_dict = {
        'arg1': 'val1',
        'arg2': 'val3',
        'argN': 'valN'
    }

    dict2kwarg(**arg_dict)

def main():
    examples()

if __name__ == '__main__':
    main()