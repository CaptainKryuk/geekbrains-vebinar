
# * global
# x = 10
# def foo():
#     print(x)
#     x += 1
# foo()

# * lambda
# squares = []
# for x in range(5):
#     squares.append(lambda n=x: n**2)

# print(squares[0]())

# * functional
# numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

# mapped_list = list(map(lambda num: num % 2, numbers_list))

# print(mapped_list)


def main(config):
    return send_email(lambda config: config['mail'].split('@')[0] )

def send_email(username):
    print(username)


main({'mail': 'andrey@mail.ru'})