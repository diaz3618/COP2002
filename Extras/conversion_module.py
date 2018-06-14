def to_feet(num):
    feet = num / 0.3048
    return feet

def to_meter(num):
    meter = num * 0.3048
    return meter

def main():
    feet = 5
    meters = to_meter(feet)
    feet = to_feet(meters)
    print(str(feet) + "ft -> " + str(meters) + "m")
    print(str(meters) + "m -> " + str(feet) + "ft")

if __name__ == "__main__":
    main()
