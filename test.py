import sys
from dataclasses import dataclass

DEBUG = False


def log(message):
    if DEBUG:
        print(message, file=sys.stderr)


class FastScanner:
    def __init__(self):
        self.tokens = []

    def next(self):
        while not self.tokens:
            self.tokens = sys.stdin.readline().split()
        return self.tokens.pop(0)

    def next_int(self):
        return int(self.next())


fs = FastScanner()


def next_token():
    return fs.next()


def next_int():
    return fs.next_int()


@dataclass(frozen=True)
class Pos:
    x: int
    y: int


@dataclass
class Inventory:
    plum: int
    lemon: int
    apple: int
    banana: int


@dataclass
class Tree:
    type: str
    x: int
    y: int
    size: int
    health: int
    fruits: int
    cooldown: int


@dataclass
class Troll:
    id: int
    player: int
    x: int
    y: int
    movement_speed: int
    carry_capacity: int
    harvest_power: int
    carry_plum: int
    carry_lemon: int
    carry_apple: int
    carry_banana: int

    def pos(self):
        return Pos(self.x, self.y)

    def carried(self):
        return self.carry_plum + self.carry_lemon + self.carry_apple + self.carry_banana

    def free_capacity(self):
        return self.carry_capacity - self.carried()


def dist(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


def is_adjacent(a, b):
    return dist(a, b) == 1


def is_inside(p, width, height):
    return 0 <= p.x < width and 0 <= p.y < height


def is_grass(p, grid, width, height):
    return is_inside(p, width, height) and grid[p.y][p.x] == "."


def adjacent_cells(p):
    return [
        Pos(p.x + 1, p.y),
        Pos(p.x - 1, p.y),
        Pos(p.x, p.y + 1),
        Pos(p.x, p.y - 1),
    ]


def nearest_drop_cell(shack, troll, grid, width, height):
    cells = [
        p for p in adjacent_cells(shack)
        if is_grass(p, grid, width, height)
    ]

    if not cells:
        return troll.pos()

    return min(cells, key=lambda p: dist(troll.pos(), p))


def train_cost(troll_count, attribute_value):
    return troll_count + attribute_value * attribute_value


def can_train(move_speed, carry_capacity, harvest_power, troll_count, inventory):
    plum_cost = train_cost(troll_count, move_speed)
    lemon_cost = train_cost(troll_count, carry_capacity)
    apple_cost = train_cost(troll_count, harvest_power)

    return (
        inventory.plum >= plum_cost
        and inventory.lemon >= lemon_cost
        and inventory.apple >= apple_cost
    )


def best_train_command(troll_count, inventory):
    if troll_count >= 5:
        return None

    options = [
        (2, 2, 2),
        (3, 2, 2),
        (2, 3, 2),
        (2, 2, 3),
        (3, 3, 2),
    ]

    for move, carry, harvest in options:
        if can_train(move, carry, harvest, troll_count, inventory):
            return f"TRAIN {move} {carry} {harvest} 0"

    return None


def best_tree_for(troll, trees, assigned):
    best_tree = None
    best_score = -10**9

    for tree in trees:
        if tree.fruits <= 0:
            continue

        if troll.free_capacity() <= 0:
            continue

        distance = dist(troll.pos(), Pos(tree.x, tree.y))
        already_assigned = assigned.get((tree.x, tree.y), 0)

        score = (
            tree.fruits * 120
            + tree.size * 12
            + troll.harvest_power * 10
            + troll.movement_speed * 5
            - distance * 10
            - already_assigned * 50
        )

        if score > best_score:
            best_score = score
            best_tree = tree

    return best_tree


def main():
    width = next_int()
    height = next_int()

    grid = []
    my_shack = Pos(0, 0)

    for y in range(height):
        row = next_token()
        grid.append(list(row))

        for x, cell in enumerate(row):
            if cell == "0":
                my_shack = Pos(x, y)

    while True:
        my_inventory = Inventory(
            plum=next_int(),
            lemon=next_int(),
            apple=next_int(),
            banana=next_int(),
        )

        # Inventaire adverse
        next_int()
        next_int()

        # Données ignorées
        for _ in range(6):
            next_int()

        tree_count = next_int()
        trees = []

        for _ in range(tree_count):
            tree = Tree(
                type=next_token(),
                x=next_int(),
                y=next_int(),
                size=next_int(),
                health=next_int(),
                fruits=next_int(),
                cooldown=next_int(),
            )
            trees.append(tree)

        trolls_count = next_int()
        my_trolls = []

        for _ in range(trolls_count):
            id_ = next_int()
            player = next_int()
            x = next_int()
            y = next_int()
            movement_speed = next_int()
            carry_capacity = next_int()
            harvest_power = next_int()

            # Donnée ignorée
            next_int()

            carry_plum = next_int()
            carry_lemon = next_int()
            carry_apple = next_int()
            carry_banana = next_int()

            # Données ignorées
            next_int()
            next_int()

            if player == 0:
                my_trolls.append(
                    Troll(
                        id=id_,
                        player=player,
                        x=x,
                        y=y,
                        movement_speed=movement_speed,
                        carry_capacity=carry_capacity,
                        harvest_power=harvest_power,
                        carry_plum=carry_plum,
                        carry_lemon=carry_lemon,
                        carry_apple=carry_apple,
                        carry_banana=carry_banana,
                    )
                )

        actions = []

        train_command = best_train_command(len(my_trolls), my_inventory)

        if train_command:
            actions.append(train_command)

        assigned_trees = {}

        for troll in my_trolls:
            troll_pos = troll.pos()

            if troll.carried() > 0:
                if is_adjacent(troll_pos, my_shack):
                    actions.append(f"DROP {troll.id}")
                else:
                    drop_target = nearest_drop_cell(
                        my_shack,
                        troll,
                        grid,
                        width,
                        height
                    )

                    actions.append(
                        f"MOVE {troll.id} {drop_target.x} {drop_target.y}"
                    )

                continue

            tree_here = next(
                (
                    tree for tree in trees
                    if tree.x == troll.x
                    and tree.y == troll.y
                    and tree.fruits > 0
                ),
                None
            )

            if tree_here is not None:
                actions.append(f"HARVEST {troll.id}")
                continue

            target = best_tree_for(troll, trees, assigned_trees)

            if target is not None:
                key = (target.x, target.y)
                assigned_trees[key] = assigned_trees.get(key, 0) + 1

                actions.append(f"MOVE {troll.id} {target.x} {target.y}")
            else:
                actions.append("WAIT")

        print(";".join(actions) if actions else "WAIT")
        sys.stdout.flush()


main()