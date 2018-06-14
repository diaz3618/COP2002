def to_feet(num):
    feet = num / 0.3048
    return feet

def to_meter(num):
    meter = num * 0.3048
    return meter

def main():
    f = 5
    m = to_meter(f)
    f = to_feet(m)

if __name__ == "__main__":
    main()
