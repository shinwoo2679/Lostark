from random import *
c1 = []
c2 = []
c3 = []
SuccesPersent = 75
c1Time = 0
c2Time = 0
c3Time = 0
times = 30

def succes(S):
    if S > 25:
        return SuccesPersent - 10
    else:
        return SuccesPersent

def fail(F):
    if F < 75:
        return SuccesPersent + 10
    else:
        return SuccesPersent

class c1Error(Exception):
    pass

class c2Error(Exception):
    pass

class c3Error(Exception):
    pass

def MakeStone(c):
    for i in range(0,10):
        if i == 9:
            if c[i] == "◈":
                print("\033[34m{0} \033[37m: {1}%".format(c[i], SuccesPersent))
            elif c[i] == "◇":
                print("\033[31m{0} \033[37m: {1}%".format(c[i], SuccesPersent))
            elif c[i] == "◆":
                print("\033[30m{0} \033[37m: {1}%".format(c[i], SuccesPersent))
        elif c[i] == "◈":
            print("\033[34m{0}".format(c[i]), end=" ")
        elif c[i] == "◇":
            print("\033[31m{0}".format(c[i]), end=" ")
        elif c[i] == "◆":
            print("\033[30m{0}".format(c[i]), end=" ")
        i += 1

for i in range(0, 10):
    c1.append("◆")
    c2.append("◆")
    c3.append("◆")

while times > 0:
    try:
        print("\033[37m남은 세공 횟수 : {0}".format(times))
        times -= 1
        print("\033[37mempty : ◆ | succes : \033[34m◈ \033[37m| fail : \033[31m◇")
        MakeStone(c1)
        MakeStone(c2)
        MakeStone(c3)

        choose = int(input("\033[37m다음중 세공할 줄을 선택하세요.(1, 2, 3) : "))
        try:
            persent = randint(0, 101)
            if choose == 1:
                if c1Time == 10:
                    times += 1
                    raise c1Error
                elif persent <= SuccesPersent:
                    SuccesPersent = succes(SuccesPersent)
                    c1[c1Time] = ("◈")
                    c1Time += 1
                elif persent >= SuccesPersent:
                    SuccesPersent = fail(SuccesPersent)
                    c1[c1Time] = ("◇")
                    c1Time += 1
            elif choose == 2:
                if c2Time == 10:
                    times += 1
                    raise c2Error
                elif persent <= SuccesPersent:
                    SuccesPersent = succes(SuccesPersent)
                    c2[c2Time] = ("◈")
                    c2Time += 1
                elif persent >= SuccesPersent:
                    SuccesPersent = fail(SuccesPersent)
                    c2[c2Time] = ("◇")
                    c2Time += 1
            elif choose == 3:
                if c3Time == 10:
                    times += 1
                    raise c3Error
                elif persent <= SuccesPersent:
                    SuccesPersent = succes(SuccesPersent)
                    c3[c3Time] = ("◈")
                    c3Time += 1
                elif persent >= SuccesPersent:
                    SuccesPersent = fail(SuccesPersent)
                    c3[c3Time] = ("◇")
                    c3Time += 1
            else:
                raise ValueError
            
            if times == 0:
                print("\n\033[37m세공결과")
                print("\033[34m저받", end="")
                for i in range(0,10):
                    if i == 9:
                        if c1[i] == "◈":
                            print("\033[34m{0} \033[37m: \033[34m{1}".format(c1[i], c1.count("◈")))
                        elif c1[i] == "◇":
                            print("\033[31m{0} \033[37m: \033[34m{1}".format(c1[i], c1.count("◈")))
                    elif c1[i] == "◈":
                        print("\033[34m{0}".format(c1[i]), end=" ")
                    elif c1[i] == "◇":
                        print("\033[31m{0}".format(c1[i]), end=" ")
                    i += 1
                print("\033[34m아드", end="")
                for i in range(0, 10):
                    if i == 9:
                        if c2[i] == "◈":
                            print("\033[34m{0} \033[37m: \033[34m{1}".format(c2[i], c2.count("◈")))
                        elif c2[i] == "◇":
                            print("\033[31m{0} \033[37m: \033[34m{1}".format(c2[i], c2.count("◈")))
                    elif c2[i] == "◈":
                        print("\033[34m{0}".format(c2[i]), end=" ")
                    elif c2[i] == "◇":
                        print("\033[31m{0}".format(c2[i]), end=" ")
                    i += 1
                print("\033[31m공감", end="")
                for i in range(0, 10):
                    if i == 9:
                        if c3[i] == "◇":
                            print("\033[34m{0} \033[37m: \033[31m{1}".format(c3[i], c3.count("◈")))
                        elif c3[i] == "◈":
                            print("\033[31m{0} \033[37m: \033[31m{1}\033[37m".format(c3[i], c3.count("◈")))
                    elif c3[i] == "◇":
                        print("\033[34m{0}".format(c3[i]), end=" ")
                    elif c3[i] == "◈":
                        print("\033[31m{0}".format(c3[i]), end=" ")
                    i += 1
                break

        except c1Error:
            print("\033[37m1번째 줄 세공이 완료 되었습니다. (2, 3)줄의 세공을 선택해 주세요.")
        except c2Error:
            print("\033[37m2번째 줄 세공이 완료 되었습니다. (1, 3)줄의 세공을 선택해 주세요.")
        except c3Error:
            print("\033[37m3번째 줄 세공이 완료 되었습니다. (1, 2)줄의 세공을 선택해 주세요.")

    except ValueError:
            times += 1
            print("\033[37m잘못된 값을 입력하였습니다. (1, 2, 3)중에 고르세요.")