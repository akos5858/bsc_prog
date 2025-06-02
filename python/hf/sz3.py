def mk_account(a=0):
    x = [a]
    def account(b=0):
        if b < 0:
            c = min(x[0], -b)
            x[0] = x[0] - c
            return c
        elif b > 0:
            x[0] += b
            return None
        else:
            return x[0]
    return account

def test_accounts():
    account = mk_account(100)
    account = mk_account(100)
    other_account = mk_account(200)
    assert account() == 100
    assert account(10) == None
    assert account() == 110
    assert account(-50) == 50
    assert account() == 60
    assert account(-80) == 60
    assert account() == 0
    assert other_account() == 200
    

if __name__ == "__main__":
    try: test_accounts()
    except AssertionError: print('test failed')
    else: print('tests succeded')




