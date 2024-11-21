def select(input_func):
    def output_func():
        print("************")
        input_func()
        print("************")
    return output_func()

@select
def hello():
    print("HI_P")

hello()