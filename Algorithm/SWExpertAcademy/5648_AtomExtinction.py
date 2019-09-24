import sys
sys.stdin = open("5648_AtomExtinction.txt", "r")


def new_x(atomObj):
    if atomObj.direction == 2:
        return atomObj.X - 1
    elif atomObj.direction == 3:
        return atomObj.X + 1
    else:
        return atomObj.X


def new_y(atomObj):
    if atomObj.direction == 1:
        return atomObj.Y - 1
    elif atomObj.direction == 0:
        return atomObj.Y + 1
    else:
        return atomObj.Y


class Atom:
    def __init__(self, X, Y, D, K):
        self.X = X
        self.Y = Y
        # 상0, 하1, 좌2, 우3
        self.direction = D
        self.K = K
        self.check = 0


T = int(input())
for tc in range(T):

    result = 0

    atoms=[]
    N = int(input())
    for n in range(N):
        coor_x, coor_y, direction, kinetic = map(int, input().split())
        atoms.append(Atom(coor_x, coor_y, direction, kinetic))

    time = 0
    while time < 2000 and atoms != []:

        collision_list = []
        time += 1

        for idx in range(len(atoms)):

            collision_sublist = []

            if not atoms[idx].check:

                if atoms[idx].direction == 0:
                    atoms[idx].Y += 1
                elif atoms[idx].direction == 1:
                    atoms[idx].Y -= 1
                elif atoms[idx].direction == 2:
                    atoms[idx].X -= 1
                elif atoms[idx].direction == 3:
                    atoms[idx].X += 1

                if atoms[idx].X < -1000:
                    collision_list.append(idx)
                    continue
                if atoms[idx].X > 1000:
                    collision_list.append(idx)
                    continue
                if atoms[idx].Y < -1000:
                    collision_list.append(idx)
                    continue
                if atoms[idx].Y > 1000:
                    collision_list.append(idx)
                    continue

                for idx_2 in range(idx+1, len(atoms)):
                    # 최종 위치가 같음
                    if (atoms[idx].X == new_x(atoms[idx_2])) and (atoms[idx].Y == new_y(atoms[idx_2])):
                        collision_sublist.append(idx_2)

                    # 교차 의심
                    elif atoms[idx].X == new_x(atoms[idx_2]):
                        if atoms[idx].direction == 1 and atoms[idx_2].direction == 0:
                            if atoms[idx].Y < new_y(atoms[idx_2]):
                                collision_sublist.clear()
                                collision_list.append(idx)
                                collision_list.append(idx_2)
                                atoms[idx].check = atoms[idx_2].check = 1
                                break

                        elif atoms[idx_2].direction == 1 and atoms[idx].direction == 0:
                            if atoms[idx].Y > new_y(atoms[idx_2]):
                                collision_sublist.clear()
                                collision_list.append(idx)
                                collision_list.append(idx_2)
                                atoms[idx].check = atoms[idx_2].check = 1
                                break

                    # 교차 의심
                    elif atoms[idx].Y == new_y(atoms[idx_2]):
                        if atoms[idx].direction == 2 and atoms[idx_2].direction == 3:
                            if atoms[idx].X < new_x(atoms[idx_2]):
                                collision_sublist.clear()
                                collision_list.append(idx)
                                collision_list.append(idx_2)
                                atoms[idx].check = atoms[idx_2].check = 1
                                break

                        elif atoms[idx_2].direction == 2 and atoms[idx].direction == 3:
                            if atoms[idx].X > new_x(atoms[idx_2]):
                                collision_sublist.clear()
                                collision_list.append(idx)
                                collision_list.append(idx_2)
                                atoms[idx].check = atoms[idx_2].check = 1
                                break

            if len(collision_sublist):
                collision_sublist.append(idx)
                for at_idx in collision_sublist:
                    atoms[at_idx].check = 1
                    collision_list.append(at_idx)

        if collision_list != []:
            collision_list.sort()
            for list_idx in range(len(collision_list)-1, -1, -1):
                # print(atoms, collision_list[list_idx])
                bye_atom = atoms.pop(collision_list[list_idx])
                if bye_atom.check:
                    result += bye_atom.K

    print("#{} {}".format(tc+1, result))
