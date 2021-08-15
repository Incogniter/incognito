def test_star(*args):
    print(args)
    for x in args:
        print(x)
test_star(0,1,2,3,4,5,6,7)