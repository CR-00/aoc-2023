from utils import parse_input


def cl(s):
    digits = [None, None]
    l, r = 0, len(s) - 1
    while digits[0] is None or digits[1] is None:
        if digits[0] is None:
            if s[l].isdigit():
                digits[0] = s[l]
            else:
                l += 1
        if digits[1] is None:
            if s[r].isdigit():
                digits[1] = s[r]
            else:
                r -= 1
    return int("".join(digits))


def fix(s):
    return (
        s.replace("one", "o1ne")
        .replace("two", "t2wo")
        .replace("three", "t3hree")
        .replace("four", "f4our")
        .replace("five", "f5ive")
        .replace("six", "s6ix")
        .replace("seven", "s7even")
        .replace("eight", "e8ight")
        .replace("nine", "n9ine")
    )


def part_one():
    return sum(cl(s) for s in parse_input("01"))


def part_two():
    return sum(cl(fix(s)) for s in parse_input("01"))


if __name__ == "__main__":
    print("Day 01:")
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
